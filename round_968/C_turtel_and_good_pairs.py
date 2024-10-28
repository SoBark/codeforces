t = int(input())

for _ in range(t):

    n = int(input())
    s = sorted(input())
    i = 0
    while i < n-1:
        while i < n-1 and s[i]==s[i+1]:
            i+=1
        s[i], s[i+1*(i < n-1)] = s[i+1*(i < n-1)], s[i]
        i+=1
    print("".join(s))