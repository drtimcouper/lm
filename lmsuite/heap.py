
class NotPositiveIntegerError(Exception):
    pass


class Heap:
    """A Heap of countable objects"""

    def __init__(self, size):
        if not float(size).is_integer() \
          or int(size) < 0:
            raise NotPositiveIntegerError("Size must be positive ('{}' found)".format(size))
        self.size = int(size)

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

    def __iadd__(self, other):
        if isinstance(other, int):
            return Heap(self.size + other)
        else:
            return self.__add__(other)

    # it might seem obvious that python can "work out" value of __ne__
    # however we must be explicit (as as != is NOT necessarily the opposite of ==)
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


def invalid_op(other):
    # use the standard python type mismatch error
    s = "unsupported operand type(s) for -: 'Heap' and '{}'".format(
        type(other).__name__)
    raise TypeError(s)

if __name__ == '__main__':   # pragma: no cover
    h1 = Heap(10)
    h2 = Heap(20)
    h3 =  h1 + 2
    print (h3)
