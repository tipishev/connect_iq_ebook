from unittest import TestCase
from io import StringIO

from .. import Chunker
from .utils import unity


class GetLineTest(TestCase):

    def set_full_text(self, string):
        buffer = StringIO(string)
        self.chunker = Chunker(buffer, char_to_width=unity)

    def get_line(self, max_width):
        return self.chunker.get_line(max_width)

    def assertBufferOffset(self, offset):
        return self.assertEqual(self.chunker.buffer.tell(), offset)

    def test_full_width_line(self):
        self.set_full_text('abc')
        line = self.get_line(3)
        self.assertEqual(line, 'abc')
        self.assertBufferOffset(3)

    def test_overflow_line(self):
        self.set_full_text('abc')
        line = self.get_line(2)
        self.assertEqual(line, 'ab')
        self.assertBufferOffset(2)

    def test_underflow_line(self):
        self.set_full_text('abc')
        line = self.get_line(4)
        self.assertEqual(line, 'abc')
        self.assertBufferOffset(3)

    def test_empty_buffer(self):
        self.set_full_text('')
        line = self.get_line(3)
        self.assertEqual(line, '')
        self.assertBufferOffset(0)

    def test_newline(self):
        self.set_full_text('ab\nc')
        line = self.get_line(3)
        self.assertEqual(line, 'ab\n')
        self.assertBufferOffset(3)

    def test_break_on_space(self):
        self.set_full_text('a b')
        line = self.get_line(2)
        self.assertEqual(line, 'a ')
        self.assertBufferOffset(2)

    def test_dont_break_words(self):
        self.set_full_text('A word wordy longasswordissimo')
        line = self.get_line(10)
        self.assertEqual(line, 'A word ')
        line = self.get_line(10)
        self.assertEqual(line, 'wordy ')
        line = self.get_line(10)
        self.assertEqual(line, 'longasswor')
        line = self.get_line(10)
        self.assertEqual(line, 'dissimo')

    def test_real_text(self):
        self.set_full_text('Первое издание «Москва—Петушки»')
        line = self.get_line(10)
        self.assertEqual(line, 'Первое ')
        line = self.get_line(5)
        self.assertEqual(line, 'издан')
        line = self.get_line(10)
        self.assertEqual(line, 'ие ')
        line = self.get_line(10)
        self.assertEqual(line, '«Москва—')
        line = self.get_line(10)
        self.assertEqual(line, 'Петушки»')
