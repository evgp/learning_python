class SI:
    def __init__(self, start, end):
        self.current = start
        self.end = end
# __iter__ magic method, gives iteration ability to our class
    def __iter__(self):
        return self
#__next__ magic method, runs when we going to next value in our iteration range
    def __next__(self):
        if self.current >= self.end:
            raise StopIteration

        result = self.current ** 2
        self.current += 1
        return result

for n in SI(1,4):
    print(n)
