def bubble_sort(arr):

    for j in range(len(arr)-1):
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp


    return arr


if __name__ == "__main__":
    numbers = [3,5,1,4,2]
    print(bubble_sort(numbers))
