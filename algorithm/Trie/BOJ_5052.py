import sys
sys.stdin = open('../input.txt', 'r')


for tc in range(int(input())):  # tc
    trie = {}  # dictionary 로 구현할 trie
    flag = False  # 중첩된 for문을 빠져나올 표시
    strings = [input() for _ in range(int(input()))]  # 트라이를 구성할 문자열들
    strings.sort(key= lambda x: len(x))  # 문제에서 길이가 중요하므로 일단 sort
    for string in strings:  # 문자열들로 trie를 만들기 시작
        cur = trie  # 현재 위치 표시
        for char in string:  # 문자열에서 각각의 문자들에 대해
            if char in cur:  # trie에 있으면
                cur = cur[char]  # 다음 노드로 넘어감
                if '#' in cur:  # 이미 구성된 trie가 끝날경우 더이상 진행 불가
                    print('NO')  # NO 출력후
                    flag = True  # 더이상 진행 필요 x 표시
                    break
            else:
                cur[char] = {}  # trie에 없으면
                cur = cur[char]  # 새로운 노드를 생성
        cur['#'] = '#'  # 문자열이 끝남을 표시
        if flag:
            break
    else:  # 모든 조건에 통과 되면
        print('YES')  # YES 표시
