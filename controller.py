# this file should be empty (for now)
import sched, time
from notifier import agent as ntf
import trelloagent as tr
import print_util as pr

s = sched.scheduler(time.time, time.sleep)


def do_something(sc):
    print("Doing stuff...")
    # do my stuff
    s.enter(10, 1, do_something, (sc,))


if __name__ == '__main__':
    pr.nice("App starting")

    tr.connect()

    # tr.print_board(tr.find_board('TODO'))

    tasks, intensity = tr.tasks()

    ntf.notify(tasks=tasks, intensity=intensity)

    # s.enter(2, 1, do_something, (s,))
    # s.run()
