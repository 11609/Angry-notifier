import os
import random

from trello import TrelloClient
import print_util as pr


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
    print(last_board.name)
    # my_list = last_board.get

    # for card in my_list.list_cards():
    #     print(card.name)


def find_board(target: str = 'TODO'):
    print('Scanning. Target board >' + target + '<')
    todo_board = next((boardname for boardname in client.list_boards() if boardname.name == target), None)
    if todo_board is None:
        pr.err('ERROR: BOARD NOT FOUND')
    return todo_board


def print_board(board):
    print("-> " + board.name + " " + board.id + " " + board.url)
    for lst in board.all_lists():
        print("---> " + lst.name)
        for card in lst.list_cards():
            print("-----> " + card.name)
        if not lst.list_cards():
            print("-----> (no cards)")


def print_all_boards():
    all_boards = client.list_boards()
    for board in all_boards:
        print_board(board)


def connect():
    client = TrelloClient(
        api_key=os.environ['TRELLO_API_KEY'],
        api_secret=os.environ['TRELLO_API_SECRET']
    )

    # all_boards = client.list_boards()
    # last_board = all_boards[-1]
    # print(last_board.name)

    return client


def task():
    todo_board = find_board()
    # lists = todo_board.all_lists()
    for lst in todo_board.all_lists():
        # print("---> " + lst.name)
        if lst.name == 'IMPORTANT & URGENT':
            pr.okbl('found I&U list...')
            task_list = lst.list_cards()
            if task_list:
                return random.choice(task_list), 4
            else:
                pr.err('  I&U is empty')


        for card in lst.list_cards():
            print("-----> " + card.name)
        if not lst.list_cards():
            print("-----> (no cards)")
    return '', 0


def boards():
    return client.list_boards()


client = connect()

if __name__ == '__main__':
    connect()
