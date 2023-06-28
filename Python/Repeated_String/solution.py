def repeatedString(s, n):
    # Write your code here
    count = 0
    num = 0
    if n % len(s) > 0:
        for i in range(0, (n % len(s))):
            if s[i] == 'a':
                count += 1
    for char in s:
        if char == 'a':
            num += 1
    count += num * (n // len(s))
    return count
