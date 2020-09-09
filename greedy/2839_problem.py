weight = int(input())
num = 0

for i in range(weight // 5, 0, -1):
    if( (weight-(i*5)) %3 == 0):
        num = i + ((weight-(i*5)) // 3)
        break

if(num == 0):
    if(weight %3 == 0):
        num = weight // 3
    else: num = -1

print(num)