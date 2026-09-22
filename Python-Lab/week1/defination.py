# Function to calculate square
def find_sqr(n):
    return n * n

# Function to check if a number is even or odd
def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Get user input
num_str = input("Enter a number: ")

# Convert input to integer once to avoid repeating int()
num = int(num_str)

# Call the functions
square = find_sqr(num)
result = check_even_odd(num)

# Print the final outputs
print(f"The square of {num} is {square}")
print(f"The number {num} is {result}")
