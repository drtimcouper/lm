from nose.tools import (assert_equals, assert_raises,
                                     assert_true, assert_false)

import lmsuite.heap as heap


def test_constructor_ok():
    h = heap.Heap(10)
    assert_true(isinstance(h, heap.Heap))


def test_constructor_size_not_floatable():
    with assert_raises(ValueError):
        heap.Heap('junk')


def test_constructor_size_negative():
    with assert_raises(heap.NegativeSizeError):
        heap.Heap(-1)


def test_len_ok():
    h = heap.Heap(10)
    assert_equals(len(h), 10)


def test_zero_size():
    h = heap.Heap(0)
    assert_equals(len(h), 0)


def test_add_ok():
    h1 = heap.Heap(11)
    h2 = heap.Heap(23)
    h3 = h1 + h2
    assert_true(isinstance(h3, heap.Heap))
    assert_equals(len(h3), 34)


def test_add_junk():
    h1 = heap.Heap(11)
    with assert_raises(TypeError):
       h1 + 23


def test_invalid_op_ok():
    with assert_raises(TypeError) as err:
        heap.invalid_op('junk')
    assert_equals(str(err.exception),
                "unsupported operand type(s) for -: 'Heap' and 'str'")

def test_sub_ok():
    h1 = heap.Heap(11)
    h2 = heap.Heap(23)
    h3 = h2 - h1
    assert_true(isinstance(h3, heap.Heap))
    assert_equals(len(h3), 12)


def test_sub_negative():
    h1 = heap.Heap(11)
    h2 = heap.Heap(24)
    with assert_raises(heap.NegativeSizeError):
       h1 - h2


def test_sub_junk():
    h1 = heap.Heap(11)
    with assert_raises(TypeError):
       h1 - 23


def test_eq_ok():
    h1 = heap.Heap(11)
    h2 = heap.Heap(11)
    assert_true(h1 == h2)
    assert_false(h1 is h2)


def test_ne_ok():
    h1 = heap.Heap(11)
    h2 = heap.Heap(15)
    assert_true(h1 != h2)


def test_lt_ok():
    h1 = heap.Heap(11)
    assert_false(h1 < h1)
    h2 = heap.Heap(23)
    assert_true(h1 < h2)


def test_ge_ok():
    h1 = heap.Heap(11)
    assert_true(h1 >= h1)
    h2 = heap.Heap(23)
    assert_true(h2 >= h1)


#__gt__ is not defined (but could be). Python will switch the arguments
# and sign of the operator and use __lt__ comparison
def test_gt_ok():
    h1 = heap.Heap(11)
    assert_false(h1 > h1)
    h0 = heap.Heap(5)
    assert_true(h1 > h0)

#__le__ is not defined. Python will switch the arguments
# and sign of the operator and use __ge__ comparison
def test_le_ok():
    h1 = heap.Heap(11)
    assert_true(h1 <= h1)
    h0 = heap.Heap(5)
    assert_true(h0 <= h1)


