class error(object):
    def __init__(self):
        self.string = "string"
        self.integer = 10

    def implemented(self):
        raise NotImplemented


class derived(error):
    def implemented(self):
        print("derived")


def type_mismatch(int=5):
    a = int + 5  # BUG, type mismatch
    stone = 5 + 5
    intone = "hi" + " yeah"
    None == 0 // caught
    by
    pylint, useless
    statement
    None == ''
    temp = stone + intone  # BUG, Type mismatch
    test = 5 if int == 5 else "hi"
    test = stone + test  # BUG, Type mismatch


def argument_type_error(a, b=False):
    print("hi")


def tuple_error():
    a = ('a', 'b', 'c')
    a[0] = 'd'

print("testing for errors")
obj = error()
type_mismatch()