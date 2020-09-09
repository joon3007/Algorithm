num = int(input())
cnt = [0 for i in range(26)]
for i in range(num):
    word = input()
    leng = len(word)
    for j in range(leng):
        cnt[ord(word[j])-65] += 10**(leng-(j+1))

cnt.sort(reverse=True)
sum = 0
for i in range(len(cnt)):
    sum += (9-i)*cnt[i]

print(sum)
