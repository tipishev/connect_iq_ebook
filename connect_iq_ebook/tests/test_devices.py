from unittest import TestCase

from .. import devices


class DevicesTest(TestCase):

    maxDiff = None

    def setUp(self):
        self.fenix5 = devices.fenix5

    def test_repr(self):
        self.assertEqual(repr(self.fenix5), 'fenix5')

    def test_family_qualifyer(self):
        self.assertEqual(self.fenix5.family_qualifier, 'round-240x240')