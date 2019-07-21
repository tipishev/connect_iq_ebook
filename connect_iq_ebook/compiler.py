import fileinput
from os.path import join
from subprocess import call
from distutils.dir_util import copy_tree
from tempfile import TemporaryDirectory

from .settings import (
    JAVA_8_PATH,
    CONNECT_IQ_BIN_DIR,
    CONNECT_IQ_DEVELOPER_KEY,
    EBOOK_SOURCE_LOCATION,
)


class Compiler:
    ''' responsible for making a PRG file from input text buffer '''

    # TODO pass app icon here?
    def __init__(self, app_name, source_buffer, devices, output_filename):
        self.app_name = app_name
        self.devices = devices
        self.output_filename = output_filename
        self.source_buffer = source_buffer
        self.workspace = TemporaryDirectory()

    def copy_source(self):
        return copy_tree(EBOOK_SOURCE_LOCATION, self.workspace.name)

    def write_app_name(self):
        resources_xml = join(self.workspace.name, 'resources', 'resources.xml')
        for line in fileinput.input(resources_xml, inplace=True):
            print(line.replace('Tom Sawyer', self.app_name))  # TODO de-Tom

    def write_resources(self):
        # TODO use functools.tee to create multiple buffers
        assert len(self.devices) == 1, 'multiple devices are not implemented'
        device, = self.devices
        resources = device.make_resources(self.source_buffer)
        # TODO deduplicate path prefix for XML and MC
        xml_path = join(
            self.workspace.name, f'resources-{device.family_qualifier}',
            'resources.xml')
        with open(xml_path, 'w') as f:
            f.write(resources.xml)
        mc_path = join(
            self.workspace.name, f'source-{device.family_qualifier}',
            'chunks_index.mc')
        with open(mc_path, 'w') as f:
            f.write(resources.mc)

    def generate_prg(self):
        assert len(self.devices) == 1, 'multiple devices are not implemented'
        device, = self.devices
        # FIXME remove absolute paths
        call([
            JAVA_8_PATH,
            '-jar', f'{CONNECT_IQ_BIN_DIR}/monkeybrains.jar',
            '-o', self.output_filename,
            #  '-w',  # show warnings
            # TODO move path to key to settings.py
            '-y', CONNECT_IQ_DEVELOPER_KEY,
            '-d', str(device),
            '-f',  join(self.workspace.name, 'monkey.jungle'),
        ])

    #  def compile(self, output_filename='ebook.prg'):
    #      with TemporaryDirectory() as tmpdir:
    #          self.workspace = self.copy_source(tmpdir)
    #          self.write_app_name(self.book_name)
    #          self.write_xml()
    #          self.write_mc()
    #          self.generate_prg(output_filename)
