#01.Write a program to print all even numbers between 1 and 50.
def print_even_numbers():
    even_numbers = [num for num in range(1, 51) if num % 2 == 0]
    print("Even numbers between 1 and 50:", even_numbers)
# Call the function to execute it
if __name__ == "__main__":
    print_even_numbers()


#02.Write a program to display the multiplication table of a number.
def multiplication_table():
    try:
        number = int(input("Enter a number to display its multiplication table: "))
        print(f"Multiplication table of {number}:")
        for i in range(1, 11):
            print(f"{number} x {i} = {number * i}")
    except ValueError:
        print("Please enter a valid integer.")
# Call the function to execute it
if __name__ == "__main__":
    multiplication_table()


#03.Write a program to find the sum of digits of a number.
def sum_of_digits():
    try:
        number = int(input("Enter a number to find the sum of its digits: "))
        digit_sum = sum(int(digit) for digit in str(abs(number)))
        print(f"The sum of the digits of {number} is {digit_sum}.")
    except ValueError:
        print("Please enter a valid integer.")
# Call the function to execute it
if __name__ == "__main__":
    sum_of_digits()


#04.Write a program to check if a number is a prime number.
def is_prime():
    try:
        number = int(input("Enter a number to check if it is prime: "))
        if number <= 1:
            print(f"{number} is not a prime number.")
            return
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                print(f"{number} is not a prime number.")
                return
        print(f"{number} is a prime number.")
    except ValueError:
        print("Please enter a valid integer.")
# Call the function to execute it
if __name__ == "__main__":  
    is_prime()


#05.Write a program to reverse a number.
def reverse_number():
    try:
        number = int(input("Enter a number to reverse it: "))
        reversed_num = str(number)[::-1]
        print(f"The reverse of {number} is {reversed_num}.")
    except ValueError:
        print("Please enter a valid integer.")
# Call the function to execute it
if __name__ == "__main__":
    reverse_number()

