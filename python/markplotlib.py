import matplotlib.pyplot as plt


def visualize_sort(arr):
    plt.bar(range(len(arr)),arr)
    plt.show()

if __name__ == "__main__":
    visualize_sort([5,4,3,2,1])
