def extract_second_last_digit(number):
    # Convert number to positive if it's negative
    number = abs(number)
    
    # Extract the second last digit
    second_last_digit = (number // 10) % 10
    
    # Return the second last digit
    return second_last_digit

# Take input from the user
number = int(input("Enter a number: "))

# Call the function and print the result
print("Second last digit of", number, "is:", extract_second_last_digit(number))
