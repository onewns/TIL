import sys
sys.stdin = open('../input.txt', 'r')


words = input().split()
space = int(input())
limit = {chr(97 + i): int(num) for i, num in enumerate(input().split())}
if space < len(words) - 1:
    print(-1)
else:
    ans = ''
    for word in words:
        possible = True
        limit[word[0].lower()] -= 2
        ans += word[0].upper()
        for char_idx in range(1, len(word)):
            if word[char_idx] != word[char_idx - 1]:
                limit[word[char_idx].lower()] -= 1
        for char in word:
            if limit[char.lower()] < 0:
                possible = False
                break
        if not possible:
            print(-1)
            break
    else:
        print(ans)
