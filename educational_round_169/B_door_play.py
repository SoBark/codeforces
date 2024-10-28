t = int(input())

for _ in range(t):

    l, r = map(int, input().split())
    L, R = map(int, input().split())
    res = 1
    if r < L or R < l:
        # print(1)
        pass
    else:
        res = (min(r, R) - max(L, l))
        if R != r:
            res +=1
        if L != l:
            res +=1
    print(res)