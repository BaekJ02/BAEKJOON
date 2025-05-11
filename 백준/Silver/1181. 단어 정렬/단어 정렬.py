N = int(input())
a = []
for i in range(N):
    word = input()
    a.append(word)
a_set = list(set(a))

result = []
tmp = []


max_a = max(a_set, key=len)
for i in range(len(max_a)+1):
    for j in range(len(a_set)):
        if len(a_set[j]) == i:
            tmp.append(a_set[j])
    for i in range(i):
        tmp.sort(key=lambda x: x)
    result += tmp
    tmp = []

for i in result:
    print(i)