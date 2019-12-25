
class Octopus:
    count_animals = 0

    def __init__(self, name='Octavio'):
        self._name = name
        self._age = 0
        Octopus.count_animals += 1

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_age(self, age):
        self._age = age


def main():
    olee = Octopus('Olee')
    oct = Octopus()
    print(f'[t0] Octopus#1 name: {olee.get_name()}\tOctopus#2 name: {oct.get_name()}')

    oct.set_name('OctiOct')
    print(f'[t1] Octopus#1 name: {olee.get_name()}\tOctopus#2 name: {oct.get_name()}')

    print(f'Octopus.count_animals: {Octopus.count_animals}')


if __name__ == '__main__':
    main()
