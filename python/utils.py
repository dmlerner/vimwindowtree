import operator
import pdb

def dbg():
    #pdb.set_trace()
    pass

def resize(sizes, size):
    total_before = sum(sizes)
    ratio = size / total_before
    return *map(ratio.__mul__, sizes), size



def add(sizes, size):
    return resize((*sizes, size), sum(sizes)-1)
    #total_before = sum(sizes)
    #total_after = total_before - size - 1 # window divider necessitates - 1
    #ratio = total_after / total_before
    ##return *(s*ratio for s in sizes), size
    #return *map(ratio.__mul__, sizes), size

def my_round(unrounded):
    dbg()
    print('unrounded', unrounded, sum(unrounded))
    rounded = list(map(int, map(round, unrounded)))
    error = sum(rounded) - sum(unrounded)

    if not error:
        return tuple(rounded)

    sign = 1 if error > 0 else - 1
    i = 0
    while error:
        print('rounded while error', rounded, error)
        term_error = rounded[i] - unrounded[i]
        if  term_error * error > 0: # same sign
            rounded[i] -= sign
            error -= sign
        i = (i + 1) % len(rounded)
        if i == 0:
            print('errorrrrrr')
            break # for testing

    print('returning', rounded)
    return tuple(rounded)

def rounded_add(sizes, size):
    dbg()
    unrounded = add(sizes, size)
    return my_round(unrounded)


sizes = 2,4
size = 1
print(sizes, size)
#print('->', add(sizes, size), rounded_add(sizes, size))

def test_assert(actual, expected):
    print('...')
    try:
        assert expected == actual
    except:
        print(f'expected {expected} but actual {actual}')

test_assert(rounded_add((2,2), 1),(1, 1, 1))
test_assert(rounded_add((2,4), 1),(1, 3, 1))

