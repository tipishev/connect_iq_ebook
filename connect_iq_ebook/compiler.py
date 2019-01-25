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

    def copy_source(self, workspace):
        return copy_tree(EBOOK_SOURCE_LOCATION, workspace)

    def write_app_name(self, workspace, app_name):
        resources_xml = join(workspace, 'resources', 'resources.xml')
        for line in fileinput.input(resources_xml, inplace=True):
            print(line.replace('Tom Sawyer', app_name))

    def write_xml(self):
        filename = join(self.workspace,
                        f'resources-{self.family_qualifier}',
                        'book.xml')
        with open(filename, 'wt') as f:
            f.write(self.xml_buffer.read())

    def write_mc(self):
        filename = join(self.workspace,
                        f'source-{self.family_qualifier}',
                        'chunks_index.mc')
        with open(filename, 'wt') as f:
            f.write(self.mc_buffer.read())

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
