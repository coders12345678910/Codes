# double for loop is to check a for loop on top of a for loop

def distinct(data):
    for k in range(1, len(data)):
        for j in range(k):
            if data[j] == data[k]:
                return False
    return True


print(distinct([4,5,6,7]))

1,2,3





