#01.Write a function to find the square and cube of a number.
def square_and_cube():
    try:
        number = float(input("Enter a number: "))
        square = number ** 2
        cube = number ** 3
        print(f"Square of {number} is {square}, and cube is {cube}.")
    except ValueError:
        print("Please enter a valid number.")
# Call the function to execute it
if __name__ == "__main__":
    square_and_cube()   


#02.Write a function that returns the number of uppercase and lowercase letters in a string.
def count_case_in_string():
    input_string = input("Enter a string: ")
    upper_count = sum(1 for char in input_string if char.isupper())
    lower_count = sum(1 for char in input_string if char.islower())
    print(f"Uppercase letters: {upper_count}, Lowercase letters: {lower_count}")
# Call the function to execute it
if __name__ == "__main__":
    count_case_in_string()


#03.Write a program to check if a string is a palindrome using a function.
def is_palindrome():
    input_string = input("Enter a string: ")
    cleaned_string = ''.join(char.lower() for char in input_string if char.isalnum())
    if cleaned_string == cleaned_string[::-1]:
        print(f'"{input_string}" is a palindrome.')
    else:
        print(f'"{input_string}" is not a palindrome.')
# Call the function to execute it
if __name__ == "__main__":
    is_palindrome()


#04.Write a function to calculate the area of a rectangle.
def calculate_area_of_rectangle():
    try:
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = length * width
        print(f"The area of the rectangle is {area}.")
    except ValueError:
        print("Please enter valid numbers for length and width.")
# Call the function to execute it
if __name__ == "__main__":
    calculate_area_of_rectangle()


