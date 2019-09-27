
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a

def main():
    for val in fib(20):
        print(val)

# 常见递归
def dfs_fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return dfs_fib(n-1) + dfs_fib(n-2)



if __name__ == '__main__':
    # main()
    print(dfs_fib(20))