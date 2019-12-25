"""Using Generators"""
import itertools

print('Ex 4.1.2')


def translate(sentence):
    words = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the'}
    translation_gen = (words[w] for w in sentence.split())
    translated = ' '.join(translation_gen)
    return translated


print(translate("el gato esta en la casa"))

print('\nEx 4.1.2')


def is_prime(n: int):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def next_numbers(n: int):
    while True:
        n += 1
        yield n


def first_prime_over(n):
    # prime_generator = (num for num in range(n, 10 ** 100))
    # for next_num in prime_generator:
    for next_num in next_numbers(n):
        # print(f'No checking: {next_num}')
        if is_prime(next_num):
            return next_num


print(first_prime_over(1000000))

# print('\npermutate')
#
#
# def permutate(seq):
#     """permutate a sequence and return a list of the permutations"""
#     if not seq:
#         return [seq]
#     else:
#         temp_perm = []
#         for i in range(len(seq)):
#             part = seq[:i] + seq[i+1:]
#             # print(f'seq: {seq} - part: {part} (seq[:{i}]: {seq[:i]}; seq[i+1:]: {seq[i+1:]})')
#             for p in permutate(part):
#                 temp_perm.append(seq[i:i+1] + p)
#         return temp_perm
#
#
# print(permutate([0, 5, 2]))

print('\nEx 4.2.2')


def parse_ranges(ranges_string):
    range_segments = (map(int, seg.split('-')) for seg in ranges_string.split(','))
    one_range = (num for start, end in range_segments for num in range(start, end + 1))
    return one_range


print(list(parse_ranges("1-2,4-4,8-10")))
print(list(parse_ranges("0-0,4-8,20-21,43-45")))

print('\nEx 4.3.4')


def get_fibo():
    n1, n2 = 0, 1
    while True:
        yield n1
        n1, n2 = n2, n1 + n2


fibo_gen = get_fibo()
print(next(fibo_gen))
print(next(fibo_gen))
print(next(fibo_gen))
print(next(fibo_gen))

print('\nEx 4.3.4')


def gen_secs():
    for sec in range(60):
        yield sec


def gen_minutes():
    for minute in range(60):
        yield minute


def gen_hours():
    for hour in range(24):
        yield hour


def gen_time():
    for h in gen_hours():
        for m in gen_minutes():
            for s in gen_secs():
                yield f'{h:02}:{m:02}:{s:02}'


# for gt in gen_time():
#     print(gt)


def gen_years(start=2019):
    year = start
    while True:
        yield year
        year += 1


def gen_months():
    for mon in range(1, 13):
        yield mon


def gen_days(month, leap_year=True):
    this_month_days = 31
    if month in (4, 6, 9, 11):
        this_month_days = 30
    elif 2 == month:
        this_month_days = 29 if leap_year else 28

    for day in range(1, this_month_days + 1):
        yield day


def gen_date():
    for y in gen_years():
        for mon in gen_months():
            leap_year = True if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0) else False
            for d in gen_days(mon, leap_year):
                for time in gen_time():
                    yield f'{d:02}/{mon:02}/{y} {time}'


date_gen = gen_date()
for i in range(1000000 * 10):
    timestamp = next(date_gen)
    if i % 1000000 == 0:
        print(timestamp)
