def input_array():
    global array_in
    array_in = list(input())


def recur():
    if array_in:
        print(array_in[0], '=', ord(array_in[0]), end=', ')
        array_in.pop(0)
        recur()
    else:
        print('end!')


array_in = []
input_array()
recur()

if __name__ == '__main__':
    import doctest
    doctest.testmod()