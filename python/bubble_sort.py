def bubble_sort(arr):
    # basically i need two for loops
    # get the first value and compare it to elements 2 to the last
    # next loop it's second element compared to element 3 to the last
    # next its third element compared to element 4 to the last
    # i need to find a way to go through the list like that
    for i in range(len(arr)):
        print(f"i {i}")
    return arr


if __name__ == "__main__":
    numbers = [4,1,5,3,2]
    # 1 2 3 4 5
    print(bubble_sort(numbers))
