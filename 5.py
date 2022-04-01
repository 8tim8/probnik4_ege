for n in range(10, 900):
    s = str(n)
    a = [int(s[i - 1] + s[i]) for i in range(1, len(s))]
    if max(a) + min(a) == 137:
        print(n)
        break
