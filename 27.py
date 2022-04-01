f = open('27-B.txt')
n = int(f.readline())
k = [0] * 999
count = 0
s = 0
queue = [0]
for i in range(1, 101):
    x = int(f.readline())
    s += x
    queue.append(s)
for i in range(101, n + 1):
    y = queue.pop(0)
    k[y % 999] += 1
    x = int(f.readline())
    s += x
    count += k[s % 999]
    queue.append(s)
print(count)
