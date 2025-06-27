#01.Write a program to input a name and print a greeting
def greet_user():
    name = input("Please enter your name: ")
    print(f"Hello, {name}! Welcome!")

# Call the function to execute it
if __name__ == "__main__":      
    greet_user()

#02. Write a program to add two numbers given by the user.
def add_two_numbers():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 + num2
        print(f"The sum of {num1} and {num2} is {result}.")
    except ValueError:
        print("Please enter valid numbers.")
# Call the function to execute it
if __name__ == "__main__":      
    add_two_numbers()   

#03. Write a program to check if a number is even or odd.
def check_even_odd():
    try:
        number = int(input("Enter a number: "))
        if number % 2 == 0:
            print(f"{number} is an even number.")
        else:
            print(f"{number} is an odd number.")
    except ValueError:
        print("Please enter a valid integer.")
# Call the function to execute it
if __name__ == "__main__":
    check_even_odd()

#04. Write a program to find the largest of three numbers.
def find_largest_of_three():

