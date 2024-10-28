t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = sorted(map(int, input().split()), reverse=True)
    i = 0
    A, B = 0, 0
    while(k > 0 and n-i >= 2):
        A+=a[i]
        tmp = a[i]-a[i+1]
        if tmp > k:
            tmp = k
        k -= tmp
        a[i+1] += tmp 
        B+=a[i+1]
        i +=2
    while n-i >= 2:
        A+=a[i]
        B+=a[i+1]
        i +=2
    if i < n:
        A+=a[i]
    print(A-B)