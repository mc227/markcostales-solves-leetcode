def binary_search(arr, target):
    # define the lowest and highest indices
    l,h = 0, len(arr)-1

    while l <=h:
        # if middle 
        mid = (l + h)//2
        if arr[mid] == target:
            return mid
        # if target is higher
        elif arr[mid] < target:
            l = mid + 1
        # if target is lower
        else:
            h = mid - 1
    
    # catch all if target doesn't exist
    return -1

if __name__ == "__main__":
    myArray = [1,2,3,4,5]
    print(binary_search(myArray,1))
    print(binary_search(myArray,2))
    print(binary_search(myArray,3))
    print(binary_search(myArray,4))
    print(binary_search(myArray,5))