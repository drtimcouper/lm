import os

def simple():
    print("Here are the first 10 lines of with_example.py..")
    this_dir = os.path.abspath(os.path.dirname(__file__))
    fn = os.path.join(this_dir, 'with_example.py')
    with open(fn) as f:
        for i, line in enumerate(f):
            if i>=10:
                break
            print('{:0>2d}: {}'.format(i+1, line.rstrip()))


# --------------------------------------------------------------------------------

#Qu: What makes a class usable with "with"?
#Ans: The presence of __enter__() and __exit__()methods

class MyClassWhichCanBehaveAsAContextManager:

    # lots of other methods, if required

    def __enter__(self):
        """what is returned here is the object referenced after the "as",
        assigned as we enter the new context
        """
        return self

    def __exit__(self, error_class, error_inst, error_tb):
        """We can handle any errors here on exiting the context,
        before we return back to the calling program
        """
        print ('Returning from exit ...')
        if error_class in (KeyError, IndexError):
            print ("Got them thar errors")
            return True  # True means that the exception is not to be raised


def my_context_manager():

    print ("\n---MyContextManager handling KeyError")
    with MyClassWhichCanBehaveAsAContextManager() as mine:
        print('mine variable is {}'.format(mine))
        raise KeyError

    print('.. and the program continues ..')
    print ("\n--MyContextManager with another error")
    with MyClassWhichCanBehaveAsAContextManager():
        raise ZeroDivisionError

    print('.. and the program does not continue ..')

if __name__ == '__main__':
    simple()
    my_context_manager()
