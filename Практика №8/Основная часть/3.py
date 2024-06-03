import matplotlib.pyplot as plt

x = [n for n in range(1, 11)]
y = [n for n in range(11, 1, -1)]
words = [
    'red', 'blue', 'yellow', 'green', 'purple',
    'orange', 'pink', 'brown', 'black', 'white'
]

plt.figure(figsize=(10, 6))
plt.plot(x, y, marker='o')
plt.title('Linear Plot')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.bar(words, x)
plt.title('Bar Chart')
plt.xlabel('List 3')
plt.ylabel('List 1')
plt.show()

plt.figure(figsize=(10, 6))
plt.pie(y, labels=words, autopct='%1.1f%%')
plt.title('Pie Chart')
plt.show()
