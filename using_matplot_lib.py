import matplotlib.pyplot as plt

x = [0, 1, 3, 5, 7, 9, 11, 13, 15]

y = [pow(xi, 2) for xi in x]

print(y)

plt.bar(x, y, color='green')
plt.title("Sample Line Plot")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid(True)
plt.show()