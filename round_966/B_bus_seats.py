t = int(input())

for _ in range(t):
    n = int(input())
    a = map(int, input().split())
    b = [False] * n
    b[next(a)-1] = True
    flag = True
    for p in a:
        if sum(b[max(p-2, 0):p+1]) == 0:
            print("NO")
            flag = False
            break
        b[p-1] = True
    if flag:
        print("YES")
        
            