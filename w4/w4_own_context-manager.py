#example counts the time spent inside our manager

import time

class timer():
    def __init__(self):
        self.start = time.time() #current time

    def current_time(self):
        return time.time() - self.start

    def __enter__(self):
        return self

    def __exit__(self, *args):
        print ('Elapsed: {}'.format(self.current_time()))

with timer() as t:
    time.sleep(1)
    print('Current: {}'.format(t.current_time()))
    time.sleep(1)