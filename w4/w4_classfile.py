import os
from tempfile import gettempdir

class File():
    def __init__(self, path=None):
        self.path = path
        with open(path, 'w') as f:
            pass


    def __iter__(self):
        with (self.path, 'r') as f:
            return f

    def __next__(self):
        pass

    def __add__(self, obj):
        with open(os.path.join(gettempdir(),self.path[-5:-4]+obj.path[-5:]), 'w') as f:
            with open(self.path, 'r') as f1:
                r1 = f1.readlines()
            with open(obj.path, 'r') as f2:
                r2 = f2.readlines()
            f.writelines(r1+r2)       

    def __str__(self):
        return self.path
      
    def write(self, newline):
        with open(self.path, 'w') as f:
            f.write(newline)

