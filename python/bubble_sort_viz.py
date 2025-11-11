import matplotlib.pyplot as plt

def bubble_sort_viz(arr):
    n = len(arr)
    iterations = 0

    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            iterations += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

            if not swapped:
                break
    return iterations

if __name__ == "__main__":
    lengths = [5, 10, 20, 50, 100]

    foo = [bubble_sort_viz(list(range(i,0,-1))) for i in lengths]

    plt.plot(lengths, foo,marker='o')
    plt.show()
