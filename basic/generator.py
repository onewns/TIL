import sys

def get_natural_number(n: int):
    num = 0
    while num != n:
        num += 1
        yield num
        yield num ** 2

gen = get_natural_number(10)
print(gen)
for _ in range(10):
    print(next(gen), end="의 제곱은 ")
    print(next(gen))

b = range(1,10000000000,2)
print(type(b))
print(len(b))
print(b[0])
print(sys.getsizeof(b))