for x in range(100, 1000, 1):
    a = int(x / 10 % 10)
    b = int(x % 10)
    c = int(x / 100)
    if a*a*a + b*b*b + c*c*c == x:
        print('水仙花数：%d' % x)


