
# dynamic programming tabulation method(bottom-top)
def factorialTabulationDP(n):
    f = {}
    f[0] = 1
    for i in range(1, n+1):
        f[i] = f[i-1]*i
    return f[n]

# dynamic programming tabulation method(top-bottom)
def memorizationDP(n):
    dp = {}
    if n == 0:
        return 1
    if n in dp:
        return dp[n]
    else:
        dp[n] = n*memorizationDP(n-1)
        return dp[n]

def main():
    nFact = factorialTabulationDP(5)
    print(nFact)
    nFact = memorizationDP(5)
    print(nFact)


if __name__ == '__main__':
    main()