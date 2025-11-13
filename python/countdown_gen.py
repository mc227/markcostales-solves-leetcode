def countdown_gen(num):
    while num > 0:
        yield num
        num -= 1

if __name__ == "__main__":
    
    for i in countdown_gen(3):
        print(i)
