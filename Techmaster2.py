print(" "*10 + "Multiplication Table")
print(" "*2, end="")
for i in range(1, 10):
    print("%5d" % i, end="")
print("\n", "-"*46)
for i in range(1, 10):
    print("%d|" % i, end="")
    for j in range(1, 10):
        print("%5d" % (i*j), end="")
    print()
