n,m = map(int,input().split())
matrix = []
cnt = 0
for _ in range(2):
    temp = []
    for _ in range(n):
        temp.append([int(i) for i in input()])
    matrix.append(temp)

def flip(x,y):
    for i in range(x,x+3):
        for j in range(y,y+3):
            matrix[0][i][j] = (matrix[0][i][j]+1)%2

for i in range(n-2):
    for j in range(m-2):
        if(matrix[0][i][j] != matrix[1][i][j]):
            flip(i,j)
            cnt += 1

if(matrix[0] == matrix[1]):
    print(cnt)
else:
    print(-1)
