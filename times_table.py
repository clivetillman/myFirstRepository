print("=" * 40)
print("{:^40}".format("Multiplication Table"))
print("=" * 40)

for i in range(1,11):
    for j in range(1, 11):
        print("{:^4}".format(i * j), end="")
    print()