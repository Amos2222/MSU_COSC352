import sys

# Check if there are exactly two arguments passed
if len(sys.argv) != 3:
    print("Usage: python hello.py <name> <number>")
    sys.exit(1)

# Extract arguments
name = sys.argv[1]
try:
    number = int(sys.argv[2])  # Convert the second argument to an integer
except ValueError:
    print("The second argument must be an integer.")
    sys.exit(1)

# Print the greeting the specified number of times
for _ in range(number):
    print(f"Hello {name}")   
 
