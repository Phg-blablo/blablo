class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob

    def __str__(self):
        return f"{self.name} (ID: {self.student_id}, DoB: {self.dob})"


class Course:
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name
        self.marks = {}

    def add_mark(self, student_id, mark):
        self.marks[student_id] = mark

    def get_mark(self, student_id):
        return self.marks.get(student_id, "No marks recorded")

    def __str__(self):
        return f"{self.name} (ID: {self.course_id})"


class StudentMarkManagement:
    def __init__(self):
        self.students = []
        self.courses = []

    def input_number_of_students(self):
        return int(input("Enter the number of students: "))

    def input_student_info(self):
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student Date of Birth (DD/MM/YYYY): ")
        self.students.append(Student(student_id, name, dob))

    def input_number_of_courses(self):
        return int(input("Enter the number of courses: "))

    def input_course_info(self):
        course_id = input("Enter course ID: ")
        name = input("Enter course name: ")
        self.courses.append(Course(course_id, name))

    def select_course(self):
        print("Available courses:")
        for i, course in enumerate(self.courses):
            print(f"{i + 1}. {course}")
        course_index = int(input("Select a course by its number: ")) - 1
        return self.courses[course_index]

    def input_marks(self, course):
        print(f"Input marks for course: {course.name}")
        for student in self.students:
            mark = float(input(f"Enter marks for {student.name} (ID: {student.student_id}): "))
            course.add_mark(student.student_id, mark)

    def list_courses(self):
        print("Courses:")
        for course in self.courses:
            print(f"- {course}")

    def list_students(self):
        print("Students:")
        for student in self.students:
            print(f"- {student}")

    def show_student_marks(self, course):
        print(f"Marks for course: {course.name} (ID: {course.course_id})")
        for student in self.students:
            mark = course.get_mark(student.student_id)
            print(f"- {student.name} (ID: {student.student_id}): {mark}")

    def main(self):
        num_students = self.input_number_of_students()
        for _ in range(num_students):
            self.input_student_info()

        num_courses = self.input_number_of_courses()
        for _ in range(num_courses):
            self.input_course_info()

        while True:
            print("\nMenu:")
            print("1. List students")
            print("2. List courses")
            print("3. Input marks for a course")
            print("4. Show student marks for a course")
            print("5. Exit")

            choice = input("Select an option: ")

            if choice == "1":
                self.list_students()
            elif choice == "2":
                self.list_courses()
            elif choice == "3":
                if not self.courses:
                    print("No courses available.")
                    continue
                selected_course = self.select_course()
                self.input_marks(selected_course)
            elif choice == "4":
                if not self.courses:
                    print("No courses available.")
                    continue
                selected_course = self.select_course()
                self.show_student_marks(selected_course)
            elif choice == "5":
                print("Exiting...")
                break
            else:
                print("Invalid option. Please try again.")


if __name__ == "__main__":
    system = StudentMarkManagement()
    system.main()
