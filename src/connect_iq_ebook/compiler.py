import fileinput
from os.path import join
from subprocess import call
from distutils.dir_util import copy_tree
from tempfile import TemporaryDirectory
from io import BytesIO

from .settings import (
    JAVA_8_PATH,
    CONNECT_IQ_BIN_DIR,
    CONNECT_IQ_DEVELOPER_KEY,
    EBOOK_SOURCE_LOCATION,
)


class Compiler:
    ''' responsible for making a PRG file from input text buffer '''

    # TODO pass app icon here?
    def __init__(self, app_name, source_buffer, devices):
        self.app_name = app_name
        self.source_buffer = source_buffer
        self.devices = devices

        # where the java-shit madness happens
        self.workspace = TemporaryDirectory()

    def copy_source(self):
        return copy_tree(EBOOK_SOURCE_LOCATION, self.workspace.name)

    def write_app_name(self):
        resources_xml = join(self.workspace.name, 'resources', 'resources.xml')
        # FIXME the file is missing
        for line in fileinput.input(resources_xml, inplace=True):
            print(line.replace('Tom Sawyer', self.app_name))  # TODO de-Tom

    def write_resources(self):
        # TODO use functools.tee to create multiple buffers
        assert len(self.devices) == 1, 'multiple devices are not implemented'
        device = self.devices[0]
        resources = device.make_resources(self.source_buffer)
        xml_path = join(
            self.workspace.name,
            f'resources-{device.family_qualifier}',
            'resources.xml')
        with open(xml_path, 'w') as f:
            f.write(resources.xml)
        mc_path = join(
            self.workspace.name, f'source-{device.family_qualifier}',
            'chunks_index.mc')
        with open(mc_path, 'w') as f:
            f.write(resources.mc)

    def generate_prg_buffer(self):
        assert len(self.devices) == 1, 'multiple devices are not implemented'
        device = self.devices[0]
        output_path = join(self.workspace.name, 'output.prg')
        breakpoint()
        call([
            JAVA_8_PATH,
            '-jar', join(CONNECT_IQ_BIN_DIR, 'monkeybrains.jar'),
            '-o', output_path,
            #  '-w',  # show warnings
            '-y', CONNECT_IQ_DEVELOPER_KEY,
            '-d', str(device),
            '-f',  join(self.workspace.name, 'monkey.jungle'),
        ])

        with open(output_path, 'rb') as f:
            return BytesIO(f.read())

    def compile(self, output_filename):
        self.copy_source()
        # FIXME write common resources.xml
        #  self.write_app_name()
        self.write_resources()
        with open(output_filename, 'wb') as f:
            prg_buffer = self.generate_prg_buffer()
            f.write(prg_buffer.read())
