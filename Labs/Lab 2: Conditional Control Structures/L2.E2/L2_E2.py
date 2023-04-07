# ask user to input date as three integers
y, m, d = input().split()

# convert inputs to integers
y, m, d = int(y), int(m), int(d)

# adjust month and year values as necessary
if m < 3:
    m += 12
    y -= 1

# calculate a, b, f1, and f values
a = (2 * m) + (6 * (m + 1) // 10)
b = y + (y // 4) - (y // 100) + (y // 400)
f1 = d + a + b + 1
f = f1 % 7

# output the corresponding day of the week
print(f)


