import os
from trello import TrelloClient

# those are required for the connection to work
# os.environ['TRELLO_API_KEY']
# os.environ['TRELLO_API_SECRET']


def set_key(key):
    os.environ['TRELLO_API_KEY'] = key


def set_secret(secret):
    os.environ['TRELLO_API_SECRET'] = secret


def demo():
    all_boards = client.list_boards()
    last_board = all_boards[-1]
    last_board.list_lists()
    my_list = last_board.get_list(list_id)

    for card in my_list.list_cards():
        print(card.name)


def connect():
    client = TrelloClient(
        api_key=os.environ['TRELLO_API_KEY'],
        api_secret=os.environ['TRELLO_API_SECRET']
    )

    # all_boards = client.list_boards()
    # last_board = all_boards[-1]
    # print(last_board.name)

    return client


def boards():
    return client.list_boards()


def scanBoards(target: str = 'TODO'):
    print("Scanning. Target board: " + target)
    todo_board, = (boardname for boardname in client.list_boards() if boardname.name=='TODO')
    return todo_board

client = connect()

if __name__ == '__main__':
    connect()
