# script to mass open command prompts
from threading import Thread
import os

class MyThread(Thread):
    def __init__(self ,name):
        Thread.__init__(self)
        self.name = name

    def run(self):
        for i in range(100):
            msg = "%s is running" % \
                self.name
            os.system("start cmd")
            print(msg)

def create_threads():
    for i in range(100):
        name = "Thread #%s" % (i + 1)
        my_thread = MyThread(name)
        my_thread.start()


if __name__ == "__main__":
    create_threads()
