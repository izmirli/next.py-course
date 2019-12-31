"""Automatic unit tests for chapter5_final_exercise
Prerequisites:
* The above script is expected to be in same directory as this test file.
* Machine should have python 3 and unittest module.
* Executed from same directory by:
    python -m unittest -v test_chapter5_final_exercise.py
"""
import unittest
import types
from chapter5_final_exercise import check_id_valid, id_generator, IDIterator


class TestIdIteratorAndGenerator(unittest.TestCase):
    """A unittest's TestCase class for testing chapter5_final_exercise.py module.
    Class attributes:
        invalid_9digit_id (int) - an invalid ID, yet 9-digits number.
        valid_id (int) - a valid ID number.
        next_valid_id (int) - ID number produced "next" after valid_id.
        second_to_last_id (int) - The second to last possible ID.
        last_valid_id (int) - The last possible ID.
    """
    invalid_9digit_id = 123456780
    valid_id = 123456782
    next_valid_id = 123456790
    second_to_last_id = 999999980
    last_valid_id = 999999998

    def test_check_id_valid(self):
        """Test check_id_valid function's usage and exceptions"""
        self.assertTrue(check_id_valid(self.valid_id), msg='Checking valid ID')
        self.assertFalse(check_id_valid(self.invalid_9digit_id), msg='Checking invalid ID')
        with self.assertRaisesRegex(ValueError, r'^ID number should be a 9-digits integer', msg='Invalid leading zeros'):
            bogus1_id_validity = check_id_valid('000123456')
        with self.assertRaisesRegex(ValueError, r'^ID number should be a 9-digits integer', msg='Invalid short ID'):
            bogus2_id_validity = check_id_valid(1234)

    def test_id_iterator(self):
        """Test IDIterator's creation, next return values and exceptions"""
        with self.assertRaisesRegex(ValueError, r'^Initial ID number mast be between', msg='Pass invalid ID to IDIterator'):
            too_long_id_iter = IDIterator(1234567890)
        id_iter = IDIterator(self.invalid_9digit_id)
        self.assertEqual(next(id_iter), self.valid_id, msg='First "next" ID is same as start ID')
        self.assertEqual(next(id_iter), self.next_valid_id, msg='Next (2nd) valid ID')
        id_iter_near_last = IDIterator(self.second_to_last_id)
        next(id_iter_near_last)
        self.assertEqual(next(id_iter_near_last), self.last_valid_id, msg='The last valid ID')
        with self.assertRaises(StopIteration, msg='End of IDIterator StopIteration'):
            next(id_iter_near_last)

    def test_id_generator(self):
        """Test id_generator function's creation, next return values and exceptions"""
        with self.assertRaisesRegex(ValueError, r'^Invalid ID number given', msg='Pass invalid ID to id_generator'):
            bogus_id_gen = id_generator(self.invalid_9digit_id)
            id_from_bogus_id_gen = next(bogus_id_gen)
        with self.assertRaisesRegex(ValueError, r'^ID number should be a 9-digits', msg='Pass short ID to id_generator'):
            short_id_gen = id_generator(1234)
            id_from_short_id_gen = next(short_id_gen)
        id_gen = id_generator(self.valid_id)
        self.assertIsInstance(id_gen, types.GeneratorType, msg='Expected GeneratorType')
        self.assertEqual(next(id_gen), self.valid_id, msg='First "next" ID is same as start ID')
        self.assertEqual(next(id_gen), self.next_valid_id, msg='Next (2nd) valid ID')
        id_gen_near_last = id_generator(self.second_to_last_id)
        next(id_gen_near_last)
        self.assertEqual(next(id_gen_near_last), self.last_valid_id, msg='The last valid ID')
        with self.assertRaises(StopIteration, msg='End of id_generator StopIteration'):
            next(id_gen_near_last)


if __name__ == '__main__':
    unittest.main()
