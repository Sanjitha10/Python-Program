#01.Write a program to create a text file and write 5 lines into it.
def create_and_write_file():
    try:
        with open("example.txt", "w") as file:
            for i in range(1, 6):
                file.write(f"This is line {i}\n")
        print("File created and written successfully.")
    except IOError as e:
        print(f"An error occurred while writing to the file: {e}")
# Call the function to execute it
if __name__ == "__main__":
    create_and_write_file()


#02.Read the content of the above file and print it line by line.
def read_file_line_by_line():
    try:
        with open("example.txt", "r") as file:
            for line in file:
                print(line.strip())
    except IOError as e:
        print(f"An error occurred while reading the file: {e}")
# Call the function to execute it
if __name__ == "__main__":
    read_file_line_by_line()
    

#03.Task: Create a simple student mark calculator using functions and dictionaries. Input name and 3 subject marks, and print total, average, and grade.
def student_mark_calculator():
    try:
        student_name = input("Enter the student's name: ")
        marks = {}
        subjects = ["Math", "Science", "English"]
        
        for subject in subjects:
            while True:
                try:
                    mark = float(input(f"Enter marks for {subject}: "))
                    if 0 <= mark <= 100:
                        marks[subject] = mark
                        break
                    else:
                        print("Marks should be between 0 and 100. Please try again.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
        
        total_marks = sum(marks.values())
        average_marks = total_marks / len(subjects)
        
        if average_marks >= 90:
            grade = 'A'
        elif average_marks >= 80:
            grade = 'B'
        elif average_marks >= 70:
            grade = 'C'
        elif average_marks >= 60:
            grade = 'D'
        else:
            grade = 'F'
        
        print(f"\nStudent Name: {student_name}")
        print(f"Total Marks: {total_marks}")
        print(f"Average Marks: {average_marks:.2f}")
        print(f"Grade: {grade}")
    
    except Exception as e:
        print(f"An error occurred: {e}")
# Call the function to execute it
if __name__ == "__main__":
    student_mark_calculator()


