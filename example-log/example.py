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

#defaultsleep = 1
defaultsleep = .5

def pske(keys):
    patrick.send_keys(keys, suppress_history=False)
    time.sleep(defaultsleep)

def psk(keys):
    patrick.send_keys(keys, enter=False, suppress_history=False)
    time.sleep(defaultsleep)

def sske(keys):
    spongebob.send_keys(keys, suppress_history=False)
    time.sleep(defaultsleep)

def ssk(keys):
    spongebob.send_keys(keys, enter=False, suppress_history=False)
    time.sleep(defaultsleep)

def sb(msg):
    with open("/tmp/sbtext", "w") as f:
        f.write(msg)
    sske('ssbb')

pske('echo foo > file1.txt')
pske('git add file1.txt')
pske('git commit -m "added file1.txt"')
pske('git push origin HEAD:master')
pske('git checkout -b patrick')
pske('git push origin HEAD:patrick')

sske('git remote update')
sske('git checkout -b spongebob origin/master')
sske('echo foo > file2.txt')
sske('git add file2.txt')
sske('git commit -m "added to file2.txt"')
sske('git push origin HEAD:spongebob')

def pupdate():
    pske('echo foo >> file1.txt')
    pske('git add file1.txt')
    pske('git commit -m "appended to file1.txt"')
    pske('git push origin HEAD:patrick')

def supdate():
    sske('echo foo >> file2.txt')
    sske('git add file2.txt')
    sske('git commit -m "appended to file2.txt"')
    sske('git push origin HEAD:spongebob')

pupdate()
supdate()
pupdate()
supdate()
pupdate()
supdate()

sske('git remote update')

sb("plain git log doesn't show much usefull stuff about branching")
sske('git log')
time.sleep(10)
sb("git log does have a sorta graphical option -g")
sske('git lg3')




time.sleep(9999999)


