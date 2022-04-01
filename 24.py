f = open('24.txt')
s = f.readline()
ans = [st for st in s.split('A') if len(st) >= 10 and st.count('B') >= 2]
print(len(ans))
print(s[0], s[-1])
print(s.split('A')[0])
print(s.split('A')[-1])

