#01.Create a list of 5 numbers. Print the sum and average.
def list_sum_and_average():
    numbers = [10, 20, 30, 40, 50]
    total = sum(numbers)
    average = total / len(numbers)
    print(f"Sum: {total}, Average: {average}")
# Call the function to execute it
if __name__ == "__main__":
    list_sum_and_average()


#02.Store 5 subjects and marks in a dictionary. Display subject with the highest marks.
def highest_marks_subject():
    subjects = {
        "Math": 85,
        "Science": 90,
        "English": 78,
        "History": 88,
        "Geography": 92
    }
    highest_subject = max(subjects, key=subjects.get)
    print(f"Subject with highest marks: {highest_subject} ({subjects[highest_subject]})")
# Call the function to execute it
if __name__ == "__main__":
    highest_marks_subject()


#03.Create a tuple of 5 elements. Print it in reverse order.
def reverse_tuple():
    my_tuple = (1, 2, 3, 4, 5)
    reversed_tuple = my_tuple[::-1]
    print(f"Original tuple: {my_tuple}, Reversed tuple: {reversed_tuple}")
# Call the function to execute it
if __name__ == "__main__":  
    reverse_tuple()


#04.Write a program to count the number of vowels in a string.
def count_vowels_in_string():
    input_string = input("Enter a string: ")
    vowels = "aeiouAEIOU"
    count = sum(1 for char in input_string if char in vowels)
    print(f"Number of vowels in the string: {count}")
# Call the function to execute it
if __name__ == "__main__":
    count_vowels_in_string()







