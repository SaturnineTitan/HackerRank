def jumpingOnClouds(c):
    # Write your code here
    stop = len(c) - 1
    current = 0
    steps = 0
    while current != stop:
        try:
            if c[current + 2] == 0:
                current += 2
                steps += 1
            elif c[current + 1] == 0:
                current += 1
                steps += 1
        except IndexError:
            if current != stop:
                current += 1
                steps += 1
            break        
    return steps 
