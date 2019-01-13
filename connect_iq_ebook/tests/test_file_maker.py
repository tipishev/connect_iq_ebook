from unittest import skip  # noqa

from unittest import TestCase

from .. import Chunker, FileMaker
from ..devices import Fenix5  # , Fenix5S

from .utils import in_this_dir, unity


class FileMakerTest(TestCase):

    maxDiff = None

    def setUp(self):
        self.file = open(in_this_dir('catch22.txt'), 'r')
        chunker = Chunker(self.file, char_to_width=unity,
                          line_widths=[25, 20, 15, 20, 25],
                          max_chunk_size=100)
        fenix5 = Fenix5()
        self.file_maker = FileMaker(chunker, device=fenix5)

    def tearDown(self):
        self.file.close()

    def test_make_xml(self):
        observed_xml = self.file_maker.make_xml()
        #  with open(in_this_dir('expected.xml'), 'w') as f:
        #      f.write(observed_xml)
        with open(in_this_dir('expected.xml'), 'r') as f:
            expected_xml = f.read()
        self.assertEqual(observed_xml, expected_xml)

    def test_make_mc(self):
        self.file_maker.make_xml()
        observed_mc = self.file_maker.make_mc()
        #  with open(in_this_dir('expected.mc'), 'w') as f:
        #      f.write(observed_mc)
        with open(in_this_dir('expected.mc'), 'r') as f:
            expected_mc = f.read()
        self.assertEqual(observed_mc, expected_mc)

    @skip
    def test_write_files(self):
        #  self.file = open(in_this_dir('catch22_full.txt'), 'r')
        #  self.file = open(in_this_dir('tom_sawyer.txt'), 'r')
        self.file = open(in_this_dir('dracula.txt'), 'r')
        Fenix5x = Fenix5
        device = Fenix5x()
        chunker = Chunker(self.file,
                          char_to_width=device.char_to_width,
                          line_widths=device.line_widths,
                          max_chunk_size=8000)
        self.file_maker = FileMaker(chunker, device=device)
        self.file_maker.write_files()
