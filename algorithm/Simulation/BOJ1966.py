import sys
sys.stdin = open("../input.txt", 'r')


from collections import deque


def printer_queue(priority, target):
    ans = 0
    priority_counts = [priority.count(x) for x in range(10)]  # 우선순위 카운트 (인쇄 해야할지 말아야 할지 결정할 때 사용)
    priority = list(map(lambda x: [int(x), 0], priority))  # 타겟인지 아닌지 구분하기 위해
    priority[target][1] = 1  # 타겟이면 1로 바꿈
    q = deque(priority)  # popleft() 를 사용하기 위해 사용
    print_doc = 0  # 타겟이 인쇄 되었는지 확인
    while not print_doc:  # 타겟이 인쇄되지 않을때 계속 반복
        temp = q.popleft()  # 인쇄 할지 말지 임시 변수
        for i in range(temp[0] + 1, 10):  # 임시 변수의 우선순위보다 높은게 있는지 검사
            if priority_counts[i]:  # 높은게 있다면
                q.append(temp)  # 해당 문서를 뒤에다 붙이고
                break  # 탐색 종료
        else:  # 없다면
            priority_counts[temp[0]] -= 1  # 해당문서의 우선순위 카운트 하나 줄이고
            print_doc = temp[1]  # 문서를 인쇄 한뒤
            ans += 1  # 몇번째 인지 추가
    return ans


for tc in range(int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    print(printer_queue(arr, m))