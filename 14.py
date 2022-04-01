a = 7 * 729**6 + 6 * 81**9 + 3**14 - 90
b = ''
while a > 0:
    b = str(a % 9) + b
    a //= 9
k = 0
for i in b:
    if int(i) % 2 == 0:
        k += 1
print(k)
