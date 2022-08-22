def sockMerchant(n, ar):
    pairs = 0
    tmp = {}
    for x in ar:
        if x not in tmp.keys():
            tmp[x] = 1
        elif x in tmp.keys():
            tmp[x] += 1
    for item in tmp.values():
        pairs += item // 2
    return pairs
