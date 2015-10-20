class Gun:
    def fire(self):
        print('Bang')

class Vehicle:
    def __init__(self, make, colour):
        self.make = make
        self.color = colour

    @property
    def color(self):
        if self._color == 'purple':
            self._color = 'mauve'
        return self._color

    @color.setter
    def color(self, value):
        self._color = value


    def __str__(self):
        return 'I am a {0} {2} {1}'.format(
            self.__class__.__name__,
            self.make, self.color)

    def start(self):
        print ('Brrrm, brrrm')


class Car(Vehicle):
    pass


class ArmouredCar(Car, Gun):
    # choose to override the definition of start()
    def start(self):
        print ('Cough, splutter')


if __name__ == '__main__':
    # g = Gun()
    # g.fire()

    # # I can add arbitrary attributes if I *really* want to:
    # g.registered = True
    # print(g.registered)

    # c = Car('Ford','green')
    # print(c)
    # c.start()

    # v = ArmouredCar('BA-10', 'Russian grey')
    # print (v)
    # v.start()
    # v.fire()

    c = Car('BMW', 'purple')
    print(c)
