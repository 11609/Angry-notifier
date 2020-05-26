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

    def test_textGen(self):
        for intensity in range(0, 5):
            text = notifier.TextGen.pick_prefix(intensity)
            self.assertNotEqual(text, '')

        text = notifier.TextGen.pick_prefix(6)  # this may comment on correcting the argument
        self.assertNotEqual(text, '')

    def test_notify(self):
        """Test if notification is being displayed"""
        displayed = notifier.agent.notify()
        self.assertIsNone(displayed)
        displayed = notifier.agent.notify(['test1', 'test2', 'test3', 'test4'])
        self.assertIsNone(displayed)


if __name__ == '__main__':
    unittest.main()
