import unittest
import controller


class TestController(unittest.TestCase):
    """Controller
    This module should trigger actions of other modules.

    DISCLAIMER - currently controller is not used,
    basic it controlls are being implemented.
    """

    def setUp(self):
        pass

    @classmethod
    def setUpClass(cls):
        pass

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_sysInitialize(self):
        """should check for all variables to be initialized
        and if system is ready to operate"""
        pass

    def test_refreshTrello(self):
        """should refresf trello data"""
        pass

    def test_triggerNotification(self):
        """should create a notification"""
        pass


if __name__ == '__main__':
    unittest.main()
