import libtmux
import os
import time
from tempfile import TemporaryDirectory as tmpdir
import subprocess

ts = libtmux.Server()

class asciitor:
    def __init__(self, *args, **kwargs):
        mysession = None

        oldsessions = ts.sessions
        os.system("konsole -e tmux&")
        for retry in range(10):
            newsessions = ts.sessions
            if newsessions != oldsessions:
                break
            time.sleep(0.5)
        for ns in reversed(newsessions):
            print("ns is {}\n".format(ns))
            if ns not in oldsessions:
                print("found a new session\n")
                mysession = ns
                break
        if mysession:
            self.pane = mysession.attached_pane
        else:
            raise RuntimeError('Unable to start session')

        self.prompt = kwargs.get('prompt', '# ')

    def send_keys(self, keys):
        self.pane.send_keys(keys)

    def prep(self):
        self.pane.send_keys('asciinema rec -i 4 -c "/bin/bash"')
        time.sleep(1)
        self.pane.send_keys('export PS1="{}"'.format(self.prompt))
        self.pane.send_keys('export LESS="-M -I -R -S"')
        for i in range(40):
            self.pane.enter()

def gitbare():
    dirpath = tmpdir()
    cmd='git init --bare'
    output = subprocess.check_output(cmd, shell=True, cwd=dirpath.name)
    return dirpath

def gitlocal(name, email):
    dirpath = tmpdir()
    cmd='''
    git init
    git config --local user.name '{}'
    git config --local user.email '{}'
    ''' . format(name, email)
    output = subprocess.check_output(cmd, shell=True, cwd=dirpath.name)
    return dirpath

class gittor(asciitor):
    def __init__(self, *args, **kwargs):
        super(gittor, self).__init__(*args, **kwargs)
        self.user_email = kwargs.get('user_email', 'joe.king@yoyodyne.com')
        self.user_name = kwargs.get('user_name', 'Joe King')
        self.remotename = kwargs.get('remotename', None)
        if self.remotename is None:
            self.remote = gitbare()
            self.remotename = self.remote.name
        self.local = gitlocal(self.user_name, self.user_email)
        self.localname = self.local.name

    def send_keys(self, keys, **kwargs):
        self.pane.send_keys(keys, **kwargs)

    def prep(self):
        self.send_keys('cd {}'.format(self.localname))
        self.send_keys('pwd'.format(self.localname))
        self.send_keys('git remote add origin {}'.format(self.remotename))
        super(gittor, self).prep()


