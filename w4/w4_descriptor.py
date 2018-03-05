class Value:
    def __get__(self, obj, objtype):
        return self.value

    def __set__ (self, obj, value):
        value = value - (value * obj.commission)
        self.value = value

    def __str__(self):
        return str(self.value)


    #     class Value:
    # def __init__(self):
    #     self.amount = 0

    # def __get__(self, obj, obj_type):
    #     return self.amount

    # def __set__(self, obj, value):
    #     self.amount = value - value * obj.commission