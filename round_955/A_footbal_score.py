t = int(input())

def f(score_winer_before, score_other_after, score_winer_after):
    if score_other_after < score_winer_before or score_other_after < score_winer_after:
        print("YES")
    else:
        print("NO")

for _ in range(t):
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    if x1 > y1:
        f(x1, y2, x2)
    else:
        f(y1, x2, y2)

