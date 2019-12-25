"""OOP Zoo - Exercise 2.5 of next.py course.

In this python zoo, based on object oriented programing, there are
classes for each type of animal - all inheriting from the general
Animal super-class. All the animals are instances of these classes,
but each with its own attributes values. They will all be fed (if
needed), asked to "talk" and to do something special.

* Developed & tested with Python 3.8
* Passed code style check (pycodestyle --statistics --count chapter02_pyzoo.py).

Exercise tasks summery:
1. Make Animal class with name and hunger attributes.
2. Make Dog, Cat, Skunk, Unicorn and Dragon classes.
3. Implement get_name, is_hungry and feed methods.
4. Add main function that will:
    a. Create instances of given class types with given initial
       attributes values.
    b. Add all instances to one list.
    c. Traverse list, printing each animal's type and name, and feeding
       it till it isn't hungry.
5. Add talk method to Animal class, and override it in each subclass.
   Use it after using the feed method.
6. For each animal sub class, implement a special method. Use it after
   using the talk method.
7. Implement extra attribute for Skunk and Dragon classes with given
   default values.
8. Add 5 more instances of animals.
9. Add zoo_name as a class attribute with the value "Hayaton". Print it
   once at the end of the program.
"""

# A constant of the data for the animals to be created.
# If not a 1-file-exercise, should come from an external source, e.g. file/DB.
ZOO_ANIMALS_INITIAL_INFORMATION = (
    # [0] type, [1] name, [2] hunger
    ('Dog', 'Brownie', 10),
    ('Cat', 'Zelda', 3),
    ('Skunk', 'Stinky', 0),
    ('Unicorn', 'Keith', 7),
    ('Dragon', 'Lizzy', 1450),
    ('Dog', 'Doggo', 80),
    ('Cat', 'Kitty', 80),
    ('Skunk', 'Stinky Jr.', 80),
    ('Unicorn', 'Clair', 80),
    ('Dragon', 'McFly', 80),
)


class Animal:
    """The super class for all animals of one zoo.
    Class attributes:
        zoo_name (str) - name of zoo.
    """
    zoo_name = 'Hayaton'

    def __init__(self, name, hunger=0):
        """Animal instance initialization.
        :param name: The animal name.
        :param hunger: The animal hunger amount. Default is: 0 - not hungary.
        :type name: str
        :type hunger: int
        :return: None
        """
        self._name = name
        self._hunger = hunger

    def get_name(self):
        """Return animal's name.
        :return: Value of _name attribute.
        :rtype: str
        """
        return self._name

    def is_hungry(self):
        """Check if animal is hungry.
        :return: True if _hunger value is more than 0. False otherwise.
        :rtype: bool
        """
        return self._hunger > 0

    def feed(self):
        """Feed animal, decrease the value of its _hunger attributes by 1.
        Note! _hanger value might become negative by using this method.
        :return: None
        """
        self._hunger -= 1

    def talk(self):
        """Print animal's "talk string".
        Do nothing in this super-class, should be overridden by sub-classes.
        """
        pass


class Dog(Animal):
    """A Dog - all that Animal have, its own talk and stick fetching trick"""

    def talk(self):
        """Print 2 dog barks.
        Override Animal (super-class) talk method.
        :return: None
        """
        print('woof woof')

    @staticmethod
    def fetch_stick():
        """Print dog's thoughts after returning the stick.
        :return: None
        """
        print('There you go, sir!')


class Cat(Animal):
    """A Cat - all that Animal have, its own talk and laser chasing"""

    def talk(self):
        """Print cat's meow.
        Override Animal (super-class) talk method.
        :return: None
        """
        print('meow')

    @staticmethod
    def chase_laser():
        """Print cat's sound while chasing laser.
        :return: None
        """
        print('Meeeeow')


class Skunk(Animal):
    """A Skunk - all that Animal have, its own talk and stink"""

    def __init__(self, name, hunger, stink_count=6):
        """Skunk instance initialization.
        :param name: The animal name.
        :param hunger: The animal hunger amount. Default is: 0 - not hungary.
        :param stink_count: for counting skunk's stinks. Default is: 6.
        :type name: str
        :type hunger: int
        :type stink_count: int
        :return: None
        """
        super().__init__(name, hunger)
        self._stink_count = stink_count

    def talk(self):
        """Print skunk's sound.
        Override Animal (super-class) talk method.
        :return: None
        """
        print('tsssss')

    @staticmethod
    def stink():
        """Print reaction to skunk's stink.
        :return: None
        """
        print('Dear lord!')


class Unicorn(Animal):

    def talk(self):
        """Print unicorn's speech.
        Override Animal (super-class) talk method.
        :return: None
        """
        print('Good day, darling')

    @staticmethod
    def sing():
        """Print unicorn's cover to Netta Barzilai's song.
        :return: None
        """
        print('I’m not your toy...')


class Dragon(Animal):

    def __init__(self, name, hunger, color='Green'):
        """Dragon instance initialization.
        :param name: The animal name.
        :param hunger: The animal hunger amount. Default is: 0 - not hungary.
        :param color: Dragon's color. Default is: Green.
        :type name: str
        :type hunger: int
        :type color: str
        :return: None
        """
        super().__init__(name, hunger)
        self._color = color

    def talk(self):
        """Print dragon's roar.
        Override Animal (super-class) talk method.
        :return: None
        """
        print('Raaaawr')

    @staticmethod
    def breath_fire():
        """Print dragon's fire breathing sound.
        :return: None
        """
        print('$@#$#@$')


# A dict with creator functions (value) for each animal sub-class type (key).
# The parameters for all creator functions are: name and hunger.
ANIMAL_CREATOR_DICT = {
    'Dog': lambda n, h: Dog(n, h),
    'Cat': lambda n, h: Cat(n, h),
    'Skunk': lambda n, h: Skunk(n, h),
    'Unicorn': lambda n, h: Unicorn(n, h),
    'Dragon': lambda n, h: Dragon(n, h),
}

# A dict with names of special method (vale) according to sub-class type (key).
ANIMAL_SPECIAL_METHOD = {
    'Dog': 'fetch_stick',
    'Cat': 'chase_laser',
    'Skunk': 'stink',
    'Unicorn': 'sing',
    'Dragon': 'breath_fire',
}


def main():
    """The main function running this python-zoo program.
    1. Populate zoo by creating animals according to their initial
       information and add them to the zoo's list.
    2. For each animal in the zoo:
        a. If it is hungry:
            i. Display its type and name.
            ii. Feed it until not hungry anymore.
        b. Call animal's talk method.
        c. Call animal's special method according to its type.
    3. Print zoo's name.
    """
    zoo_lst = []
    for animal in ZOO_ANIMALS_INITIAL_INFORMATION:
        zoo_lst.append(ANIMAL_CREATOR_DICT[animal[0]](animal[1], animal[2]))

    for animal in zoo_lst:
        animal_type = animal.__class__.__name__
        if animal.is_hungry():
            print(f'{animal_type} {animal.get_name()}')
            while animal.is_hungry():
                animal.feed()

        animal.talk()

        special_method = getattr(animal, ANIMAL_SPECIAL_METHOD[animal_type])
        special_method()

    print(Animal.zoo_name)


if __name__ == '__main__':
    main()
