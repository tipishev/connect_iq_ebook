from io import StringIO
from pkgutil import get_data
from unittest import skip  # noqa

from unittest import TestCase

from .. import Chunker, ResourceMaker, devices

from .utils import unity


class ResourceMakerTest(TestCase):

    maxDiff = None

    def setUp(self):
        self.file = StringIO(get_data(__package__, 'catch22.txt').decode())
        chunker = Chunker(self.file, char_to_width=unity,
                          line_widths=[25, 20, 15, 20, 25],
                          max_chunk_size=100)
        fenix5 = devices.fenix5
        self.resource_maker = ResourceMaker(chunker, device=fenix5)

    def tearDown(self):
        self.file.close()

    def test_make_xml(self):
        observed_xml = self.resource_maker.make_xml()
        expected_xml = get_data(__package__, 'expected.xml').decode()
        self.assertEqual(observed_xml, expected_xml)

    def test_make_mc(self):
        self.resource_maker.make_xml()
        observed_mc = self.resource_maker.make_mc()
        expected_mc = get_data(__package__, 'expected.mc').decode()
        self.assertEqual(observed_mc, expected_mc)
