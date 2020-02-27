class Abc:
    def __init__(self, a):
        self.a = a

    def show(self):
        return self.a


obj = Abc(10)
print(obj.a, obj.show())
