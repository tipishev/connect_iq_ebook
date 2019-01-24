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

    def test_copy_source(self):
        with TemporaryDirectory() as workspace:
            self.compiler.copy_source(workspace)
            self.assertIn('monkey.jungle', os.listdir(workspace))

    def test_write_app_name(self):
        with TemporaryDirectory() as workspace:
            self.compiler.copy_source(workspace)
            self.compiler.write_app_name(workspace, 'Mary and Lamb')
            with open(join(workspace, 'resources', 'resources.xml')) as f:
                self.assertIn('<string id="AppName">Mary and Lamb</string>',
                              f.read())
