t = int(input())

for _ in range(t):

    n, k = map(int, input().split())
    pie = sorted(map(int, input().split()))
    res = 0
    i = 0
    if k == 1:
        print(0)
        continue
    while i < k - 1 and pie[i] == 1:
        res +=1
        i+=1
    for k in range(i, k-1):
        res += 2*pie[k] - 1
    print(res)
