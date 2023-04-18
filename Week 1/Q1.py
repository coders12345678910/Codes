def minmax(data):
    small = big = data[0]

    for val in data:
        if val < small:
            small = val
        elif val > big:
            big = val

    return small, big
