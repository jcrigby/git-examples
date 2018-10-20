import os
import sys
from os.path import abspath, join, dirname
import time

sys.path.insert(0, dirname(abspath(dirname('__file__'))))

from asciitor import asciitor

patrick = asciitor.gittor(user_email="patrick@nick.com",
                            user_name="Patrick Star")
patrick.prep()

spongebob = asciitor.gittor(user_email="spongebob@nick.com",
                            user_name="SpongeBob SquarePants",
                            remotename=patrick.remotename)
spongebob.prep()

def pske(keys):
    patrick.send_keys(keys, suppress_history=False)
    time.sleep(1)

def psk(keys):
    patrick.send_keys(keys, enter=False, suppress_history=False)
    time.sleep(1)

def sske(keys):
    spongebob.send_keys(keys, suppress_history=False)
    time.sleep(1)

def ssk(keys):
    spongebob.send_keys(keys, enter=False, suppress_history=False)
    time.sleep(1)


pske('echo foo > file1.txt')
pske('git add file1.txt')
pske('git commit -m "added file1.txt"')
pske('git push origin HEAD:master')

sske('git remote update')
sske('git checkout master; speechbubble 5 90 "checked out master"')
time.sleep(5)

sske('echo foo > file2.txt')
sske('git add file2.txt')
sske('git commit -m "added to file2.txt"')

pske('echo foo >> file1.txt')
pske('git add file1.txt')
pske('git commit -m "appended to file1.txt"')
pske('git push origin HEAD:master')

sske('git push')
sske('speechbubble 5 80 "push failed          \nrebase and try again "')
time.sleep(5)
sske('git pull --rebase')

def ppush():
    pske('echo foo >> file1.txt')
    pske('git add file1.txt')
    pske('git commit -m "appended to file1.txt"')
    pske('git push origin HEAD:master')

def sfail():
    sske('git push')
    sske('speechbubble 5 80 "push failed again\nrebase and try again "')
    time.sleep(5)
    sske('git pull --rebase')

ppush()
sfail()
ppush()
sfail()
ppush()
sfail()

# finally succeed
sske('git push')
#sske('speechbubble 5 80 "push succeeded!"')
sske('git lg3')
ssk(' ')
#sske('speechbubble 5 80 "history is linear                \njust one commit to add our change!"')
ssk('q')
time.sleep(0.5)
ssk('C-d')
sske('')



time.sleep(9999999)


