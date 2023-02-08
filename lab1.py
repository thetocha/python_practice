x = float(input("Enter x \n"))
while x < -1 or x >= 1:
    print("x should be in range of -1 including to 1 not including")
    x = float(input("Enter x again \n"))

k = int(input("Enter natural k \n"))
while k <= 1:
    print("k should be bigger than 1")
    k = float(input("Enter k again \n"))

accuracy = pow(10, -k)

term = 1.0
sum = 0.0
i = 1
while term >= accuracy:
    term = pow(x, i)
    term /= i
    sum -= term
    i += 1

print(sum)