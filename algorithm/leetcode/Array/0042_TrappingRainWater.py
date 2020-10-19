# leetcode 42
def trap(height) -> int:

    # my style 52ms 14.6MB
    left_p, right_p = 0, len(height) - 1
    answer = 0
    while left_p < right_p:
        left_temp = 0
        right_temp = 0
        for left in range(left_p+1,right_p + 1):
            if height[left_p] <= height[left]:
                answer += left_temp
                left_p = left
                break
            else:
                left_temp += height[left_p] - height[left]
        for right in range(right_p-1,left_p-1,-1):
            if height[right_p] <= height[right]:
                answer += right_temp
                right_p = right
                break
            else:
                right_temp += height[right_p] - height[right]
    print(answer)
    
    # use two pinter 52ms 14.5MB
    if not height:
        return 0
    volume = 0
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    
    while left < right:
        left_max, right_max = max(height[left], left_max), max(height[right], right_max)
        # 낮은 쪽에서 높은 쪽으로 포인터가 이동
        if left_max <= right_max:
            volume += left_max - height[left]
            left += 1
        else:
            volume += right_max -height[right]
            right -= 1
    print(volume)

    # use stack
    stack = []
    volume = 0
    for i in range(len(height)):
        # 변곡점을 만나면
        while stack and height[i] > height[stack[-1]]:
            top = stack.pop()
            if not len(stack):
                break
            distance = i - stack[-1] - 1
            waters = min(height[i], height[stack[-1]]) - height[top]

            volume += distance * waters
        stack.append(i)
    print(volume)

trap([0,1,0,2,1,0,1,3,2,1,2,1])