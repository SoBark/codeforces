t = int(input())



for _ in range(t):

    n = int(input())
    abc = [None, None, None]
    abc[0] = list(map(int, input().split()))
    abc[1] = list(map(int, input().split()))
    abc[2] = list(map(int, input().split()))
    sum_abc = [0, 0, 0]
    tot = sum(abc[0])
    tot_d3 = tot // 3 + (tot % 3 > 0)
    rem_abc = [tot, tot, tot]
    lr = [[1, 1], [1, 1], [1, 1]]
    i = 0
    participants = [0, 1, 2]
    while i < n and len(participants) > 1:
        flag = False
        for p in participants:
            sum_abc[p] += abc[p][i]
            rem_abc[p] -= abc[p][i]
            flag += sum_abc[p] >= tot_d3
        if flag:
            x = sorted(range(3), key=lambda k: rem_abc[k])[0]
            lr[x][1] = i+1
            participants.remove(x)
            for j in participants:
                lr[j][0] = i+2
                sum_abc[j] = 0
        i += 1
    if len(participants) > 1:
        print(-1) 
        continue
    if len(participants) == 1:
        sum_abc[participants[0]] += sum(abc[participants[0]][i:])
        lr[participants[0]][1] = n
    
    if False in map(lambda x: x >= tot_d3, sum_abc):
        print(-1)
    else:
        print(f"{lr[0][0]} {lr[0][1]} {lr[1][0]} {lr[1][1]} {lr[2][0]} {lr[2][1]}")

