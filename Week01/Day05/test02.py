def gcd(x, y):
    if x > y :(x,y) = (y,x)
    else: (x, y)
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor


def lcm(x, y):
    return x * y // gcd(x, y)

x = int(input('x = '))
y = int(input('y = '))


print('%d 和 %d 的最大公约数是：%d' % (x, y, gcd(x,y)))
print('%d 和 % d的最小公倍数是：%d' % (x, y, lcm(x,y)))

if __name__ == '__main__':
    print("输出main")