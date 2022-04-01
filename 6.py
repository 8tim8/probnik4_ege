k = 0
for s in range(7, 1000000):
    x = s
    s //= 7
    n = 1
    while s < 255:
        s += n
        n += 1
    if n == 7:
        k += 1
print(k)
