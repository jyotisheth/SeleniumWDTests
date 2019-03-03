import unittest

class BaseTestCase(unittest.TestCase):

    def setUp(self):
        print("in Setup")
    def tearDown(self):
        print("in TearDown")

