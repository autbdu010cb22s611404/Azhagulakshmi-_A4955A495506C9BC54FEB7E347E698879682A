'''
implement  a function called sort_student that takes a list of student  object  as input and sort the
list based on the CGPA(umulative Grade Point Avarage)in decending order.each student object
has the generate attributes: name (string),roll_no (string),and cpga(float).test the function
with difference input list of student .
'''


class Student:

  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sort_students(students_list):
  # Sort time list of student in decending  order of cgpa
  sorted_students = sorted(students_list,
                           key=lambda student: student.cgpa,
                           reverse=True)
  # synatax_lambda arg:exp
  return sorted_students


# Example usage:
students = [
    Student("Hari", "A123", 7.8),
    Student("Srikanth", "A124", 8.9),
    Student("Saumya", "A125", 9.1),
    Student("Mahidhar", "A126", 9.9),
]

sorted_students = sort_students(students)

# Print the sorted list of students
for student in sorted_students:
  print("Name:  {} ,Roll number:  {} ,CGPA: {}".format(student.name,
                                                       student.roll_number,
                                                       student.cgpa))
