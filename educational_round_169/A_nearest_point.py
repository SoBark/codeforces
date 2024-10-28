t = int(input())

for _ in range(t):
    n = int(input())
    x = input()
    if n > 2:
        print("NO")
    else:
        x = list(map(int, x.split()))
        if abs(x[0] - x[1]) > 1:
            print("YES")
        else:
            print("NO")
