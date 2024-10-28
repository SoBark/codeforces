t = int(input())

for _ in range(t):
    n = int(input())
    a = map(int, input().split())
    b = map(int, input().split())
    a_score = 0
    b_score = 0
    plus = 0
    minus = 0
    for ai, bi in zip(a, b):
        if ai == 1:
            if bi == 1:
                plus += 1
            else:
                a_score += 1
        else:
            if bi == 1:
                b_score += 1
            elif ai == 0 or bi == 0:
                continue
            else:
                minus += 1
    min_score, max_score = sorted([a_score, b_score])
    dif_score = max_score - min_score
    if plus >= minus:
        p_m = plus - minus
        if dif_score > p_m:
            ans = min_score + p_m
        else:
            ans = min_score + dif_score + (p_m - dif_score) // 2
    else:
        p_m = plus - minus
        if dif_score >= abs(p_m):
            ans = min_score
        else:
            ans = max_score - dif_score + (p_m + dif_score) // 2

    print("s", ans)
