def f(a, b):
    if a == 0:
        return b
    if a > 0:
        return f(a // 10, 10 * b + (a % 10))


for a in range(1, 1000000000000):
    try:
        r = f(a, 0)
    except:
        pass
    else:
        print(a, r)
        if r > 1248163264:
            break
