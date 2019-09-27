"""
@Desc: 将8个苹果分成四组每组至少一个苹果有多少种方案  C 7 取 3 ，插入三个空格，将分成四组
@Author: lirong
@Date: 2019-9-24 17:42:21
"""
def factorial(num):
    result = 1
    for n in range(1, num + 1):
        result *= n
    return result

m = int(input('m = '))
n = int(input('n = '))
print(factorial(m) // factorial(n) // factorial(m - n))
