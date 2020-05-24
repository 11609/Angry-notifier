from win10toast import ToastNotifier
import time


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

    def notify(self, title: str = "Title", text: str = "Some short text."):
        self.toaster.show_toast(title,
                                text,
                                icon_path="icon.ico")


agent = Notifier()

if __name__ == '__main__':
    notifier = Notifier()
    notifier.demo()
