t = int(input())

for _ in range(t):

    n = input()
    if len(n) >= 3 and n[:2] == "10":
        if n[2:3] != "0" and int(n[2:]) >= 2:
            print("YES")
            continue
    print("NO")

