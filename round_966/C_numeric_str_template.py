t = int(input())


for _ in range(t):

    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    for _ in range(m):
        s = input()
        if len(s) != n:
            print("NO")
            continue
        a_map = {}
        s_map = {}
        flag = True
        for num, ch in zip(a, s):
            if num in a_map:
                if a_map[num] != ch:
                    print("NO")
                    flag = False
                    break
            else:
                a_map[num] = ch
            if ch in s_map:
                if s_map[ch] != num:
                    print("NO")
                    flag = False
                    break
            else:
                s_map[ch] = num
        if flag:
            print("YES")
