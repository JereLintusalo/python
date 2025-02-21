print("   X", end="")
for i in range(1, 11):
    print(f"{i:5}", end="")
print()

for i in range(1, 11):
    print(f"{i:4}", end=" ")
    for j in range(1, 11):
        print(f"{i * j:4}", end=" ")
    print()