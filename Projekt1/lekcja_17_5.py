def fibonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


n = 8
print(f"Element {n} ciągu Fibonacciego: {fibonacci(n)}")


def fibo(l1, l2, curn, n):
    if curn < n:
        sum = l1 + l2
        print(sum)
        fibo(l2, sum, curn + 1, n)


fibo(0, 1, 10, 19)

print("="*50)
def ciag_fibo(n):
    if n <= 1:
        return n
    return ciag_fibo(n - 1) + ciag_fibo(n - 2)


for i in range(10):
    ciag_fibo(i)
    print(ciag_fibo(i))
