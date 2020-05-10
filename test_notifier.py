import unittest
import notifier


class TestNotifier(unittest.TestCase):
    """Notifier
    this module is responsible for displaying notification."""

    def setUp(self):
        self.notifier = notifier.Notifier()

    @classmethod
    def setUpClass(cls):
        pass

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def  test_notify(self):
        """Test if notification is being displayed"""
        pass

    def test_composeReminder(self):
        """should compose arbitrary reminder"""
        pass

    def test_displayReminder(self):
        """should display arbitrary reminder"""
        pass

    def test_composePraise(self):
        """should compose arbitrary praise
        subprocess of displlayPraise"""
        pass

    def test_displayPraise(self):
        """should display arbitrary praise
        composePraise is it's subprocess"""
        pass


if __name__ == '__main__':
    unittest.main()
