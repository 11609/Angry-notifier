from win10toast import ToastNotifier
import time

class Notifier:

    def __init__(self):
        self.toaster = ToastNotifier()


    def demo(self):
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

