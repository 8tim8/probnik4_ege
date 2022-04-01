f = open('17.txt')
a = [int(x) for x in f]
m = 10000000000
for i in a:
    if i % 2 != 0:
        m = min(i, m)
m_max = -10000000000
k = 0
for i in range(1, len(a)):
    x = a[i - 1]
    y = a[i]
    if (x % 3 == 0 and y % 3 != 0) or (x % 3 != 0 and y % 3 == 0):
        if abs(x - y) < m:
            k += 1
            m_max = max(m_max, abs(x - y))
print(k, m_max)
