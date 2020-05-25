import print_util as pr
import trelloagent as tr
import os

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