def print_formatted(number):
    # your code goes here
    pad = len(bin(number)[2:])
    for i in range(1, number + 1):
        print('{:>{width}d} {:>{width}o} {:>{width}X} {:>{width}b}'.format(i, i, i, i, width=pad))
    return
