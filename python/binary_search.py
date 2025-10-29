def binary_search(arr, target):
    l,h = 0, len(arr)-1
    while l<=h:
        # look for the middle
        # is the middle value the same as the target
        # if so you're done
        mid = (l+h)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid + 1
        else:
            h = mid - 1



    # this covers the case where the target
    # is not present in the array
    return -1

if __name__ == "__main__":
    print(binary_search([1,2,3,4,5],6))
    print(binary_search([1,2,3,4,5],3))
    print(binary_search([1,2,3,4,5],2))
