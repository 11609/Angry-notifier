import os
import unittest
import trelloagent


class TestTrelloAgent(unittest.TestCase):

    def setUp(self):
        self.agent = trelloagent.Agent()

    @classmethod
    def setUpClass(cls):
        pass

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_promptApiKey(self):
        """user should be prompted to enter api credentials"""
        pass

    def test_ApiKey(self):
        self.assertEqual(os.environ['TRELLO_API_KEY'], '<insert correct api key here>');
        pass

    def test_update(self):
        """test the ability to get update trello board data"""
        pass

    def test_setApiKey(self):
        """tests functionality of resetting api key"""
        self.agent.setApiKey('fake_Key')
        self.assertEqual(self.agent.apiKey, 'fake_key')


    def test_getTodoCard(self):
        """t0d0 card should be obtained from downloaded data"""
        pass

    def test_getTask(self):
        """should be able to retrieve a task"""
        pass

    def test_rateProductivity(self):
        """rates productivity based on completed activities"""
        pass


if __name__ == '__main__':
    unittest.main()
