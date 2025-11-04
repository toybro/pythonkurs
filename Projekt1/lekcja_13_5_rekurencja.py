#silnia
# 5! = 5*4*3*2*1* = 120
# n! = n * n-1 * n-2 ... * 1


def silnia(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return n * silnia(n - 1)

print(silnia(5))
