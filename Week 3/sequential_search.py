def sequentialSearch( theValues, target ):
    n = len( theValues )

    for i in range(n):
        # If the target is in the ith element, return True
        if theValues[i] == target:
            return True

    return False    # If not found, return False


def sortedSequentialSearch( theValues, target ):
    n = len( theValues )

    for i in range(n):
        # If the target is in the ith element, return True
        print(theValues[i])
        if theValues[i] == target:
            return True
        # If target is larger than the ith element,
        # it is not in the sequence
        elif theValues[i] > target:
            return False

    return False    # If not found, return False


# Test codes
listOfNum = [10, 7, 1, 3, -4, 2, 20]
print(sequentialSearch(listOfNum, 3))
print(sequentialSearch(listOfNum, 4))

sortedListOfNum = [-4, 1, 2, 3, 7, 10, 20]
print(sortedSequentialSearch(sortedListOfNum, 10))
print(sortedSequentialSearch(sortedListOfNum, 4))
