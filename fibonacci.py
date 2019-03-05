def fibonacci(i):

    if (i==0): return 0
    if (i==1): return 1

    return fibonacci(i-1) + fibonacci(i-2)

def fibonacciDynamic(n):
    #bottom up dynamic
    if n==0:
        return 0
    memo = [0] * (n)
    memo[0] = 0
    memo[1] = 1

    for i in range(2, n):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n-1] + memo[n-2]
print(fibonacciDynamic(30))
