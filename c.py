students = {}
courses = {}
mark = {}

def input_number_of_students ():
    return int(input("Enter students number"))
def input_student_information():
    for _ in range (input_number_of_students()):
        student_id = input("Enter student ID:")
        name = input("Enter student's name:")
        dob = input("Enter Date of Birth (DD/MM/YY):")
        students[student_id] ={"name:": name, "DOB:": dob}
def input_number_of_courses():
    return int(input("Enter number of courses:"))
def input_courses_information():
    for _ in range (input_number_of_courses()):
        name = input("Enter course's name:")
        courses_id = input("Enter course's ID:")
        courses[courses_id]={"name:":name, "courses ID:": courses_id}
def input_marks_for_courses():
    global mark
    if not courses:
        print("No avaiable courses. Please creat courses first")
        return
    if not students:
        print("No avaiable students. Please input students first")
        return
    courses_id = input("Enter course ID:")
    if courses_id not in courses:
        print("Coures not found")
        return
    courses_mark = {}
    for students_id, students in students.items():
        mark = float(input("Enter marks for {student['name']} (ID: {student_id}):"))
        courses_mark[students_id] = mark
    mark[courses_id] = courses_mark
def list_course():
    if not courses:
        print("Not available courses")
    else:
        print("Courses:")
        for course_id, info in courses.item():
            print(f"ID:{course_id}, Name: {info['name']}")
def list_students():
    if not students:
        print("No students available.")
    else:
        print("Students:")
        for student_id, info in students.items():
            print(f"ID: {student_id}, Name: {info['name']}, Date of Birth: {info['dob']}")
def show_student_marks():
    if not mark:
        print("No marks available.")
        return
    course_id = input("Enter course ID to show marks: ")
    if course_id not in mark:
        print("Course not found.")
        return
    print(f"Marks for course '{courses[course_id]['name']}':")
    for student_id, mark in mark[course_id].items():
        print(f"{students[student_id]['name']} (ID: {student_id}): {mark}")
def main():
    while True:
        print("\nOptions:")
        print("1. Input students")
        print("2. Input courses")
        print("3. Input marks for a course")
        print("4. List courses")
        print("5. List students")
        print("6. Show student marks for a course")
        print("7. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            input_student_information()
        elif choice == "2":
            input_courses_information()
        elif choice == "3":
            input_marks_for_courses()
        elif choice == "4":
            list_course()
        elif choice == "5":
            list_students()
        elif choice == "6":
            show_student_marks()
        elif choice == "7":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()




