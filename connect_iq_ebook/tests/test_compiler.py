from unittest import TestCase
from io import StringIO

from .. import Compiler


class CompilerTest(TestCase):

    def setUp(self):
        self.compiler = Compiler(
            book_name='Dracula',
            family_qualifier='round-240x240',
            xml_buffer=StringIO('hello'),
            mc_buffer=StringIO('world'),
        )

    def test_copy_source(self):
        self.compiler.compile()
