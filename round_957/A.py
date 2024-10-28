t = int(input())

for _ in range(t):
    abc = sorted(map(int, input().split()))
    tmp = abc[1] - abc[0]
    if tmp > 5:
        abc[0] += 5
    elif tmp <= 5:
        abc[0] += tmp
        tmp2 = 5 - tmp
        tmp = abc[2] - abc[1]
        if tmp >= tmp2:
            abc[1] += tmp2
        elif tmp <= tmp2:
            abc[1] += tmp
            tmp2 = tmp2 - tmp 
            abc[0] += tmp2 // 3 + ((tmp2 % 3) // 2) + ((tmp2 % 3) % 2)
            abc[1] += tmp2 // 3 + ((tmp2 % 3) // 2)
            abc[2] += tmp2 // 3


    print(abc[0]*abc[1]*abc[2])