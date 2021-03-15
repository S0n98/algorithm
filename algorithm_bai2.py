if __name__ == '__main__':
    y, x = int(input()), int(input())
    while(y != x):
        if x * 2 - y <= x - y / 2:
            x *= 2
        else:
            x -= 1
    print(x, y)