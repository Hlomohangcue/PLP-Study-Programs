# Write a python function that checks if a number is even or odd and prints the
# result. Here's a start:

def check_even_odd(number):
    if number % 2 == 0:
        print(f"{number} is even!")
    else:
        print(f"{number} is odd!")

# take input from user
user_input = int(input("Enter a number: "))
print(check_even_odd(user_input))