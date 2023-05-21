def binarySearch_Mod( theValues, target ):
    # Start with the entire sequence of elements
    low = 0
    high = len( theValues ) - 1

    # Repeatedly subdivide the sequence in half
    # until the target is found
    while low <= high:
        # Find the midpoint of the sequence
        mid = (high + low) // 2

        # Does the midpoint contain the target?
        # If yes, return the first occurrence of the target
        if theValues[mid] == target: #value found                           # ADDED FOR 3b
            first_occurrence = mid   # index found                          # ADDED FOR 3b
            cont = True                                         # ADDED FOR 3b
            while first_occurrence > 0 and cont:                # ADDED FOR 3b
                if theValues[first_occurrence - 1] == target:   # ADDED FOR 3b
                    first_occurrence -= 1                       # ADDED FOR 3b
                else:                                           # ADDED FOR 3b
                    cont = False                                # ADDED FOR 3b
            return first_occurrence                             # ADDED FOR 3b
        # Or is the target before the midpoint?
        elif target < theValues[mid]:
            high = mid - 1
        # Or is the target after the midpoint?
        else:
            low = mid + 1

    # If the sequence cannot be subdivided further,
    # target is not in the list of values
    return -1


# Test codes
sortedListOfNum = [1, 1, 1, 2, 2, 2, 2, 33, 42, 56, 61, 70, 73, 88]
print( binarySearch_Mod( sortedListOfNum, 1))
print( binarySearch_Mod( sortedListOfNum, 2))
print( binarySearch_Mod( sortedListOfNum, 61))
print( binarySearch_Mod( sortedListOfNum, 88))
print( binarySearch_Mod( sortedListOfNum, 95))
