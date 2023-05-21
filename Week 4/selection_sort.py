# Original
# Sort a sequence in ascending order using the selection sort algorithm
def selectionSort( theSeq ):
    n = len( theSeq )

    for i in range(n - 1):
        # Assume the ith element is the smallest.
        smallNdx = i
        # Determine if any other element contains a smaller value.
        for j in range(i+1, n):
            if theSeq[j] < theSeq[smallNdx]:
                smallNdx = j

        # Swap the ith value and smallNdx value only if the smallest
        # value is not already in its proper position.
        if smallNdx != i:
            tmp = theSeq[i]
            theSeq[i] = theSeq[smallNdx]
            theSeq[smallNdx] = tmp


# Qn 1
# Sort a sequence in ascending or descending order using the selection sort algorithm
def selectionSort(theSeq, sortOrder):
    n = len(theSeq)

    print("Selection Sort")
    print("Pass:  0\t", theSeq)

    for i in range(n - 1):
        # Assume the ith element is the smallest/biggest.
        currNdx = i
        # Determine if any other element contains a smaller/bigger value.
        for j in range(i + 1, n):
            if sortOrder == 'A':
                if theSeq[j] < theSeq[currNdx]: # find smaller
                    currNdx = j
            elif sortOrder == 'D':
                if theSeq[j] > theSeq[currNdx]: # find bigger
                    currNdx = j

        # Swap the ith value and currNdx value only if the smallest/biggest
        # value is not already in its proper position.
        if currNdx != i:
            tmp = theSeq[i]
            theSeq[i] = theSeq[currNdx]
            theSeq[currNdx] = tmp

        # Print Pass details
        print("Pass: ", i+1, "\t", theSeq)



# Test codes
list1 = [5, 7, 3]
selectionSort(list1, 'A')
print ( list1)

list_of_numbers = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]

print('\nSorting in ascending order:')
print('Input List:', list_of_numbers)
selectionSort(list_of_numbers, 'A')
print('Sorted List:', list_of_numbers)

print('\nSorting in descending order:')
print('Input List:', list_of_numbers)
selectionSort(list_of_numbers, 'D')
print('Sorted List:', list_of_numbers)
