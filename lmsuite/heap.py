class Heap:

    def __init__(self, size):
        self.size = int(size)
        if self.size < 0:
            raise NegativeSizeError

    def __str__(self):
        return 'A heap of size {}'.format(self.size)

    def __len__(self):
        return self.size

    def __add__(self, other):
        if isinstance(other, Heap):
            return Heap(size=self.size + other.size)
        invalid_op(other)

    def __sub__(self, other):
         if isinstance(other, Heap):
            return Heap(size=self.size - other.size)
         invalid_op(other)

    def __eq__(self, other):
        if isinstance(other, Heap):
            return self.size == other.size
        invalid_op(other)

    # it might seem obvious that python can "work out" value of __ne__
    # however we must be explicit (as not __eq__ will NOT be called otherwise)
    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
         if isinstance(other, Heap):
            return self.size < other.size
         invalid_op(other)

    def __ge__(self, other):
        return not self.__lt__(other)

    # we do not need to define __gt__ and __le__ as python will try
    # to invert the arguments and the operator. This works
    # in this case as we will only have Heap instances on each side
    # of the operator.



class NegativeSizeError(Exception):
    pass


def invalid_op(other):
    # use the standard python type mismatch error
    s = "unsupported operand type(s) for -: 'Heap' and '{}'".format(
        type(other).__name__)
    raise TypeError(s)

if __name__ == '__main__':
    h1 = Heap(10)
    h2 = Heap(20)
    h3 =  h1 + 2
    print (h3)
