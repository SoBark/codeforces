t = int(input())

for _ in range(t):

    x, y, k = map(int, input().split())
    x += 1
    d, m = divmod(x,y)
    while m == 0:
        x = d
        d, m = divmod(x, y)
    k -= 1
    while k > 0:
        if x <= y:
            # if y == 2:
            #     x = 1
            #     break
            k0 = k
            k0 -= y - x
            if k0 >= 0:
                d, m = divmod(k0,y-1)
                x = 1 + m
            else:
                x += k
            break
        d, m = divmod(x, y)
        y_m = y - m
        if k < y_m:
            x += k
        else:
            x += y_m
        k -= y_m
        d, m = divmod(x,y)
        while m == 0:
            x = d
            d, m = divmod(x, y)
    print(x)
    