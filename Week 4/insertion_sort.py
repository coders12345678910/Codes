# Original
# Sorts a sequence in ascending order using the insertion sort algorithm
def insertionSort( theSeq ):
    n = len( theSeq )

    # Starts with the first item as the only sorted entry.
    for i in range(1, n):
        # Save the value to be positioned
        value = theSeq[i]

        # Find the position where value fits in the
        # ordered part of the list.
        pos = i
        while pos > 0 and value < theSeq[pos - 1]:
            # Shift the items to the right during the search
            theSeq[pos] = theSeq[pos-1]
            pos -= 1

        # Put the saved value into the open slot.
        theSeq[pos] = value

# Test codes
#list_of_numbers = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]
#print('Input List:', list_of_numbers)
#insertionSort(list_of_numbers)
#print('Sorted List:', list_of_numbers)


# Qn 2
# Sorts a sequence in ascending order using the insertion sort algorithm
def insertionSort( theSeq ):
    # Print original list (Pass 0)
    print("Insertion Sort")
    print("Pass:  0\t", theSeq)

    n = len( theSeq )

    # Starts with the first item as the only sorted entry.
    for i in range(1, n):
        # Save the value to be positioned
        value = theSeq[i]

        # Find the position where value fits in the
        # ordered part of the list.
        pos = i
        while pos > 0 and value < theSeq[pos - 1]:
            # Shift the items to the right during the search
            theSeq[pos] = theSeq[pos-1]
            pos -= 1

        # Put the saved value into the open slot.
        theSeq[pos] = value

        # Print Pass details
        print("Pass: ", i, "\t", theSeq)


# Test codes
list_of_numbers = [10, 51, 2]
insertionSort(list_of_numbers)

list_of_numbers = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]
insertionSort(list_of_numbers)
