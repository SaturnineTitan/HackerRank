def solve(s):
    name = s.split(' ')
    capital = []
    for i in name:
        capital.append(i.capitalize())
    return ' '.join(capital)
