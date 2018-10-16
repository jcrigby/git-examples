import libtmux
import os
import time

ts = libtmux.Server()

class asciitor:
    def __init__(self):
        mysession = None

        self.oldsessions = ts.sessions
        print(ts)
        print(self.oldsessions)
        os.system("konsole -e tmux&")
        time.sleep(5)
        self.newsessions = ts.sessions
        print(self.newsessions)
        for ns in self.newsessions:
            print("ns is {}\n".format(ns))
            if ns not in self.oldsessions:
                print("found a new session\n")
                mysession = ns
                break
        if mysession:
            self.pane = mysession.attached_pane
        else:
            raise RuntimeError('Unable to start session')

    def send_keys(self, keys):
        self.pane.send_keys(keys)


#asc = newasciitor()


