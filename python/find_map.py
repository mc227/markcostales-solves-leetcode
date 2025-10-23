def maximum_number(arr):
    # given an array
    # set the first number as the maximum
    highest = arr[0]
    # loop through the entire array
    # compare each number to the current maximum number
    for a in arr:
    # if number is greater then current maximum
        if a >  highest:
            highest = a
    # update current maximum to that

    return highest

numbers = [1,2,3,4,5]
print(f"{maximum_number(numbers)}")