import operator
import pdb

def add(sizes, size):
    total_before = sum(sizes)
    total_after = total_before - size - 1 # window divider necessitates - 1
    ratio = total_after / total_before
    #return *(s*ratio for s in sizes), size
    return *map(ratio.__mul__, sizes), size

def rounded_add(sizes, size):
    unrounded = add(sizes, size)
    print('unrounded', unrounded)
    rounded = tuple(map(int, map(round, unrounded)))
    error = sum(sizes) - 1 - sum(rounded)

    if not error:
        return rounded

    sign = 1 if error > 0 else - 1
    i = 0
    while error:
        print('rounded while error', rounded)
        term_error = rounded[i] - unrounded[i]
        if  term_error * error > 0: # same sign
            rounded[i] -= sign
        i = (i + 1) % len(rounded)

    print('returning', rounded)
    return rounded

sizes = 2,4
size = 1
print(sizes, size)
print('->', add(sizes, size), rounded_add(sizes, size))

def test_assert(expected, actual):
    try:
        assert expected == actual
    except:
        print(f'expected {expected} but actual {actual}')

test_assert(rounded_add((2,2), 1),(1, 1, 1))
test_assert(rounded_add((2,4), 1),(1, 3, 1))
