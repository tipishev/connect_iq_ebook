import os
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
        with TemporaryDirectory() as tmpdir:
            self.compiler.copy_source(tmpdir)
            self.assertIn('monkey.jungle', os.listdir(tmpdir))
