import io, os
# input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline


t = int(input())
nm = []
matrixes = []
for _ in range(t):
    n, m = map(int,input().split())
    nm.append([n,m])
    mat = [list(map(int, input().split())) for _ in range(n)]
    matrixes.append(mat)


# ans = []

def stabilize(mat, n, m):
    neighbours = [0]*4
    if n > 1 or m > 1:
        for i in range(n):

            for j in range(m):
                n_c = 0

                if j > 0:
                    neighbours[n_c] = mat[i][j-1]
                    n_c += 1
                if j < m-1:
                    neighbours[n_c] = mat[i][j+1]
                    n_c+=1
                if i > 0:
                    neighbours[n_c] = mat[i-1][j]
                    n_c += 1
                if i < n-1:
                    neighbours[n_c] = mat[i+1][j]
                    n_c+=1
                x = max(neighbours[:n_c])
                if mat[i][j] > x:
                    mat[i][j] = x
    for i in range(n):
        print(" ".join(map(str,mat[i])))


for (n, m), mat in zip(nm, matrixes):

    stabilize(mat, n, m)