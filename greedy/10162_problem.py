import sys
input = sys.stdin.readline
btn = [0,0,0]
num = int(input())
if(num % 10 != 0):
    print(-1)
else:
    if(num // 300 > 0):
        btn[0] = num // 300
        num = num % 300


    if(num // 60 > 0):
        btn[1] = num // 60
        num = num % 60

    btn[2] = num // 10

    for i in btn:
        print(i, end=" ")