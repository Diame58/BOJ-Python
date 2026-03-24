S = int(input())
left = 1
right = S
while left <= right:
    mid = (left + right) // 2
    if mid * (mid + 1) // 2 <= S:
        left = mid + 1
    else:
        right = mid - 1
print(right)