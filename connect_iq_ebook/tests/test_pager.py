from unittest import TestCase
from io import StringIO

from ..chunker import Chunker
from .utils import unity


class PagerTest(TestCase):

    def set_pager(self, string, line_widths):
        buffer = StringIO(string)
        self.chunker = Chunker(buffer, line_widths=line_widths,
                               char_to_width=unity)
        self.pager = self.chunker.pager

    def test_1_page_2_lines(self):
        self.set_pager('ab', [1, 1])
        self.assertEqual(next(self.pager), ('ab', [0, 1, 1]))
        with self.assertRaises(StopIteration):
            next(self.pager)

    def test_2_pages_2_lines(self):
        self.set_pager('abcdefgh', [2, 2])
        self.assertEqual(list(self.pager), [('abcd', [0, 2, 2]),
                                            ('efgh', [4, 2, 2])])

    def test_variable_line_width(self):
        self.set_pager('Первое издание «Москва—Петушки»', [10, 5, 10])
        self.assertEqual(list(self.pager),
                         [('Первое издание ', [0, 7, 5, 3]),
                          ('«Москва—Петушки»', [15, 8, 5, 3])])
