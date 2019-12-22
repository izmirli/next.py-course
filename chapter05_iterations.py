import winsound

print('\nEx 5.1.2')
FREQUENCIES = {
    "la": 220,
    "si": 247,
    "do": 261,
    "re": 293,
    "mi": 329,
    "fa": 349,
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


# for note in notes_list:
#     frequency, duration = note.split(',')
#     winsound.Beep(int(FREQUENCIES[frequency]), int(duration))

