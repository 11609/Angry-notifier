from win10toast import ToastNotifier
import time
import print_util as pr
import random


# ta klasa jest przykładem wzorca projektowego - SINGLETONU
# ponieważ interesuje nas tylko jej działanie
# nie ma potrzeby jej instancjować
class TextGen:
    arrows = ['➠', '→', '⇒', '⇝', '➔', '👉', '🤜']

    headersByLv = [
        [  # lvl 0; there is nothing to do...
            'Nie zmarnuj dnia!',
            'Szukasz inspiracji? A może...'
        ],
        [  # lvl 1: only >UNIMPORTANT & NON-URGENT< is not empty
            'A może by tak dziś... zrobić coś ciekawego?',
            'Nic pilnego... jakieś pomysły na dziś?'
        ],
        [  # lvl 2: >URGENT< is not empty
            'Pilne, ale czy ważne?',
            'Teraz albo nigdy!'
        ],
        [  # lvl 3: - >IMPORTANT< is not empty
            'Sam stwierdziłeś że to ważne 🤷‍♀️',
            'Im szybciej odchaczysz, tym lepiej 😉'
        ],
        [  # lvl 4: >IMPORTANT & URGENT< is not empty (!!!)
            'Uuu... coś ważnego do zrobienia'
        ]
    ]

    prefixesByLv = [
        [  # lvl 0; there is nothing to do...
            'Może przynajmniej angielski powtórzysz?',
            'Powtórzymy angielski?'
        ],
        [  # lvl 1: only >UNIMPORTANT & NON-URGENT< is not empty
            'Może by tak...  dla zabicia czasu...',
            'A gdyby tak w spróbować...'
        ],
        [  # lvl 2: >URGENT< is not empty
            'Dasz radę! 💪'
        ],
        [  # lvl 3: - >IMPORTANT< is not empty
            'Do it now, party later!',
            'Nothing worth doing is easy!',
            'Willing is not enough. We must do. -Bruce Lee'
        ],
        [  # lvl 4: >IMPORTANT & URGENT< is not empty (!!!)
            'To nie zające, same się nie zrobią! :D',
            'No dawaj, zrób to dziś! 😏'
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
        arrow = random.choice(TextGen.arrows)
        for t in tasks:
            content += '\n' + arrow + ' ' + t
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
