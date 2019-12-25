import functools

# כתבו תוכנית שמדפיסה למסך את השם הארוך ביותר בקובץ
with open('names.txt', 'r') as fh:
    print(max(fh.readlines(), key=len))
    # print(functools.reduce(lambda a, b: a if len(a) > len(b) else b, fh.readlines()))

# כתבו תוכנית שמדפיסה למסך את סכום האורכים של השמות בקובץ
with open('names.txt', 'r') as fh:
    print(sum([len(name.strip()) for name in fh.readlines()]))
    # print(len(''.join([word.strip() for word in fh.readlines()])))

# כתבו תוכנית שמדפיסה למסך את השמות הכי קצרים בקובץ, כל שם בשורה נפרדת
with open('names.txt', 'r') as fh:
    names = sorted(fh.readlines(), key=len)
    print(''.join([name for name in names if len(name) == len(names[0])]))
    # names = [word.strip() for word in fh.readlines()]
    # smallest_word_size = len(functools.reduce(lambda a, b: a if len(a) < len(b) else b, names))
    # print('\n'.join([w for w in names if len(w) == smallest_word_size]))

# כתבו תוכנית שיוצרת קובץ חדש בשם name_length.txt המכיל את האורך של כל שם בקובץ names.txt, לפי הסדר, אחד בכל שורה
with open('names.txt', 'r') as fh:
    with open('name_length.txt', 'w') as wfh:
        wfh.writelines([str(len(w.strip())) + '\n' for w in fh.readlines()])

# כתבו תוכנית שקולטת מהמשתמש מספר המייצג אורך של שם ומדפיסה את כל השמות בקובץ names.txt שהם באורך הזה
name_length = int(input('Enter name length: '))
with open('names.txt', 'r') as fh:
    print(''.join([name for name in fh.readlines() if len(name.strip()) == name_length]))
