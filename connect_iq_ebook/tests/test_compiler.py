import os
from os.path import join
from io import StringIO
from tempfile import TemporaryDirectory
from unittest import TestCase
from unittest.mock import patch, Mock

from .. import Compiler
from ..devices import fenix5


class CompilerTest(TestCase):

    def setUp(self):
        source_buffer = StringIO('Mary had a little lamb')
        self.compiler = Compiler(
            source_buffer,
            devices=[fenix5],
            output_filename='mary.prg',
        )

    # Helpers

    def assertInFile(self, filename, string):
        with open(filename) as f:
            self.assertIn(string, f.read())

    # Tests

    def test_copy_source(self):
        with TemporaryDirectory() as workspace:
            self.compiler.copy_source(workspace)
            self.assertIn('monkey.jungle', os.listdir(workspace))

    def test_write_app_name(self):
        with TemporaryDirectory() as workspace:
            self.compiler.copy_source(workspace)
            common_resources = join(workspace, 'resources', 'resources.xml')
            self.assertInFile(common_resources, 'AppName">Tom Sawyer')
            self.compiler.write_app_name(workspace, 'Mary and Lamb')
            self.assertInFile(common_resources, '"AppName">Mary and Lamb')

    @patch('connect_iq_ebook.devices.base.BaseDevice.make_resources')
    def test_write_resources(self, mock_make_resources):
        mock_resources = Mock()
        mock_resources.xml = 'xml content'
        mock_resources.mc = 'mc content'
        mock_make_resources.return_value = mock_resources
        with TemporaryDirectory() as workspace:
            self.compiler.copy_source(workspace)
            self.compiler.write_resources(workspace)

            xml_path = join(workspace,
                            f'resources-{fenix5.family_qualifier}',
                            'resources.xml')
            self.assertInFile(xml_path, 'xml content')

            mc_path = join(workspace,
                           f'source-{fenix5.family_qualifier}',
                           'chunks_index.mc')
            self.assertInFile(mc_path, 'mc content')

    def test_generate_prg(self):
        with TemporaryDirectory() as workspace:
            self.compiler.copy_source(workspace)
            self.compiler.write_app_name(workspace, 'Mary and Lamb')
            self.compiler.write_resources(workspace)
            self.compiler.generate_prg(workspace)
