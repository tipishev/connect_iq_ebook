import fileinput
from os.path import join
from subprocess import call
from distutils.dir_util import copy_tree
#  from tempfile import TemporaryDirectory

EBOOK_SOURCE_LOCATION = 'connect_iq_ebook/connect_iq/ebook'


class Compiler:
    ''' responsible for making a PRG file from input text buffer '''

    # TODO pass image here?
    def __init__(self, source_buffer, devices, output_filename):
        self.devices = devices
        self.source_buffer = source_buffer
        # TODO encapsulate temporary workspace

    def copy_source(self, workspace):
        return copy_tree(EBOOK_SOURCE_LOCATION, workspace)

    def write_app_name(self, workspace, app_name):
        resources_xml = join(workspace, 'resources', 'resources.xml')
        for line in fileinput.input(resources_xml, inplace=True):
            print(line.replace('Tom Sawyer', app_name))

    def write_resources(self, workspace):
        # TODO use functools.tee to create multiple buffers
        assert len(self.devices) == 1, 'multiple devices are not implemented'
        device, = self.devices
        resources = device.make_resources(self.source_buffer)
        xml_path = join(
            workspace, f'resources-{device.family_qualifier}', 'resources.xml')
        with open(xml_path, 'w') as f:
            f.write(resources.xml)
        mc_path = join(
            workspace, f'source-{device.family_qualifier}', 'chunks_index.mc')
        with open(mc_path, 'w') as f:
            f.write(resources.mc)

    def generate_prg(self, prg_name='ebook.prg'):
        call([
            'java',
            '-Dfile.encoding=UTF-8',
            '-Dapple.awt.UIElement=true',
            '-jar', './connect_iq/monkeybrains.jar',
            '-o', prg_name,
            '-w', '-y', '/home/user/connectiq/fascinus_connect_key',
            '-d', self.device,
            '-f',  join(self.workspace, 'monkey.jungle'),
        ])

    #  def compile(self, output_filename='ebook.prg'):
    #      with TemporaryDirectory() as tmpdir:
    #          self.workspace = self.copy_source(tmpdir)
    #          self.write_app_name(self.book_name)
    #          self.write_xml()
    #          self.write_mc()
    #          self.generate_prg(output_filename)
