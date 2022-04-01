z = []
for x in range(1, 100000):
    a = 1
    b = 0
    while x > 0:
        d = x % 10
        a *= d
        if d > 5:
            b += d
        x //= 10
    if a == 6300:
        z.append(b)
print(max(z))
