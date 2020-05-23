# this file should be empty (for now)
import sched, time
from notifier import agent as ntf
import trelloagent as tr

s = sched.scheduler(time.time, time.sleep)


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def do_something(sc):
    print("Doing stuff...")
    # do my stuff
    s.enter(10, 1, do_something, (sc,))


def nice_print(string: str):
    print(f"{bcolors.HEADER}{string}{bcolors.ENDC}")


if __name__ == '__main__':
    # print(f"{bcolors.HEADER}App launched{bcolors.ENDC}")
    nice_print("hello")

    tr.connect()

    todo_board = tr.scanBoards()
    print("board found: " + todo_board.name)

    ntf.notify(title="ZAPOMNIAŁEŚ KUPIĆ ZIEMNIAKÓW", text="JAK MOGŁEŚ")

    # s.enter(2, 1, do_something, (s,))
    # s.run()
