import winsound
import itertools
import timeit
import time

print('\nEx 5.1.2')
FREQUENCIES = {
    "la": 220,
    "si": 246.96,
    "do": 261.64,
    "re": 293.68,
    "mi": 329.64,
    "fa": 349.24,
    "sol": 392,
}
NOTES = "sol,250-mi,250-mi,500-fa,250-re,250-re,500-do,250-re,250-mi,250-fa,250-sol,250-sol,250-sol,500"

notes_list = NOTES.split('-')
print(f'notes_list type: {type(notes_list)} - '
      f'has __iter__: {"__iter__" in dir(notes_list)}, has __next__: {"__next__" in dir(notes_list)}')
# notes_list type: <class 'list'> - has __iter__: True, has __next__: False

notes_iter = iter(notes_list)
print(f'notes_iter type: {type(notes_iter)} - '
      f'has __iter__: {"__iter__" in dir(notes_iter)}, has __next__: {"__next__" in dir(notes_iter)}')
# notes_iter type: <class 'list_iterator'> - has __iter__: True, has __next__: True

while True:
    try:
        note = next(notes_iter)
    except StopIteration:
        break

    frequency, duration = note.split(',')
    winsound.Beep(int(FREQUENCIES[frequency]), int(duration))


print('\nEx 5.3.2 - frequencies of all notes in 5 octaves')


class MusicNotes:

    def __init__(self):
        self._base_notes = sorted(FREQUENCIES.values())
        self._first_octave = 0.25
        self._last_octave = 4
        self._notes = 7

    def __iter__(self):
        self._note_index = -1
        self._cur_octave = self._first_octave
        return self

    def __next__(self):
        if self._note_index == self._notes - 1:
            self._cur_octave *= 2
            self._note_index = 0
        else:
            self._note_index += 1

        if self._cur_octave > self._last_octave:
            raise StopIteration

        next_freq = self._base_notes[self._note_index] * self._cur_octave
        return f'{next_freq:.0f}' if int(next_freq) == next_freq else f'{next_freq:.2f}'


notes_iter = iter(MusicNotes())
for freq in notes_iter:
    print(freq, end=', ')


print('\n\nEx 5.2.2')
# שנו את הקוד כך שידפיס כל מספר שלישי בלבד, ללא שימוש בפקודת if.
# numbers = iter(list(range(1, 101)))
# for i in numbers:
#     print(i)

# simple, but not what they wanted: range(1, 101, 3)

numbers = iter(list(range(1, 101)))
for i in numbers:
    try:
        next(numbers)
        i = next(numbers)
    except StopIteration:
        break
    print(i, end=', ')


"""How many options getting to 100$ with these bills: 3x20$, 5x10$, 2x5$, 5x1$"""
print('\n\nEx 5.2.3')
# בארנק שלכם יש 3 שטרות של 20 דולר, 5 שטרות של 10 דולר, 2 שטרות של 5 דולר ו-5 שטרות של דולר אחד.
# בכמה דרכים תוכלו ליצור מהשטרות סכום של 100 שקלים?
# https://ideone.com/BUFrCY

TARGET = 100
print('\nstarted option 2 - nested loops')
start_time2 = time.time()
op_count = 0
for twenties in range(4):
    if TARGET < twenties * 20:
        break
    for tans in range(6):
        if TARGET < twenties * 20 + tans * 10:
            break
        for fifths in range(3):
            if TARGET < twenties * 20 + tans * 10 + fifths * 5:
                break
            for ones in range(6):
                this_sum = twenties * 20 + tans * 10 + fifths * 5 + ones
                if TARGET == this_sum:
                    op_count += 1
                    print(f'{twenties} * 20 + {tans} * 10 + {fifths} * 5 + {ones} * 1')
                elif TARGET < this_sum:
                    break

print(f'[{time.time() - start_time2:2.5f}] OP#2: {op_count}')

print('\nstarted option 1 - itertools')
start_time3 = time.time()
good_ops = set()
all_bills = tuple(itertools.chain(
    [20 for _ in range(3)],
    [10 for _ in range(5)],
    [5 for _ in range(2)],
    [1 for _ in range(5)],
))

for r in range(7, 14):
    for opt in itertools.combinations(all_bills, r):
        if sum(opt) == TARGET:
            good_ops.add(tuple(sorted(opt)))

print(f'[{time.time() - start_time3:0.5f}] good_ops: {len(good_ops)} -\n\t' + '\n\t'.join([str(op) for op in good_ops]))

print('\nstarted option 3 - recursive')
bills = {20: 3, 10: 5, 5: 2, 1: 5}
bills_options = set()


def pick_bills(bills_left: dict, bills_picked: list):
    global bills_options
    if sum(bills_left.values()) == 0 or sum(bills_picked) >= TARGET:
        if sum(bills_picked) == TARGET:
            bills_options.add(tuple(sorted(bills_picked)))
        return None
    for bill_type in bills_left:
        if bills_left[bill_type] == 0:
            continue
        new_bills_left = bills_left.copy()
        new_bills_left[bill_type] -= 1
        new_bills_picked = bills_picked.copy()
        new_bills_picked.append(bill_type)
        pick_bills(new_bills_left, new_bills_picked)


start_time = time.time()
pick_bills(bills, [])
print(f'[{time.time() - start_time:.5f}] bills_options: {len(bills_options)} -\n\t' +
      '\n\t'.join([str(op) for op in bills_options]))
