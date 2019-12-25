class BigThing:

    def __init__(self, thing):
        self._my_thing = thing

    def size(self):
        if isinstance(self._my_thing, int):
            return self._my_thing
        elif isinstance(self._my_thing, dict) or isinstance(self._my_thing, list) or isinstance(self._my_thing, str):
            return len(self._my_thing)


class BigCat(BigThing):

    def __init__(self, thing, w):
        super().__init__(thing)
        self._wight = w

    def size(self):
        if self._wight > 20:
            return 'Very Fat'
        elif self._wight > 15:
            return 'Fat'
        else:
            return 'OK'


def main():
    my_thing = BigThing("balloon")
    print(my_thing.size())
    my_number = BigThing(3)
    print(my_number.size())
    cutie = BigCat("mitzy", 22)
    print(cutie.size())


if __name__ == '__main__':
    main()
