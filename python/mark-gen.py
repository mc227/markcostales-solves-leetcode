def countdown(num):

    while num > 0:
        yield num
        num -=1


if __name__ == "__main__":
    for number in countdown(5):
        print(number)
