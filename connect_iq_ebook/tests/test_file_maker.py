from unittest import skip  # noqa

from unittest import TestCase

from .. import Chunker, FileMaker, devices

from .utils import in_this_dir, unity


class FileMakerTest(TestCase):

    maxDiff = None

    def setUp(self):
        self.file = open(in_this_dir('catch22.txt'), 'r')
        chunker = Chunker(self.file, char_to_width=unity,
                          line_widths=[25, 20, 15, 20, 25],
                          max_chunk_size=100)
        fenix5 = devices.fenix5
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
