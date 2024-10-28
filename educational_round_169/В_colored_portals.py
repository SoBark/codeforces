t = int(input())

for _ in range(t):

    n, q = map(int, input().split())
    cities = input().split()
    matrix = [[0]*n for j in range(n)]
    for i in range(n):
        for j in range(n):
            if cities[i][0] in cities[j] or cities[i][1] in cities[j]:
                matrix[i][j] = abs(i-j)

    for i in range(q):
        x, y = map(int, input().split())
        