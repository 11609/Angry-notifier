# this file should be empty (for now)
import sched, time
from notifier import agent as ntf
import trelloagent as tr
import print_util as pr
import os

s = sched.scheduler(time.time, time.sleep)


def main_loop(sc):
    print("Doing stuff...")
    # do my stuff

    tasks, intensity = tr.tasks()

    ntf.notify(tasks=tasks, intensity=intensity)

    s.enter(60, 1, main_loop, (sc,))


if __name__ == '__main__':
    pr.nice("App starting")

    if 'TRELLO_API_KEY' not in os.environ:
        pr.err('TRELLO_API_KEY not set. Paste it here and press enter')
        new_key = input('')
        tr.set_key(new_key)
    else:
        pr.okbl('TRELLO_API_KEY found.')

    if 'TRELLO_API_SECRET' not in os.environ:
        pr.err('TRELLO_API_SECRET not set. Paste it here and press enter')
        new_secret = input('')
        tr.set_secret(new_secret)
    else:
        pr.okbl('TRELLO_API_SECRET found.')

    tr.connect()

    # tr.print_board(tr.find_board('TODO'))

    s.enter(2, 1, main_loop, (s,))
    s.run()
