"""
输入一个正整数判断它是不是素数

Version: 0.1
Author: lirong
Date: 2019-9-24 16:31:49
"""
from math import sqrt

num = int(input("请输入一个正整数："))
end = int(sqrt(num))

is_prime = True
for x in range(2, end+1):
    if num % x == 0:
        is_prime = False
        break;

if is_prime and num != 1:
    print("输入的 %d 是素数" % num)
else:
    print("输入的 %d 不是素数" % num)

