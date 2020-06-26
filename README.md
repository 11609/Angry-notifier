# Angry-notifier
![Alt Text](https://github.com/11609/Angry-notifier/blob/master/demo/demo.gif)


### Requirements:
```
pip install py-trello win10toast
```

To run, two environment variables must be set:

    TRELLO_API_KEY
    
    TRELLO_API_SECRET
    
You can learn about how to obtain those here: https://trello.com/app-key

If not set, App will simply prompt you for those :)

### Launching

    $ cd /path/to/project/Angry-notifier
    $ py .controller.py

### Trello setup

You need to have a Trello Board named "TODO".

Inside it, there should be 4 Lists:

    IMPORTANT & URGENT
    IMPORTANT
    URGENT
    UNIMPORTANT & NON-URGENT
    
Adhering to the Eisenhower's Matrix method.

https://en.wikipedia.org/wiki/Time_management#The_Eisenhower_Method

You are not required to have, or use, all 4 of them. Eisenhower himself is said to have used only two.

I recommend using at least two.

App will ignore boards other than those listed above.

Use one Trello Card per task for best results!

App will remind you about the tasks you have noted on Trello.
IMPORTANT & URGENT has the highest priority.
