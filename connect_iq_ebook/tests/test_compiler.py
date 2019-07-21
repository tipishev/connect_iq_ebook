import os
from os.path import join
from io import StringIO
from unittest import TestCase
from unittest.mock import patch, Mock
from tempfile import NamedTemporaryFile

from .. import Compiler
from ..devices import fenix5


class CompilerTest(TestCase):

    def setUp(self):
        self.compiler = Compiler(
            app_name='Mary and Lamb',
            devices=[fenix5],
            source_buffer=StringIO('Mary had a little lamb'),
        )

    # Helpers

    def assertInFile(self, filename, string):
        with open(filename) as f:
            self.assertIn(string, f.read())

    # Tests

    def test_copy_source(self):
        workspace = self.compiler.workspace.name
        self.compiler.copy_source()
        self.assertIn('monkey.jungle', os.listdir(workspace))

    def test_write_app_name(self):
        workspace = self.compiler.workspace.name
        self.compiler.copy_source()
        self.compiler.copy_source()
        common_resources = join(workspace, 'resources', 'resources.xml')
        self.assertInFile(common_resources, 'AppName">Tom Sawyer')
        self.compiler.write_app_name()
        self.assertInFile(common_resources, '"AppName">Mary and Lamb')

    @patch('connect_iq_ebook.devices.base.BaseDevice.make_resources')
    def test_write_resources(self, mock_make_resources):
        workspace = self.compiler.workspace.name

        mock_resources = Mock()
        mock_resources.xml = 'xml content'
        mock_resources.mc = 'mc content'
        mock_make_resources.return_value = mock_resources
        self.compiler.copy_source()
        self.compiler.write_resources()

        xml_path = join(workspace,
                        f'resources-{fenix5.family_qualifier}',
                        'resources.xml')
        self.assertInFile(xml_path, 'xml content')

        mc_path = join(workspace,
                       f'source-{fenix5.family_qualifier}',
                       'chunks_index.mc')
        self.assertInFile(mc_path, 'mc content')

    def test_generate_prg_buffer(self):
        self.compiler.copy_source()
        self.compiler.write_app_name()
        self.compiler.write_resources()
        prg_buffer = self.compiler.generate_prg_buffer()
        self.assertTrue(prg_buffer.readable())

    def test_compile(self):
        temporary_file = NamedTemporaryFile()
        self.compiler.compile(output_filename=temporary_file.name)
