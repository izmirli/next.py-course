"""IDs validator/iterator/generator - Exercise 5.4 of next.py course.

This file have 3 ID numbers related utilities:
* Validation function - checking given number is a valid ID number.
* Iterator class - enable making iterator objects for traversing ID numbers.
* Generator function - enable ID numbers generation on the fly.

If this file will be run directly (not imported), it will print test sample
for the above utilities.

* Developed & tested with Python 3.8
* Passed code style check (pycodestyle chapter05_ex5.4.py).
"""
import re

MAX_ID_NUMBER = 999999999


def check_id_valid(id_number):
    """Check if given value is a valid ID number.
    Mast be a 9-digit integer (no leading zeros) and pass checksum test.

    :param id_number: ID number to check.
    :type id_number: int
    :return: True if valid ID number, False otherwise.
    :rtype: bool
    """
    if not re.search(r'^[1-9]\d{8}$', str(id_number)):
        raise ValueError(f'ID number should be a 9-digits integer '
                         f'(got: {id_number}).')

    id_as_list = list(map(int, str(id_number)))
    checksum = 0
    for i in range(9):
        factor = id_as_list[i] * (i % 2 + 1)
        checksum += factor // 10 + factor % 10 if factor > 9 else factor

    return checksum % 10 == 0


class IDIterator:
    """An iterator for ID numbers.
    Class attributes:
        max_id_number (int) - maximum ID number.
    """
    max_id_number = MAX_ID_NUMBER

    def __init__(self, start_id=0):
        """IDIterator instance initialization.
        Will raise exception if given start_id not between 0 and max_id_number.

        :param start_id: Minimal number for iterator's IDs. Default is: 0.
        :type start_id: int
        :return: None
        """
        if start_id < 0 or self.max_id_number < start_id:
            raise ValueError(f'Initial ID number mast be between 0 and '
                             f'{self.max_id_number} (got: {start_id}).')
        self._id = start_id
        self._delta = 0

    def __iter__(self):
        """Return IDs iterator.
        Will return instance to act as an iterator.

        :return: iterator instance.
        :rtype: IDIterator
        """
        return self

    def __next__(self):
        """Return next valid ID.
        * Generate next potential ID by adding _delta and _id values.
        * Increment _delta value.
        * If generated ID invalid, repeat the 2 steps above.
        * If generated ID is bigger than max_id_number, raise exception.

        :return: Valid ID number.
        :rtype: int
        """
        while True:
            next_id = self._id + self._delta
            self._delta += 1
            if next_id > self.max_id_number:
                raise StopIteration
            elif check_id_valid(next_id):
                return next_id


def id_generator(start_id):
    """Generate valid ID numbers.
    Each call for next on this function's product, will generate a Valid ID
    number. IDs will start from given start_id value and up to MAX_ID_NUMBER.
    Will raise exception if given start_id is not a Valid ID.

    :param start_id: Valid ID number for iterator's first value.
    :type start_id: int
    :return: ID numbers generator.
    :rtype: generator
    """
    if not check_id_valid(start_id):
        raise ValueError(f'Invalid ID number given ({start_id}).')
    for number in range(start_id, MAX_ID_NUMBER):
        if check_id_valid(number):
            yield number


def main():
    """Use IDIterator and print 10 IDs bigger than: 123456780."""
    try:
        id_iter = IDIterator(123456780)
    except ValueError as e:
        print(f'Failed to create IDIterator object - {e}')
    else:
        for _ in range(10):
            cur_id = next(id_iter)
            print(cur_id)


if __name__ == '__main__':
    main()
