class Value:
    def __get__(self, obj, objtype):
        return self.value

    def __set__ (self, obj, value):
        value = value - (value * obj.commission)
        self.value = value

    def __str__(self):
        return str(self.value)