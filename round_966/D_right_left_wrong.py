

def rlw(nums, lrs):

    for i, ch in enumerate(lrs):
        if ch == 'L':
            break
    for j, ch in enumerate(reversed(lrs)):
        if ch == 'R':
            break
    j = len(lrs) - j
    res = sum(nums[i:j])
    if i+1 < j-1:
        res += rlw(nums[i+1:j-1], lrs[i+1:j-1])
    return res


t = int(input())


for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    lrs = input()
    print(rlw(nums, lrs)) 

