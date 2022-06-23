n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

i = int(input("Number: "))

print(n)

while len(n) > 1:
    if i >= n[len(n)//2]:
        n = n[len(n)//2:]
    elif i <= n[len(n)//2]:
        n = n[:len(n)//2]
    print(n)
