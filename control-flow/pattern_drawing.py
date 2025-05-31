# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use a while loop for rows
while row < size:
    # Use a for loop to print asterisks in a row
    for col in range(size):
        print("*", end="")
    # Move to the next line after printing one row
    print()
    # Increment the row counter
    row += 1