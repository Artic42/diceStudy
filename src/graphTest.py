import articlib.dice as Dice
import matplotlib.pyplot as plt

rollQuantity = 10000000

dice1 = Dice.dice()
rolls = []
for i in range(rollQuantity):
    rolls.append(dice1.roll())

one = rolls.count(1) / rollQuantity
two = rolls.count(2) / rollQuantity
three = rolls.count(3) / rollQuantity
four = rolls.count(4) / rollQuantity
five = rolls.count(5) / rollQuantity
six = rolls.count(6) / rollQuantity

one = round(one, 3)
two = round(two, 3)
three = round(three, 3)
four = round(four, 3)
five = round(five, 3)
six = round(six, 3)

y = [one, two, three, four, five, six]
x = [1, 2, 3, 4, 5, 6]

# Create the plot
plt.plot(x, y, marker='o', linestyle='-', color='b', label='Line 1')

# Add titles and labels
plt.title('Simple Line Graph')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()

# Save the plot as a JPEG file
plt.savefig('plot.jpg', format='jpeg')
