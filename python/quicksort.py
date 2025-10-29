def quicksort(arr):
    # cover the case where array is null or just on
    if len(arr) <=1:
        return arr

    # define a pivot, which is the middle of the array
    pivot = arr[len(arr)//2]
    # divide the array into left,middle and right
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # do some recursion and stuff
    return quicksort(left) + middle + quicksort(right)
if __name__ == "__main__":
    print(quicksort([5,4,3,2,1]))
