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
            tc_module = get_test_case(test_case_number)
        except ImportError:
            print("Test case {} has not been defined".
                format(test_case_number))
        else:
            tc_module.main()


def get_test_case(number):
    """Expects an test case number, which will then be
        prefixed by tc, and return a reference to the correct module
        in the tcs subdir.
        Failure to find a module for this test_case will raise an ImportError
    """
    module_name = 'tcs.tc{}'.format(number)
    return importlib.import_module(module_name)


if __name__ == '__main__':
    main()

