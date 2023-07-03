from django.test import TestCase

class DummyTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")

    def test_false_is_false(self):
        print("Method: test_false_is_false.")
        self.assertFalse(False)