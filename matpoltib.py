import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.plot(x, y)
plt.xlabel("X-axis Label")
plt.ylabel("Y-axis Label")
plt.title("Line Plot Example")
plt.show()  # Display the plot

plt.subplot(1, 2, 1)  # 1 row, 2 columns, first subplot
plt.plot(x, y)

plt.subplot(1, 2, 2)  # 1 row, 2 columns, second subplot
plt.bar(categories, values)

plt.show()