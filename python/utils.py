import operator
import pdb

def dbg():
    pdb.set_trace()
    pass

def resize(sizes, size):
    total_before = sum(sizes)
    ratio = size / total_before
    return tuple(map(ratio.__mul__, sizes))



def add(sizes, size):
    return resize((*sizes, size), sum(sizes)-1)

def my_round(unrounded):
    # round, ensuring nearly unaltered sum
    rounded = list(map(int, map(round, unrounded)))
    error = sum(rounded) - sum(unrounded)
    # returning integers, so may not be possible to have zero error
    min_error = abs(sum(unrounded) - round(sum(unrounded)))

    if not error:
        return tuple(rounded)

    sign = 1 if error > 0 else - 1
    i = 0
    while abs(error) > min_error*1.01: # float precision
        if i > 10:
            break
        #print('rounded while error', rounded, error)
        j = i % len(rounded)
        print(i, j, error)
        term_error = rounded[j] - unrounded[j]
        if  i != j or term_error * error > 0: # same sign
            rounded[j] -= sign
            error -= sign

        i += 1
        #if i == 0:
            #print('errorrrrrr')
            #break # for testing

    #print('returning', rounded)
    return tuple(rounded)

def rounded_add(sizes, size):
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
test_assert(my_round((1.3, 1.3, 1.3)), (2, 1, 1))
