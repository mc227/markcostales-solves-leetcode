def binary_search(arr, target):
    l,h = 0, len(arr) - 1
     
    while l <= h:
        mid = int(h+l)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid + 1
        else:
            h = mid - 1
    return -1

if __name__ == "__main__":
    myArray = [1,2,3,4,5]
    print(binary_search(myArray,1))
    print(binary_search(myArray,2))
    print(binary_search(myArray,3))
    print(binary_search(myArray,4))
    print(binary_search(myArray,5))