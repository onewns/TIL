### 언제 끝날지 모르는 인풋

- BOJ1694
  - ```python
    while True:
        try:
            data = input()
        except EOFError:
            break
```