start = 7000000

for k in range(1, 60):
    x = start + k
    st = set()
    d = [0] * (x + 1)
    while x != 1:
        for j in range(2, x + 1):
            if j >= x - 1:
                st.add(x)
                d[x] += 1
                x = 1
                break

            if x % j == 0:
                st.add(j)
                d[j] += 1
                x //= j
                break
    if len(st) == 2:
        if d[list(st)[0]] <= 2 and d[list(st)[1]] <= 2:
            print(start + k, st)

    if len(st) == 1:
        if d[list(st)[0]] < 6:
            print(start + k, st)
