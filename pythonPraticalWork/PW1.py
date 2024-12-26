# Student Mark Management System

def input_number_of_students():
    return int(input("Enter the number of students: "))

def input_student_info():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    dob = input("Enter student Date of Birth (DD/MM/YYYY): ")
    return (student_id, name, dob)

def input_number_of_courses():
    return int(input("Enter the number of courses: "))

def input_course_info():
    course_id = input("Enter course ID: ")
    name = input("Enter course name: ")
    return (course_id, name)

def select_course(courses):
    print("Available courses:")
    for i, course in enumerate(courses):
        print(f"{i + 1}. {course[1]} (ID: {course[0]})")
    course_index = int(input("Select a course by its number: ")) - 1
    return courses[course_index]

def input_marks(course, students):
    marks = {}
    print(f"Input marks for course: {course[1]}")
    for student in students:
        mark = float(input(f"Enter marks for {student[1]} (ID: {student[0]}): "))
        marks[student[0]] = mark
    return marks

def list_courses(courses):
    print("Courses:")
    for course in courses:
        print(f"- {course[1]} (ID: {course[0]})")

def list_students(students):
    print("Students:")
    for student in students:
        print(f"- {student[1]} (ID: {student[0]}, DoB: {student[2]})")

def show_student_marks(course, marks, students):
    print(f"Marks for course: {course[1]} (ID: {course[0]})")
    for student in students:
        student_id = student[0]
        if student_id in marks:
            print(f"- {student[1]} (ID: {student_id}): {marks[student_id]}")
        else:
            print(f"- {student[1]} (ID: {student_id}): No marks recorded")

def main():
    students = []
    courses = []
    course_marks = {}

    num_students = input_number_of_students()
    for _ in range(num_students):
        students.append(input_student_info())

    num_courses = input_number_of_courses()
    for _ in range(num_courses):
        courses.append(input_course_info())

    while True:
        print("\nMenu:")
        print("1. List students")
        print("2. List courses")
        print("3. Input marks for a course")
        print("4. Show student marks for a course")
        print("5. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            list_students(students)
        elif choice == "2":
            list_courses(courses)
        elif choice == "3":
            if not courses:
                print("No courses available.")
                continue
            selected_course = select_course(courses)
            course_marks[selected_course[0]] = input_marks(selected_course, students)
        elif choice == "4":
            if not courses:
                print("No courses available.")
                continue
            selected_course = select_course(courses)
            if selected_course[0] in course_marks:
                show_student_marks(selected_course, course_marks[selected_course[0]], students)
            else:
                print("No marks recorded for this course.")
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

main()
