import io, os
# input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline


t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    
    s = list(input())
    ind = sorted(list(map(int, input().split())))
    c = sorted(list(input()))
    j = 0
    i = 0
    while i < m:
        s[ind[i]-1] = c[j]
        while i+1 < m and ind[i] == ind[i+1]:
            i += 1
        j +=1
        i +=1
    print("".join(s))


    