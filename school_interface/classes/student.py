from .person import Person
import csv

"""
Student class
    - name
    - age, int
    - role: "Student" - hardcode
    - school_id, int
    - password
- Create students from csv data
"""
class Student(Person):
    all_students_lst = []

    """
    Class method to get all the students from the csv file and add them to all_students_list
    """
    @classmethod
    def all_students(cls, path_to_file):
        # Prototype getting students.csv
        # Open the file
        with open(path_to_file, mode='r', newline='') as csvfile:
            # Turn each row of the csv file into a dictionary
            student_data_reader = csv.DictReader(csvfile)
            for student_data in student_data_reader:
                # Destructure dictionary into vars we can pass as named arguments
                # to the Student class constructor
                a_student = Student(**student_data)
                cls.all_students_lst.append(a_student)

        return cls.all_students_lst

    @classmethod
    def get_student_by_name(cls, name):
        for student in cls.all_students_lst:
            if name.lower() == student.name.lower():
                return student
            else:
                return None

    def __init__(self, name=None, age=None, role=None, school_id=None, password=None):
        super().__init__(name, age, role)
        self.school_id = int(school_id)
        self._password = password

    def __repr__(self):
        return f"Name: {self.name} | Age: {self.age} | Role: {self.role} | School ID: {self.school_id} | Password: {self._password}"

    @property
    def get_password(self):
        return f"Password: {self._password}"

    @get_password.setter
    def set_password(self, new_password):
        if len(new_password) < 5:
            print("Password must be at least 5 characters long")
        else:
            self._password = new_password



