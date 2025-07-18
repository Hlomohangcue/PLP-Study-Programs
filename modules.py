# Modules - Python's Toolkit!
""" Python comes with a toolkit of modules -- specialized code libraries that
you can use without building everything from scratch. It's like using a toolbox
instead of crafting tools by hand!

To use a module, just import it:

Example 1: Math Module: For mathematical functions.
"""
import math

# Using the math module to calculate the square root
print(math.sqrt(16))

# Example 2: Random Module: For generating random numbers:

import random

# Generate a random number between 1 and 6 (like rolling a dice)
for roll in range(5):
    dice_roll = random.randint(1, 6)
    print("You rolled a:", dice_roll)

