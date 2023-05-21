

def sort_tup(list):
    return list[-1]


input_val = [(1, 7),(1, 3),(3, 4, 5),(2, 2)]
print(sorted(input_val,key=sort_tup))


