f = open('26.txt')
n = int(f.readline())
a = []
for i in range(n):
    ryd, mesto = [int(x) for x in f.readline().split()]
    a.append([ryd, mesto])
a.sort()
c = 0
max_len = -1
otv_ryd = -1
for i in range(1, len(a)):
    if a[i] == a[i - 1]:
        continue
    if a[i][0] == a[i - 1][0]:
        if a[i][1] % 2 == 0:
            c += 1
            if c > max_len:
                max_len = c
                otv_ryd = a[i][0]
    else:
        if mesto % 2 == 0:
            c = 1
        else:
            c = 0
print(max_len, otv_ryd)
