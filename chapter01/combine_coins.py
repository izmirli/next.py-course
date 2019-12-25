import functools


def combine_coins(coin: str, numbers: list):
    print(', '.join([f'{coin}{num}' for num in numbers]))


print(combine_coins('$', range(5)))

# map
l1 = [1, 2, -5, 6]
l2 = [2, -1, 3, 4]
print(list(map(lambda a, b: a * b, l1, l2)))


# filter
def secret(a):
    return a % 3 != 0 and a % 5 != 0


result = filter(secret, range(1, 31))
print(list(result))


#
def double_letter(my_str: str):
    return ''.join(map(lambda s: s + s, my_str))


print(double_letter("python"))
print(double_letter("we are the champions!"))


#
def four_dividers(number: int):
    return list(filter(lambda n: n % 4 == 0, range(1, number + 1)))


print(four_dividers(9))
print(four_dividers(3))


#
def sum_of_digits(number):
    return functools.reduce(lambda a, b: a + b, [int(d) for d in str(number)[:]])


print(sum_of_digits(104))

#
print((lambda y, x: x in y) ([1, 5, 6, 9], 9))
# True


#
def is_prime(number):
    return 0 == len([n for n in range(2, number // 2) if number % n == 0])


def is_prime_r(number):
    return 0 != functools.reduce(lambda a, b: min(a, b), map(lambda x: number % x, range(2, number // 2)))


print(f'\nis_prime(42): {is_prime(42)}; is_prime_r(42): {is_prime_r(42)}.')
print(f'is_prime(43): {is_prime(43)}; is_prime_r(43): {is_prime_r(43)}.\n')


def is_funny(string: str):
    return 0 == len([c for c in string if c not in ('a', 'h')])


print(f'is_funny("hahahahahaha"): {is_funny("hahahahahaha")}')
print(is_funny("hahahahaghaha"))

# abcdefghijklmnopqrstuvwxyz
#   abcdefghijklmnopqrstuvwxyz
password = "sljmai ugrf rfc ambc: lglc dmsp mlc rum"
# print(f'pass is: ' + ''.join(map(lambda c: chr(ord(c) + 2 if ord(c) < ord('y') else ord(c) - 24), password)))
print(' '.join([''.join(map(lambda c: chr(ord(c) + 2) if ord('a') <= ord(c) <= ord('z') else c, word)) for word in password.split()]))

