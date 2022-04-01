from itertools import *

s = 'НАСТЯ'
k = 0
comb = product(s, repeat=7)
for i in comb:
    s = ''.join(i)
    if s.count('Н') == 2 and s.count('А') >= 1:
        k += 1
print(k)
