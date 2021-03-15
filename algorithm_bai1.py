nums = '123456789'
operator = ['+', '-', 'none']
rs = [''] * 9

def next_num(i):
    num = int(nums[i])
    for x in range(i, 8):
        if rs[x] != 'none':
            return num
        num = num * 10 + int(nums[x + 1])
    return num

def check_rs():
    total = next_num(0)
    buff = 0
    for i in range(0, 8):
        if rs[i] == '+':
            buff = next_num(i + 1)
            total += buff
        if rs[i] == '-':
            buff = next_num(i + 1)
            total -= buff
    return total == 100

def print_rs():
    for i in range(8):
        oper = ' ' + rs[i] + ' ' if rs[i] != 'none' else ''
        print(f"{nums[i]}{oper}", end='')
    print(nums[8])

def gen_rs(i):
    if i == 8:
        if check_rs():
            print_rs()
        return
    for j in range(3):
        rs[i] = operator[j]
        gen_rs(i + 1)

if __name__ == '__main__':
    gen_rs(0)
    