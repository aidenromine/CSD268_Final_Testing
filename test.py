from main import can_drive
from unittest import TestCase


class MyTestCase(TestCase):

    def test_can_drive1(self):
        self.assertEqual(can_drive(15), False)  # add assertion here

    def test_can_drive2(self):
        self.assertEqual(can_drive(16), True)  # add assertion here

    def test_can_drive3(self):
        self.assertEqual(can_drive(17), True)  # add assertion here

