# Python



### Type Hint

> 말 그대로 힌트 일뿐 여전히 동적할당 됨을 주의

```python
# a의 자료형은 문자열이고 "1"을 할당하겠다는 의미
# b의 자료형은 인티저이고 1을 할당한다는 의미 => 두경우 모두 여전히 동적할당
a: str = "1"
b: int = 1
    
# a 라는 파라미터는 인티저가 와야하며 return 값으로 bool이 온다는 의미
def fn(a:int) -> bool:
`````
```



### List Comprehension

​```python
[n*2 for n in range(1,11) if n % 2 == 1]
# 1 이상 11 미만 정수에 대해 n 을 2로 나눈 나머지가 1 이면 n에 2를 곱한다

# 딕셔너리도 Comporehension 가능
a = {key:value for key, value in original.items()}
```



### Generator

> 루프의 반복 동작을 제어할 수 있는 루틴 형태

```python
def get_natural_number(n: int):
    num = 0
    while num != n:
        num += 1
        yield num # return과 달리 종료되지 않고 값을 내보내고(양보하고) 함수가 계속 진행
        yield num * 2

gen = get_natural_number(10)
print(gen)
# <generator object get_natural_number at 0x000001BBDDFC4BF8>

for _ in range(10):
    print(next(gen), end="의 제곱은 ")
    print(next(gen))
    
# 1의 제곱은1
# 2의 제곱은4
# 3의 제곱은9
# 4의 제곱은16
# 5의 제곱은25
# 6의 제곱은36
# 7의 제곱은49
# 8의 제곱은64
# 9의 제곱은81
# 10의 제곱은100
```

- range

  > 대표적인 generator방식을 이용한 함수

  ```python
  a = range(1,100,2)
  print(type(a))
  >>> <class 'range'>
  print(len(a))
  >>> 50
  print(a[0])
  >>> 1
  print(sys.getsizeif(a))
  >>> 48
  # 리스트로 사용했을때와 메모리에서 큰 차이를 보임
  ```



### Enumerate

> 순서가 있는 자료형 (list, set, tuple 등) 을 인덱스를 포함한 enumerate 객체로 리턴

```python
lis = [1,2,3,4,5]
# enumerate 는 오브젝트를 반환
print(enumerate(lis))
>>> <enumerate object at 0x0000021FB00A92D0>

print(list(enumerate(lis)))
>>> [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]



sett = {6,7,8,9,10}
# enumerate 는 오브젝트를 반환
print(enumerate(sett))
>>> <enumerate object at 0x0000021FB00A92D0>

print(set(enumerate(sett)))
>>> {(4, 10), (2, 8), (0, 6), (3, 9), (1, 7)}





tup = (11,12,13,14,15)
# enumerate 는 오브젝트를 반환
print(enumerate(tup))
>>> <enumerate object at 0x0000021FB00A92D0>

print(tuple(enumerate(tup)))
>>> ((0, 11), (1, 12), (2, 13), (3, 14), (4, 15))
```



### print

> f 스트링을 활용하자!



### in 연산자의 시간복잡도

1. list, tuple => 순회하면서 확인 O(n)
2. dictionary, set => 내부적으로 hash를 사용하기 때문에 O(1)
   but, 해시가 성능이 떨어진 경우 O(n)