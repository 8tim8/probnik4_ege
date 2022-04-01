d = [[0] * 50 for i in range(50)]
d[0][1] = 1
for j in range(11):
    for i in range(3):
        d[i][j + 1] += d[i][j]
        d[i + 1][j * 2] += d[i][j]
print(d[0][11] + d[1][11] + d[2][11])
