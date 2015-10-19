
#Qu: What makes a class usable as an iterator??
#Ans: The presence of  __iter__() & __next__() method
class MyClass:

    def __init__(self, stuff):
        self.stuff = stuff

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return self.stuff.pop()
        except IndexError:
            raise StopIteration

def basic():
    stuff = [1, 'a', (1,2), {1:2, 'a': 'another'}]
    m = MyClass(stuff)
    print (m.__next__())


def main():
    stuff = [1, 'a', (1,2), {1:2, 'a': 'another'}]
    m = MyClass(stuff)
    for value in m:
        print (value)


if __name__ == '__main__':
    #main()
    basic()
