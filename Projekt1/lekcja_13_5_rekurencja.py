# silnia
# 5! = 5 * 4 * 3 * 2 * 1 = 120
# n! = n * n-1 * n-2 ... * 1

def slina(n):
    if n <= 1:
        return 1
    return n * slina(n-1)

# def slina(5):
#     if 5 <= 1:
#         return 1
#     return 5 * slina(5-1)

# def slina(4):
#     if 4 <= 1:
#         return 1
#     return 4 * slina(4-1)

# def slina(3):
#     if 3 <= 1:
#         return 1
#     return 3 * slina(3-1)

# def slina(2):
#     if 2 <= 1:
#         return 1
#     return 2 * slina(2-1)

# def slina(1):
#     if 1 <= 1:
#         return 1
#     return n * slina(n-1)

print(slina())