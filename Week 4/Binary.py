def binarySearch( theValues, target):
    # Start with the entire sequence of elements

    low = 0
    high = len(theValues) - 1

    while low <= high:

        mid = (high + low) // 2

        if theValues[mid] == target:
            return mid

        elif target < theValues[mid]: # 2 < 4
            high = mid # cuz of the shifting
            if target < theValues[high]:
                high -= 1

        else:
            low = mid  # cuz of the shifting l m h
            if target > theValues[low]:
                low += 1

    return -1  # if no matches then return -1


data = [1,2,3,4,5,6,7]
target_no = 6
print(binarySearch(data,target_no))
