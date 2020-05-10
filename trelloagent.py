import os
from trello import TrelloClient

os.environ['TRELLO_API_KEY'] = '<this should be prompted for during runtime>'
os.environ['TRELLO_API_SECRET'] = '<this should be prompted for during runtime>'

client = TrelloClient(
    api_key=os.environ['TRELLO_API_KEY'],
    api_secret=os.environ['TRELLO_API_SECRET']
)

all_boards = client.list_boards()
last_board = all_boards[-1]
print(last_board.name)
