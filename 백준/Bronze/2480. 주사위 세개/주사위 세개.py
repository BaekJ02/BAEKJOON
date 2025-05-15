x = list(map(int, input().split()))

x.sort()

if (x[0] == x[1] and x[0] == x[2]):
    print(10000 + x[0]*1000)
elif (x[0] == x[1] and x[1] != x[2]) or (x[1] == x[2] and x[0] != x[1]):
    print(1000+ x[1] * 100)
else:
    print(max(x) * 100)