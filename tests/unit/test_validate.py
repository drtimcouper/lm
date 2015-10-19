from nose.tools import (assert_equals, assert_raises,
                                     assert_is_none)
import lmsuite.validate as validate


def test_validate_ok_as_string():
    data = {'temperature': '23.4'}
    res = validate.validate_input(data)
    assert_is_none(res)


def test_validate_ok_as_number():
    data = {'temperature': 23.4}
    res = validate.validate_input(data)
    assert_is_none(res)


def test_validate_no_temperature_key():
    data = {}
    with assert_raises(KeyError):
        validate.validate_input(data)


def test_validate_temperature_not_a_number():
    data = {'temperature': 'junk'}
    with assert_raises(validate.NoFloatFoundError):
        validate.validate_input(data)


def test_validate_temperature_negative():
    data = {'temperature': -46}
    with assert_raises(validate.NotAPositiveNumberError):
        validate.validate_input(data)
