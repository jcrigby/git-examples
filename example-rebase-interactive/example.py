import os
import sys
from os.path import abspath, join, dirname
import time

sys.path.insert(0, dirname(abspath(dirname('__file__'))))

from asciitor import asciitor

patrick = asciitor.gittor(user_email="patrick@nick.com",
                            user_name="Patrick Star")
patrick.prep()

#defaultsleep = 1
defaultsleep = .5

def pske(keys):
    patrick.send_keys(keys, suppress_history=False)
    time.sleep(defaultsleep)

def psk(keys):
    patrick.send_keys(keys, enter=False, suppress_history=False)
    time.sleep(defaultsleep)

pske('echo foo > foo.txt')
pske('git add foo.txt')
pske('git commit -m "added foo.txt"')
pske('echo bar > bar.txt')
pske('git add bar.txt')
pske('git commit -m "added bar.txt"')

def pupdate():
    pske('echo another foo >> foo.txt')
    pske('git add foo.txt')
    pske('git commit -m "appended to foo.txt"')
    pske('echo another bar >> bar.txt')
    pske('git add bar.txt')
    pske('git commit -m "appended to bar.txt"')

pupdate()
pupdate()
pupdate()
pupdate()

pske('git rebase -i HEAD~9')




time.sleep(9999999)


