"""IDs - Exercise 5.4 of next.py course.

"""
import re


def check_id_valid(id_number):
    """Check if given value is a valid ID number.
    :param id_number: The animal name.
    :type id_number: int
    :return: True if valid ID number, False otherwise.
    :rtype: bool
    """
    if not re.search(r'^\d{9}$', str(id_number)):
        raise ValueError(f'ID number should have exactly 9 digits.')

    id_list = list(map(int, str(id_number)))
    checksum = 0
    for i in range(9):
        factor = id_list[i] * (i % 2 + 1)
        checksum += factor // 10 + factor % 10 if factor > 9 else factor

    return checksum % 10 == 0


class IDIterator:
    """An iterator for ID numbers.
    Class attributes:
        max_id_number (int) - maximum ID number.
    """
    max_id_number = 999999999

    def __init__(self, start_id=0):
        if start_id > self.max_id_number:
            raise ValueError(f'ID number mast have up to 9 digits.')
        self._id = start_id

    def __iter__(self):
        self._delta = 0
        return self

    def __next__(self):
        """

        """
        while True:
            next_id = self._id + self._delta
            self._delta += 1
            if check_id_valid(next_id):
                return next_id
            elif next_id > self.max_id_number:
                raise StopIteration


def id_generator(start_id):
    """

    """
    if not check_id_valid(start_id):
        raise ValueError('Invalid ID number given.')
    for number in range(start_id + 1, 999999999):
        if check_id_valid(number):
            yield number


def main():
    # IDIterator test - 10 IDs bigger than 123456780
    id_iter = iter(IDIterator(123456780))
    for _ in range(10):
        cur_id = next(id_iter)
        print(cur_id)

    # id_generator test - 9 IDs bigger than 123456782
    print('\nStart id_generator function:')
    for next_id in id_generator(123456782):
        print(next_id)
        if next_id >= 123456873:
            break


if __name__ == '__main__':
    main()

