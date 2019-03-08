def recursiveMultiply(a, b):
    if a>b:
        bigger = a
        smaller = b
    else:
        bigger = b
        smaller = a
    return _recursiveMultiply(smaller, bigger)
class cal:
    cnt =0
def _recursiveMultiply(smaller, bigger):

    if smaller ==0 :
        return 0
    if smaller == 1:
        return bigger
    s = smaller >> 1
    cal.cnt+=1

    halfProd = _recursiveMultiply(s, bigger)

    if smaller % 2 == 0:
        cal.cnt += 1
        return halfProd+halfProd
    else:
        cal.cnt += 2
        return halfProd+halfProd+bigger

recursiveMultiply(10,30)
print(cal.cnt)