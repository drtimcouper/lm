class Gun:
    def __init__(self, name):
        self.name = name

    def fire(self):
        print('Bang')

class Vehicle:
    def __init__(self, make, colour):
        self.make = make
        self.color = colour

    def __str__(self):
        return 'I am a {0} {2} {1}'.format(
            self.__class__.__name__,
            self.make, self.color)


class Car(Vehicle):
    pass


class Tank(Car, Gun):
    pass

if __name__ == '__main__':
    # g = Gun('S&W')
    # print(g.name)
    # g.fire()

    v = Tank('T34', 'Russian grey')
    print (v)
    v.fire()
