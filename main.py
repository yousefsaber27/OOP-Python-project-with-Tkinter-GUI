import tkinter as tk
from tkinter import messagebox


class Student:
    def __init__(self, student_id, name, age):
        self.student_id = student_id
        self.name = name
        self.age = age


class Course:
    def __init__(self, course_id, course_name, instructor):
        self.course_id = course_id
        self.course_name = course_name
        self.instructor = instructor


class Registration:
    def __init__(self):
        self.registrations = []

    def register(self, student, course):
        self.registrations.append((student, course))

    def get_courses_by_student(self, student_id):
        return [course for student, course in self.registrations if student.student_id == student_id]


class Department:
    def __init__(self, name):
        self.name = name
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)


class University:
    def __init__(self):
        self.students = []
        self.departments = []
        self.registration = Registration()

    def add_student(self, student):
        self.students.append(student)

    def add_department(self, department):
        self.departments.append(department)


class App:
    def __init__(self, root, university):
        self.root = root
        self.university = university
        self.root.title("Student Registration System")
        self.root.configure(bg='#f0f0f0')

        self.create_widgets()

    def create_widgets(self):
        self.student_frame = tk.Frame(self.root, bg='#cfe2f3', bd=2, relief='solid')
        self.student_frame.pack(pady=10, padx=10)

        tk.Label(self.student_frame, text="Student ID", bg='#cfe2f3').grid(row=0, column=0, padx=5, pady=5)
        tk.Label(self.student_frame, text="Name", bg='#cfe2f3').grid(row=1, column=0, padx=5, pady=5)
        tk.Label(self.student_frame, text="Age", bg='#cfe2f3').grid(row=2, column=0, padx=5, pady=5)

        self.student_id_entry = tk.Entry(self.student_frame)
        self.name_entry = tk.Entry(self.student_frame)
        self.age_entry = tk.Entry(self.student_frame)

        self.student_id_entry.grid(row=0, column=1, padx=5, pady=5)
        self.name_entry.grid(row=1, column=1, padx=5, pady=5)
        self.age_entry.grid(row=2, column=1, padx=5, pady=5)

        self.add_student_button = tk.Button(self.student_frame, text="Add Student", command=self.add_student,
                                            bg='#6fa8dc')
        self.add_student_button.grid(row=3, columnspan=2, pady=10)

        self.course_frame = tk.Frame(self.root, bg='#d9ead3', bd=2, relief='solid')
        self.course_frame.pack(pady=10, padx=10)

        tk.Label(self.course_frame, text="Course ID", bg='#d9ead3').grid(row=0, column=0, padx=5, pady=5)
        tk.Label(self.course_frame, text="Course Name", bg='#d9ead3').grid(row=1, column=0, padx=5, pady=5)
        tk.Label(self.course_frame, text="Instructor", bg='#d9ead3').grid(row=2, column=0, padx=5, pady=5)

        self.course_id_entry = tk.Entry(self.course_frame)
        self.course_name_entry = tk.Entry(self.course_frame)
        self.instructor_entry = tk.Entry(self.course_frame)

        self.course_id_entry.grid(row=0, column=1, padx=5, pady=5)
        self.course_name_entry.grid(row=1, column=1, padx=5, pady=5)
        self.instructor_entry.grid(row=2, column=1, padx=5, pady=5)

        self.add_course_button = tk.Button(self.course_frame, text="Add Course", command=self.add_course, bg='#93c47d')
        self.add_course_button.grid(row=3, columnspan=2, pady=10)

        self.registration_frame = tk.Frame(self.root, bg='#f4cccc', bd=2, relief='solid')
        self.registration_frame.pack(pady=10, padx=10)

        tk.Label(self.registration_frame, text="Student ID", bg='#f4cccc').grid(row=0, column=0, padx=5, pady=5)
        tk.Label(self.registration_frame, text="Course ID", bg='#f4cccc').grid(row=1, column=0, padx=5, pady=5)

        self.reg_student_id_entry = tk.Entry(self.registration_frame)
        self.reg_course_id_entry = tk.Entry(self.registration_frame)

        self.reg_student_id_entry.grid(row=0, column=1, padx=5, pady=5)
        self.reg_course_id_entry.grid(row=1, column=1, padx=5, pady=5)

        self.register_button = tk.Button(self.registration_frame, text="Register", command=self.register_student,
                                         bg='#e06666')
        self.register_button.grid(row=2, columnspan=2, pady=10)

        self.show_courses_button = tk.Button(self.registration_frame, text="Show Courses", command=self.show_courses,
                                             bg='#e06666')
        self.show_courses_button.grid(row=3, columnspan=2, pady=10)

    def add_student(self):
        student_id = self.student_id_entry.get()
        name = self.name_entry.get()
        age = self.age_entry.get()

        if student_id and name and age:
            student = Student(student_id, name, age)
            self.university.add_student(student)
            messagebox.showinfo("Success", "Student added successfully")
        else:
            messagebox.showwarning("Input Error", "Please fill all fields")

    def add_course(self):
        course_id = self.course_id_entry.get()
        course_name = self.course_name_entry.get()
        instructor = self.instructor_entry.get()

        if course_id and course_name and instructor:
            course = Course(course_id, course_name, instructor)
            department_name = "General"
            department = next((dept for dept in self.university.departments if dept.name == department_name), None)
            if not department:
                department = Department(department_name)
                self.university.add_department(department)
            department.add_course(course)
            messagebox.showinfo("Success", "Course added successfully")
        else:
            messagebox.showwarning("Input Error", "Please fill all fields")

    def register_student(self):
        student_id = self.reg_student_id_entry.get()
        course_id = self.reg_course_id_entry.get()

        if student_id and course_id:
            student = next((stu for stu in self.university.students if stu.student_id == student_id), None)
            if not student:
                messagebox.showwarning("Error", "Student not found")
                return
            course = None
            for department in self.university.departments:
                course = next((crs for crs in department.courses if crs.course_id == course_id), None)
                if course:
                    break
            if not course:
                messagebox.showwarning("Error", "Course not found")
                return
            self.university.registration.register(student, course)
            messagebox.showinfo("Success", "Registration successful")
        else:
            messagebox.showwarning("Input Error", "Please fill all fields")

    def show_courses(self):
        student_id = self.reg_student_id_entry.get()
        if student_id:
            courses = self.university.registration.get_courses_by_student(student_id)
            if courses:
                course_list = "\n".join([f"{course.course_id}: {course.course_name}" for course in courses])
                messagebox.showinfo("Courses Registered",
                                    f"Student ID {student_id} is registered in the following courses:\n\n{course_list}")
            else:
                messagebox.showinfo("No Courses", f"Student ID {student_id} is not registered in any courses.")
        else:
            messagebox.showwarning("Input Error", "Please enter a student ID")


university = University()
root = tk.Tk()
app = App(root, university)
root.mainloop()
