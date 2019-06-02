# input so lieu
so_thu1 = int(input("Nhap so thu 1: "))
so_thu2 = int(input("Nhap so thu 2: "))

a = so_thu1 % so_thu2
while a != 0:
    so_thu1 = so_thu2
    so_thu2 = a
    a = so_thu1 % so_thu2
print(so_thu2)
print("abc")
print("crgrafsg")
print("from feature-1")
print("from feature-2")