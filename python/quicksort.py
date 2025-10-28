# i want to do a quick implentation of the the quicksort algorithm

# there are some recursion going on
# we cover the case when the the array is one or none

# then we look for the middle of the array if it exists

# this middle value we return the middle value
# i personally don't know what would happen if the case were odd or even
# then we define pivot
# then we define left
# then we define right
# then we return the quicksort left + middle + quicksort right

def quicksort(arr):

    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr)//2]
    left = [item for item in arr if item < pivot ]
    middle = [item for item in arr if item == pivot]
    right = [item for item in arr if item > pivot]
    return quicksort(left) + middle + quicksort(right)

if __name__ == "__main__":
    numbers = [6,5,4,3,2,1]
    print(quicksort(numbers))
