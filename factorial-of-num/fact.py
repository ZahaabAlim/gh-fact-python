def calculate_factorial(number):
   if number < 0:
       return "Factorial is not defined for negative numbers."
   elif number == 0 or number == 1:
       return 1
   else:
       result = 1
       for i in range(2, number + 1):
           result *= i
       return result
# Get user input for the number
user_input = int(input("Enter a number to calculate its factorial: "))
# Calculate and print the factorial
result = calculate_factorial(user_input)
print(f"The factorial of {user_input} is: {result}")