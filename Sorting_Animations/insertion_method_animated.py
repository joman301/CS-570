import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib as mp
import numpy as np
import random

# Setting the graph style
plt.style.use('fivethirtyeight')

# Creates a list of randomized numbers n elements long
n = int(input("Enter array size: "))
min = 0
max = 100
a = []
for i in range(1,n):
	a.append(random.randint(min,max))
#random.shuffle(a)


# Insertion sort method
def insertionsort(a):
	for j in range(1, len(a)):
		key = a[j]
		i = j-1

		while(i >= 0 and a[i] > key):
			a[i+1] = a[i]
			i -= 1

			# yield the current position
			# of elements in a
			yield a
		a[i+1] = key
		yield a


# Insertion sort is a generator object because of the yield statments
generator = insertionsort(a)

# Setting the color of the bars with a custom color map
data_normalizer = mp.colors.Normalize()
color_map = mp.colors.LinearSegmentedColormap(
	"my_map",
	{
		"red": [(0, 1.0, 1.0),
				(1.0, .5, .5)],
		"green": [(0, 0.5, 0.5),
				(1.0, 0, 0)],
		"blue": [(0, 0.50, 0.5),
				(1.0, 0, 0)]
	}
)

# Creating the matplotlib figure
fig, ax = plt.subplots()

# Creating the bars for the figure
rects = ax.bar(range(len(a)), a, align="edge",
			color=color_map(data_normalizer(range(n))))

# Setting x and y view limits based off of maximum value bounds
ax.set_xlim(0, len(a))
ax.set_ylim(0, int(1.1*max))

# Creating the text object that displays the iteration count
text = ax.text(0.01, 0.95, "", transform=ax.transAxes)
iteration = [0]


# Animation function (called repeatedly)
def animate(A, rects, iteration):

	# Setting the size of each bar equal
	# to the value of the elements
	for rect, val in zip(rects, A):
		rect.set_height(val)

	iteration[0] += 1
	text.set_text("Iterations : {}".format(iteration[0]))


# Animation object that calls the animate function, as well as the bars/ text to be displayed
anim = FuncAnimation(fig, func=animate,
					fargs=(rects, iteration), frames=generator, interval=100,
					repeat=False)

plt.show()
