def bubble_sort(arr):
    # loop through each array
    # so for loop length is length of the array
    # do so double for loop
    # in the inner for loop i compare the item to the one beside it
    # if it is bigger, that is  if j > j+1, then swap them
    # the case above is the worst case scenario and stuff
    # i have to add a state whether the item has been swapped
    # basically it is a way to find out if i need to go on further and stuff
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if swapped == False:
            break
    return arr
if __name__ == "__main__":
    arr = [5,4,3,2,1]
    print(bubble_sort(arr))
