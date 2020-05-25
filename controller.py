# this file should be empty (for now)
import sched, time
import setup
from notifier import agent as ntf
import trelloagent as tr
import print_util as pr

s = sched.scheduler(time.time, time.sleep)


def main_loop(sc):
    pr.okgr("Reporting: main loop tick.")
    # do my stuff

    tasks, intensity = tr.tasks()

    ntf.notify(tasks=tasks, intensity=intensity)

    # Time between alerts should depend on task's intensity.
    # If there is something important to do, notify more often.
    timeout = 4 * 60 * 60 // ((intensity + 1) ** 2)  # time in seconds
    pr.okgr("Timeout set to " + str(timeout / 60) + ' min.')

    s.enter(timeout, 1, main_loop, (sc,))


if __name__ == '__main__':
    pr.nice("App starting")

    tr.client = tr.connect()

    # tr.print_board(tr.find_board('TODO'))

    s.enter(2, 1, main_loop, (s,))
    s.run()
