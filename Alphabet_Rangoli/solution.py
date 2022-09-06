def print_rangoli(size):
    # your code goes here
    rangoli = []
    for i in range(size):
        d = chr(96+size)
        for j in range(i):
            d += chr(96 + size - j - 1)
        rangoli.append('-'.join((d+d[-2::-1])).center(4*size - 3, '-'))
    print('\n'.join(rangoli+rangoli[-2::-1]))
    return
