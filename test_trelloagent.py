import unittest
import setup
import trelloagent


class TestTrelloAgent(unittest.TestCase):

    def setUp(self):
        trelloagent.client = trelloagent.connect()

    @classmethod
    def setUpClass(cls):
        pass

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_update(self):
        """test the ability to get update on trello board data"""
        pass

    def test_getTodoBoard(self):
        """T0D0 board should be obtained"""
        card = trelloagent.find_board('TODO')
        self.assertEqual(card.name, 'TODO')
        pass

    def test_getTask(self):
        """should be able to retrieve a task"""
        tasks, intensity = trelloagent.tasks()

        self.assertTrue(tasks)  # empty list would evaluate to false
        pass


if __name__ == '__main__':
    unittest.main()
