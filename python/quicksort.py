def quicksort(arr):
    # case where array is blank or single
    if len(arr) <= 1:
        return arr
    # calculate the middle and set it to pivot
    pivot = arr[len(arr)//2]
    # calculate the numbers below the middle
    left = [x for x in arr if x < pivot]
    # calcualte the middle number
    middle = [x for x in arr if x == pivot]
    # calculate the numbers on the right
    right = [x for x in arr if x > pivot]
    # add them all up
    return quicksort(left) + middle + quicksort(right)

if __name__ == "__main__":
    numbers = [5,4,3,2,1]
    print(quicksort(numbers))
