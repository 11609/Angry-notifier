# Angry-notifier
Requirements:
```
py-trello win10toast
```

To run, two environment variables must be set:

    TRELLO_API_KEY
    
    TRELLO_API_SECRET
    
You can learn about how to obtain those here: https://pypi.org/project/py-trello/

If not set, App will simply prompt you for those :)

## Trello setup

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

App will remind you about the tasks you have noted on Trello.
IMPORTANT & URGENT has the highest priority. If it's empty, App will remind bout the IMPORTANT ones, and so long.
