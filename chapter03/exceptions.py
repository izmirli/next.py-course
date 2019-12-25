"""Exceptions - Chapter 3, next.py course"""
import re
import string

print('Ex 3.1.3 - Raise Exceptions')


# StopIteration
def raise_stop_iteration_exception():
    next(iter({}))


# ZeroDivisionError
def raise_zero_division_error_exception():
    return 1 / 0


# AssertionError
def raise_assertion_error_exception():
    assert 0 == 1


# ImportError (as ModuleNotFoundError)
def raise_import_error_exception():
    # import bogus_module
    from sys import bogus


# IOError/OSError (as FileNotFoundError)
def raise_io_error_exception():
    fh = open('bogus_file')


# KeyError
def raise_key_error_exception():
    my_dict = {'a': 'bla'}
    print(my_dict['b'])


# SyntaxError
def raise_syntax_error_exception():
    eval('1 <-? "bla"')


# IndentationError
# def raise_indentation_error_exception():
#     for _ in range(1):
#     print("shouldn't be here")


# TypeError
def raise_type_error_exception():
    return 1 + 'bla'


# run all functions
all_functions = [
    raise_stop_iteration_exception,
    raise_zero_division_error_exception,
    raise_assertion_error_exception,
    raise_import_error_exception,
    raise_io_error_exception,
    raise_key_error_exception,
    raise_syntax_error_exception,
    # raise_indentation_error_exception,
    raise_type_error_exception,
]
for f in all_functions:
    try:
        f()
    except Exception as e:
        print(f'{type(e)} {e}')
    else:
        print('Error: got no Exception :)')


print('\nEx 3.2 - Exception Handling')


def read_file(file_name):
    out = '__CONTENT_START__\n'
    try:
        fh = open(file_name, 'r')
    except FileNotFoundError:
        out += '__NO_SUCH_FILE__'
    else:
        try:
            out += fh.readline().strip()
        finally:
            fh.close()
    finally:
        out += '\n__CONTENT_END__'

    return out


print('\none_lined_file:')
print(read_file("one_lined_file.txt"))
print('\nfile_does_not_exist:')
print(read_file("file_does_not_exist.txt"))


class UnderAge(Exception):

    def __init__(self, age):
        self._age = age

    def __str__(self):
        return f'Your age ({self._age}) is smaller than 18. ' \
               f'In {18 - self._age} year{"" if self._age == 17 else "s"} you could come to the party.'


def send_invitation(name, age):
    try:
        if int(age) < 18:
            raise UnderAge(age)
        else:
            print("You should send an invite to " + name)
    except UnderAge as e:
        print(e)


print('\nEx 3.3.2 - custom exception')
send_invitation('Tom', 17)
send_invitation('Jerry', 20)
send_invitation('Spike', 14)


print('\nEx 3.4 - Exceptions concluding exercise')


class UsernameContainsIllegalCharacter(Exception):

    def __init__(self, username, character, char_index=None):
        self._user = username
        self._char = character
        self._char_index = char_index

    def __str__(self):
        msg = f'Username "{self._user}" has illegal characters like: "{self._char}"'
        if self._char_index and isinstance(self._char_index, int):
            msg += f' at position {self._char_index + 1}.'
        return msg


class UsernameTooShort(Exception):

    def __init__(self, username):
        self._user = username

    def __str__(self):
        return f'Username "{self._user}" should have more than 3 characters, but have only {len(self._user)}.'


class UsernameTooLong (Exception):

    def __init__(self, username):
        self._user = username

    def __str__(self):
        return f'Username "{self._user}" should have less than 16 characters, but have: {len(self._user)}.'


class PasswordMissingCharacter(Exception):

    def __str__(self):
        return 'Password is missing mandatory characters'


class PasswordMissingUppercaseCharacter(PasswordMissingCharacter):

    def __str__(self):
        return super().__str__() + ' (Uppercase)'


class PasswordMissingLowercaseCharacter(PasswordMissingCharacter):

    def __str__(self):
        return super().__str__() + ' (Lowercase)'


class PasswordMissingDigitCharacter(PasswordMissingCharacter):

    def __str__(self):
        return super().__str__() + ' (Digit)'


class PasswordMissingSpecialCharacter(PasswordMissingCharacter):

    def __str__(self):
        return super().__str__() + ' (Special)'


class PasswordTooShort(Exception):

    def __init__(self, pass_len):
        self._pass_len = pass_len

    def __str__(self):
        return f'Password should have more than 8 characters, but have only {self._pass_len}.'


class PasswordTooLong(Exception):

    def __init__(self, pass_len):
        self._pass_len = pass_len

    def __str__(self):
        return f'Password should have less than 40 characters, but have {self._pass_len}.'


def check_input(username, password):
    if m := re.search(r'(\W)', username):
        raise UsernameContainsIllegalCharacter(username, m.group(), username.index(m.group()))
    elif len(username) < 3:
        raise UsernameTooShort(username)
    elif len(username) > 16:
        raise UsernameTooLong(username)
    elif len(password) < 8:
        raise PasswordTooShort(len(password))
    elif len(password) > 40:
        raise PasswordTooLong(len(password))
    elif not re.search(r'[a-z]', password):
        raise PasswordMissingLowercaseCharacter
    elif not re.search(r'[A-Z]', password):
        raise PasswordMissingUppercaseCharacter
    elif not re.search(r'\d', password):
        raise PasswordMissingDigitCharacter
    elif not re.search(r'[' + re.escape(string.punctuation) + r']', password):
        raise PasswordMissingSpecialCharacter
    else:
        print('OK')


test_cases = (
    ("1", "2"),
    ("0123456789ABCDEFG", "2"),
    ("A_a1.", "12345678"),
    ("A_1", "2"),
    ("A_1", "ThisIsAQuiteLongPasswordAndHonestlyUnnecessary"),
    ("A_1", "abcdefghijklmnop"),
    ("A_1", "ABCDEFGHIJLKMNOP"),
    ("A_1", "ABCDEFGhijklmnop"),
    ("A_1", "4BCD3F6h1jk1mn0p"),
    ("A_1", "4BCD3F6.1jk1mn0p"),
)
for i in range(len(test_cases)):
    print(f'Test#{i} - check_input({test_cases[i][0]}, {test_cases[i][1]}): ', end='')
    try:
        check_input(test_cases[i][0], test_cases[i][1])
    except Exception as e:
        print(f'{e.__class__.__name__} Exception: {e}')


def check_input_main():
    while True:
        user = input('Please enter your username: ')
        pw = input('Please enter your password: ')
        try:
            check_input(user, pw)
        except Exception as ex:
            print(f'Error: {ex}\n')
        else:
            break


check_input_main()
