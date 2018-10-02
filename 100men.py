n = int(input())
m = int(input()
t = m-1
a = list(range(1, n+1))
while len(a)>m:
    if (t >= len(a)):
        for i in range(len(a)-1):
            if a[i] == 0:
                del a[i]
        t = 0
    print(a[t])
    a[t] = 0
    t = t+ m-1
    print(a)
