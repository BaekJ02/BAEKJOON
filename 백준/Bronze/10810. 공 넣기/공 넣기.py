n, m = map(int, input().split())
x = []
for i in range(n):
    x.append(0)

for j in range(m):
    a, b, c = map(int, input().split())
    for k in range(a, b+1):
        x[k-1]= c
    

print(*x)

