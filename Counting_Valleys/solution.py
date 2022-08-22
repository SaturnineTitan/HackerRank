def countingValleys(steps, path):
    # Write your code here
    valleys = 0
    level = 0
    for item in path:
        if item == 'U':
            level += 1
        elif item == 'D':
            level -= 1
        if item == 'U' and level == 0:
            valleys += 1
    return valleys
