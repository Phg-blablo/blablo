students = {}
courses = {}
marks = {}  # Changed from list to dictionary to store marks per course

def input_number_of_students():
    return int(input("Enter the number of students: "))

def input_student_information():
    for _ in range(input_number_of_students()):
        student_id = input("Enter student ID: ")
        name = input("Enter student's name: ")
        dob = input("Enter Date of Birth (DD/MM/YY): ")
        students[student_id] = {"name": name, "dob": dob}

def input_number_of_courses():
    return int(input("Enter the number of courses: "))

def input_courses_information():
    for _ in range(input_number_of_courses()):
        course_id = input("Enter course ID: ")
        name = input("Enter course name: ")
        courses[course_id] = {"name": name}

def input_marks_for_courses():
    if not courses:
        print("No available courses. Please create courses first.")
        return
    if not students:
        print("No available students. Please input students first.")
        return
    
    course_id = input("Enter course ID: ")
    if course_id not in courses:
        print("Course not found.")
        return
    
    course_marks = {}
    for student_id, student in students.items():
        mark = float(input(f"Enter marks for {student['name']} (ID: {student_id}): "))
        course_marks[student_id] = mark
    marks[course_id] = course_marks

def list_courses():
    if not courses:
        print("No available courses.")
    else:
        print("Courses:")
        for course_id, info in courses.items():
            print(f"ID: {course_id}, Name: {info['name']}")

def list_students():
    if not students:
        print("No students available.")
    else:
        print("Students:")
        for student_id, info in students.items():
            print(f"ID: {student_id}, Name: {info['name']}, Date of Birth: {info['dob']}")

def show_student_marks():
    if not marks:
        print("No marks available.")
        return
    
    course_id = input("Enter course ID to show marks: ")
    if course_id not in marks:
        print("Course not found.")
        return
    
    print(f"Marks for course '{courses[course_id]['name']}':")
    for student_id, mark in marks[course_id].items():
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
            list_courses()
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
