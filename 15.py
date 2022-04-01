for x in range(0, 100):
    f = ((18 <= x <= 52) == (6 <= x <= 45)) or (((6 <= x <= 45) and not(18 <= x <= 52)) <= 0)
    if f == False:
        print(x)

x = 5.5
f = ((18 <= x <= 52) == (6 <= x <= 45)) or (((6 <= x <= 45) and not(18 <= x <= 52)) <= 0)
print(f)

x = 17.5
f = ((18 <= x <= 52) == (6 <= x <= 45)) or (((6 <= x <= 45) and not(18 <= x <= 52)) <= 0)
print(f)
