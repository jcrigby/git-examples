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

hello_c = """#include <stdio.h>
main()
{
    printf("Hello Beekini Bottom\\n");
}
"""

def pske(keys):
    patrick.send_keys(keys, suppress_history=False)
    time.sleep(0.5)

def psk(keys):
    patrick.send_keys(keys, enter=False, suppress_history=False)
    time.sleep(0.5)

pske("vim hello.c")
psk("i")
psk(hello_c)
psk("Escape")
pske(":wq")
pske("git add hello.c")
pske("git commit -m 'added hello.c'")
pske("git push origin HEAD:master")

def sske(keys):
    spongebob.send_keys(keys, suppress_history=False)
    time.sleep(0.5)

def ssk(keys):
    spongebob.send_keys(keys, enter=False, suppress_history=False)
    time.sleep(0.5)

sske("git remote update")
sske("git checkout master")
sske("vim hello.c")
sske("/Bee")
ssk("ctk")
ssk("Bi")
ssk("Escape")
sske(":wq")
sske("git add hello.c")
sske("git commit -m 'fix spelling error'")
sske("git push origin")
sske("git remote update")









time.sleep(9999999)


