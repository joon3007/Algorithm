num = int(input())
loops = []
max = 0
for i in range(num):
    loops.append(int(input()))

loops.sort(reverse=True)

for i in range(len(loops)):
    if(loops[i]*(i+1) >= max):
        max = loops[i]*(i+1)

print(max)