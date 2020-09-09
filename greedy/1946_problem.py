import sys
input = sys.stdin.readline

num = int(input())
case = []
for i in range(num):
    n = int(input())
    temp = []
    for j in range(n):
        temp.append(list(map(int, input().split())))
    case.append(sorted(temp,key=lambda x : x[0]))

for i in case:
    cnt = 1
    min = i[0][1]
    for j in range(1,len(i)):
        if(i[j][1] < min):
            cnt += 1
            min = i[j][1]
    print(cnt)