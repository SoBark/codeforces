import io, os
# input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline


n = int(input())

points = [list(map(int, input().split())) for _ in range(n)]

ans = []
for group in points:
    x = sorted(group)
    ans.append(str(x[2]-x[0]))
    # if x[0] == x[1]:
    #     ans.append(str(x[1]))
    # elif x[1] == x[2]:
    #     ans.append(str(x[1]))

print("\n".join(ans))