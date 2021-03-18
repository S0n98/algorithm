if __name__ == '__main__':
    y, x = int(input()), int(input())
    count = 0
    print("All step: ")
    while(y != x):
        if x * 2 - y <= x - y // 2:
            x *= 2
            print("x * 2")
        else:
            x -= 1
            print("x - 1")
        count += 1
        print(x)
    print("Total step:", count)