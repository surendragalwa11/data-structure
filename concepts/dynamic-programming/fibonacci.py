# normal recursion solution
def recursiveFb(n):
    if n<=1:
        return n
    else:
        return recursiveFb(n-1) + recursiveFb(n-2)

# dynamic programming approach, memorization
def dpFibonacci(n):
    f = {}
    f[0] = 0
    f[1] = 1
    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]

def main():
    nthFib = recursiveFb(5)
    print(nthFib)
    nthFib = dpFibonacci(6)
    print(nthFib)


if __name__ == '__main__':
    main()