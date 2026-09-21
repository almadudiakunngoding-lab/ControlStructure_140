a = float(input("Angka 1: "))
b = float(input("Angka 2: "))
c = float(input("Angka 3: "))

if a >= b and a >= c:
    max_num = a
elif b >= a and b >= c:
    max_num = b
else:
    max_num = c

print("Terbesar:", max_num)