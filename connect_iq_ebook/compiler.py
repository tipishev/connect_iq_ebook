from os.path import join
from subprocess import call
from shutil import copytree
from tempfile import TemporaryDirectory

EBOOK_SOURCE_LOCATION = 'connect_iq_ebook/connect_iq/ebook'


class Compiler:

    def __init__(self, book_name, family_qualifier, xml_buffer, mc_buffer):
        self.book_name = book_name
        self.family_qualifier = family_qualifier
        self.xml_buffer = xml_buffer
        self.mc_buffer = mc_buffer
        self.device = 'fenix5'

    def copy_source(self, tmpdir):
        return copytree(EBOOK_SOURCE_LOCATION, join(tmpdir, 'workspace'))

    def write_app_name(self, app_name):
        common_resources = join(self.workspace, 'resources', 'resources.xml')
        with open(common_resources, 'r') as f:
            before_text = f.read()
        with open(common_resources, 'w') as f:
            after_text = before_text.replace('Tom Sawyer', self.book_name)
            f.write(after_text)

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

    def compile(self, output_filename='ebook.prg'):
        with TemporaryDirectory() as tmpdir:
            self.workspace = self.copy_source(tmpdir)
            self.write_app_name(self.book_name)
            self.write_xml()
            self.write_mc()
            self.generate_prg(output_filename)