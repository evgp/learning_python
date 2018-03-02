#magic methods playground

class MagicDict:
    def __init__(self, mydict=None):
        self.mydict = mydict or {}
        

    def __call__(self, func):
        def wrapped(*args, **kwargs):
            print("Called!")
            
            return func(*args, *kwargs)
        return wrapped

    def __getitem__(self, key):
        print("Got item!")

    def __setitem__(self, key, value):
        print("Item set!")