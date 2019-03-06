def tripleStep(n):
    if n == 0:
         return 0
    if n == 1:
         return 1
    if n == 2:
         return 2
    if n == 3:
        return 4
    # base case covered.
    # Initialize
    result = [0] * (n+1)
    result[1] = 1
    result[2] = 2
    result[3] = 4

    for i in range(4, n+1):
        result[i] = result[i-1] + result[i-2] + result[i-3]
    return result[i]


print (tripleStep(5))