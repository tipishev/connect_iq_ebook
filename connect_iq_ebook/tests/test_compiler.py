import os
from os.path import join
from io import StringIO
from tempfile import TemporaryDirectory
from unittest import TestCase

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

    def assertInFile(self, filename, string):
        with open(filename) as f:
            self.assertIn(string, f.read())

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

    # TODO patch make_resources to return short strings
    def test_write_resources(self):
        source_buffer = StringIO('Mary had a little lamb')
        fenix5.make_resources(source_buffer)
        raise NotImplementedError('check that overriden files are written')
