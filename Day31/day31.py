import matplotlib.pyplot as plt

#Task 2

#Plot two lines, Add labels, Add legend
x = [1, 2, 3, 4]
y1 = [10, 20, 30, 40]
y2 = [40, 30, 20, 10]

plt.plot(x, y1, label="Sales")
plt.plot(x, y2, label="Profit")

plt.legend()
plt.show()


#Task 3

#Change figure size, Add title, Add grid
x = [1, 2, 3, 4]
y = [10, 20, 30, 40]

plt.figure(figsize=(8, 5))
plt.plot(x, y, marker='o', linestyle='--')

plt.title("Customized Graph")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.grid()
plt.show()


#Task 4

#1. Create 2 subplots
x = [1, 2, 3, 4]
y1 = [10, 20, 30, 40]
y2 = [40, 30, 20, 10]

plt.subplot(1, 2, 1)
plt.plot(x, y1)
plt.title("Graph 1")

plt.subplot(1, 2, 2)
plt.plot(x, y2)
plt.title("Graph 2")

plt.show()

#2. Create 4 subplots
x = [1, 2, 3]
y1 = [1, 4, 9]
y2 = [2, 5, 8]
y3 = [3, 6, 9]
y4 = [4, 7, 10]

plt.subplot(2, 2, 1)
plt.plot(x, y1)
plt.title("Graph 1")

plt.subplot(2, 2, 2)
plt.plot(x, y2)
plt.title("Graph 2")

plt.subplot(2, 2, 3)
plt.plot(x, y3)
plt.title("Graph 3")

plt.subplot(2, 2, 4)
plt.plot(x, y4)
plt.title("Graph 4")

plt.tight_layout()
plt.show()


#Task 5

#Create histogram, Analyze distribution, Use random dataset
import numpy as np
data = np.random.randint(1, 100, 50)

plt.hist(data)
plt.title("Histogram")
plt.xlabel("Values")
plt.ylabel("Frequency")

plt.show()


#Task 6

#1. Save Line Graph
plt.plot([1,2,3,4], [10,20,30,40])
plt.savefig("line_graph.png")

#2. Save Histogram
plt.hist(data)
plt.savefig("histogram.png")

#3. Save Subplot Figure
plt.subplot(1,2,1)
plt.plot([1,2,3], [1,4,9])

plt.subplot(1,2,2)
plt.plot([1,2,3], [2,5,8])
plt.savefig("subplots.png")