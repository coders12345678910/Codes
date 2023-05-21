def binarySearch( theValues, target ):
    # Start with the entire sequence of elements
    low = 0
    high = len( theValues ) - 1

    # Repeatedly subdivide the sequence in half
    # until the target is found
    while low <= high:
        # Find the midpoint of the sequence
        mid = (high + low) // 2

        # Does the midpoint contain the target?
        # If yes, return midpoint (i.e. index of the list)
        if theValues[mid] == target:
            return mid # position of found value
        # Or is the target before the midpoint?
        elif target < theValues[mid]: # go left
            high = mid - 1
        # Or is the target after the midpoint?
        else: # go right
            low = mid + 1

    # If the sequence cannot be subdivided further,
    # target is not in the list of values
    return -1


# Test codes
sortedListOfNum = [1, 2, 7, 10, 18, 25, 30, 33, 42, 56, 61, 70, 73, 88]



print( binarySearch( sortedListOfNum, 10))
print( binarySearch( sortedListOfNum, 73))
print( binarySearch( sortedListOfNum, 12))
