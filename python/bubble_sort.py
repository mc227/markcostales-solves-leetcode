def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
if __name__ == "__main__":
    print(bubble_sort([1,4,3,2,5]))
