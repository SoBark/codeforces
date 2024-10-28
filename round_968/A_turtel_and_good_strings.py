t = int(input())

for _ in range(t):

    n = int(input())
    s = input()
    if s[0] == s[n-1]:
        print("NO")
    else:
        print("YES")