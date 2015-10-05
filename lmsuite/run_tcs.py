"""example to read the tcs package and allow dispatch of
a selected one
"""

import importlib


def main():
    "simulate a calling program"
    while True:
        test_case_number = input("?")
        if test_case_number.lower() == 'q':
            break
        execute_test_case(test_case_number)


def execute_test_case(test_case_number):
        try:
            tc_module = get_tc(test_case_number)
        except ImportError:
            print("Test case {} has not been defined".
                format(test_case_number))
        else:
            tc_module.main()


def get_tc(test_case_number):
    """Expects an integer which will be prefixed by tc, and
        for that module to exist in tcs subdir.
        Failure to find a test_case will raise an ImportError
    """
    module_name = 'tcs.tc{}'.format(test_case_number)
    return importlib.import_module(module_name)


if __name__ == '__main__':
    main()

