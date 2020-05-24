from win10toast import ToastNotifier
import time
import print_util as pr
import random


class TextGen:
    headersByLv = [
        [  # lvl 0; there is nothing to do...
            'Nie zmarnuj dnia!'
        ],
        [  # lvl 1: only >UNIMPORTANT & NON-URGENT< is not empty
            'A może by tak dziś dla odmiany... cokolwiek zrobić?'
        ],
        [  # lvl 2: >URGENT< is not empty
            "How about finally doing something? LV2"
        ],
        [  # lvl 3: - >IMPORTANT< is not empty
            "How about finally doing something? LV3"
        ],
        [  # lvl 4: >IMPORTANT & URGENT< is not empty (!!!)
            "Niedługo DEADLINE !!!"
        ]
    ]

    prefixesByLv = [
        [  # lvl 0; there is nothing to do...
            'ja wiem że nie ma nic do roboty... \n'
            'Może przynajmniej angielski powtórzysz?'
        ],
        [  # lvl 1: only >UNIMPORTANT & NON-URGENT< is not empty
            'hej a może by tak '
        ],
        [  # lvl 2: >URGENT< is not empty
            'jak się nie pośpieszysz, to nie zdążysz '
        ],
        [  # lvl 3: - >IMPORTANT< is not empty
            "WAŻNE! ZRÓB TERAZ, NIE PŁACZ PÓŹNIEJ!\n",
            "PAMIĘTAJ, MUSISZ "
        ],
        [  # lvl 4: >IMPORTANT & URGENT< is not empty (!!!)
            'SZYBKO!!!  '
        ]
    ]

    @staticmethod
    def pick_header(intensity: int = 0):
        if intensity not in [0, 1, 2, 3, 4]:
            pr.err('header intensity lv incorrect! setting to lowest!')
            return random.choice(TextGen.headersByLv[0])
        return random.choice(TextGen.headersByLv[intensity])

    @staticmethod
    def pick_prefix(intensity: int = 0):
        if intensity not in [0, 1, 2, 3, 4]:
            pr.err('prefix intensity lv incorrect! setting to lowest!')
            return random.choice(TextGen.prefixesByLv[0])
        return random.choice(TextGen.prefixesByLv[intensity])


class Notifier:

    def __init__(self):
        self.toaster = ToastNotifier()

    def demo_long(self):
        self.toaster.show_toast("Hello World!!!",
                                "Python is 10 seconds awsm!",
                                icon_path="icon.ico")

        self.toaster.show_toast("Example two",
                                "This notification is in it's own thread!",
                                icon_path=None,
                                duration=5,
                                threaded=True)
        # Wait for threaded notification to finish
        while self.toaster.notification_active(): time.sleep(0.1)

    def demo(self):
        self.toaster.show_toast("Hello World!!!",
                                "Python is 10 seconds awsm!\n"
                                "Newline!",
                                icon_path="icon.ico")

    def notify(self,
               tasks: str = "zjeść kebaba",
               intensity: int = 0):
        content = TextGen.pick_prefix(intensity)
        for t in tasks:
            content += '\n-> ' + t
        pr.okbl('Notification intensity: ' + str(intensity))
        self.toaster.show_toast(TextGen.pick_header(intensity),
                                content,
                                icon_path="icon.ico",
                                duration=10,
                                threaded=True)


agent = Notifier()

if __name__ == '__main__':
    notifier = Notifier()
    notifier.demo()
