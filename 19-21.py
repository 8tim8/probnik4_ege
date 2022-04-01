def f(x, c, max_):
    if x >= 22:
        return c % 2 == max_ % 2
    if c == max_:
        return False

    p1 = f(x + 1, c + 1, max_)
    p2 = f(x + 2, c + 1, max_)
    p3 = f(x * 2, c + 1, max_)

    if c % 2 != max_ % 2:
        if x % 2 == 0:
            return p1 or p2
        else:
            return p1 or p2 or p3
    else:
        if x % 2 == 0:
            return p1 and p2
        else:
            return p1 and p2 and p3


for s in range(1, 22):
    for j in range(1, 6):
        if f(s, 0, j):
            if j == 3:  # ставим нужное кол-во ходов
                print(s, j)
            break

