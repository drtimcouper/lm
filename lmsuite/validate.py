class NoFloatFoundError(Exception):
    pass


class NotAPositiveNumberError(Exception):
    pass


def validate_input(data):
    """data is a dict, whose values are to be validated
    specific exceptions are raised if errors are found"""

    # check for temperature - must exist and be a float > 0:
    try:
        value = float(data['temperature'])
    # except KeyError:
        # this means that there is no key in the data
    #    raise   # for demonstration
    except ValueError:
        # this menas that the value there isn't float-able
        err = 'Temperature {} is not a number'.format(
            data['temperature'])
        raise NoFloatFoundError(err)
    else:
        print('this is called if there are no exceptions')
    finally:
        print ('this is always called')

    if value < 0:
        err = 'Temperature {} is not a positive number'.format(
            data['temperature'])
        raise NotAPositiveNumberError(err)

