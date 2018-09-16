from unittest import TestCase
from io import StringIO

from chunker import Chunker
from .utils import unity


class TestChunker(TestCase):

    def setup_chunker(self, string, line_widths, max_chunk_size):
        buffer = StringIO(string)
        self.chunker = Chunker(buffer, max_chunk_size=max_chunk_size,
                               line_widths=line_widths, char_to_width=unity)

    def test_one_chunk(self):
        self.setup_chunker('Mary had a little lamb', [4, 4, 4], 9999)
        self.assertEqual(list(self.chunker), [
            ('Mary had a little lamb', [[0, 4, 1, 4],
                                        [9, 2, 4, 3],
                                        [18, 4, 0, 0]])]
        )

    def test_chunking(self):
        self.setup_chunker('Mary had a little lamb', [2, 2, 2], 15)
        self.assertEqual(list(self.chunker), [
            ('Mary had a ', [[0, 2, 2, 1], [5, 2, 2, 2]]),
            ('little lamb', [[0, 2, 2, 2], [6, 1, 2, 2]])])
