import unittest
import controller
import os


class TestController(unittest.TestCase):

    def test_sysInitialize(self):
        """should check for all variables to be initialized
        and if system is ready to operate"""
        self.assertTrue('TRELLO_API_KEY' in os.environ)
        self.assertTrue('TRELLO_API_SECRET' in os.environ)


if __name__ == '__main__':
    unittest.main()
