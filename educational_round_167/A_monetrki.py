

t = int(input())

for _ in range(t):

    x, y = map(int, input().split())
    if y < -1:
        print("NO")
    else:
        print("YES")
        