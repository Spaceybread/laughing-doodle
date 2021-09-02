import matplotlib.pyplot as plt
tn = input('N max: ')
n = 1
x = []
y = []

while n < int(tn):
    x.append(n)
    s = 0
    while n != 1:
        if n % 2 == 1:
            n = (3 * n) + 1
        else:
            n = n / 2
        s = s + 1
    print(s)
    y.append(s)
    pick = len(x) - 1
    n = x[pick] + 1

plt.scatter(x, y)
plt.show()
