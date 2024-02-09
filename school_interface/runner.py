from classes.school import School 
from classes.student import Student
from classes.staff import Staff
import csv

school = School(
    'Ridgemont High',
    students_file_path="./data/students.csv",
    staff_file_path="./data/staff.csv",
    ) 

# print(school.name)
# print(school.staff)
# print(school.students)

a_student = school.students[0]

print(a_student.get_password)
a_student.set_password = "xyz12345"
print(a_student.get_password)

# Make our terminal

main_menu_message = """
What would you like to do?
Options:
    1. List All Students
    2. View Individual Student <student_id>
    3. Add a Student
    4. Remove a Student <student_id>
    5. Quit
"""

def display_all_students_menu():
    print(school.students)

def display_view_individual_student_menu():
    name = input("What is the name of the student you want to view?")
    student = Student.get_student_by_name(name)
    if student is None:
        print("That student isn't at this school")
    else:
        print(student)

def display_add_a_student_menu():
    print("Add student")
    

def display_remove_a_student_menu():
    print("Remove Student")
    pass

def display_main_menu():
    user_main_menu_input = input(main_menu_message)
    print(user_main_menu_input)

    if user_main_menu_input == "1":
        display_all_students_menu()
        display_main_menu()
    elif user_main_menu_input == "2":
        display_view_individual_student_menu()
        display_main_menu()
    elif user_main_menu_input == "3":
        display_add_a_student_menu()
        display_main_menu()
    elif user_main_menu_input == "4":
        display_remove_a_student_menu()
        display_main_menu()
    # Quit
    elif user_main_menu_input == "5":
        print('Have a brutal day')
        exit()
    # Invalid input
    else:
        print("Invalid input, please type '1', '2', '3', etc, to select an Option")
        display_main_menu()

# Run the program!
display_main_menu()
