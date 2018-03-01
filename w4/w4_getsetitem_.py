#magic methods playground

class MagicDict:
    def __init__(self, mydict=None):
        self.mydict = mydict or {}

    def __getitem__(self, key):
        print("Got item!")

    def __setitem__(self, key, value):
        print("Item set!")