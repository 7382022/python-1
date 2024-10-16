def count_digits(number):
    # Convert the number to a string and count the characters
    return len(str(abs(number)))

# Initialize a variable to control the loop
valid_input = False

while not valid_input:
    user_input = input("Enter a number: ")
    try:
        number = int(user_input)
        valid_input = True  # Set to True if conversion is successful
    except ValueError:
        print("Please enter a valid integer.")

# Calculate the total digits and display the result
total_digits = count_digits(number)
print(f"The total number of digits in {number} is: {total_digits}")
