from functools import total_ordering


@total_ordering
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lec(self, lecturer, course, grade):
        if grade < 0 or grade > 10:
            return 'Error'
        if (isinstance(lecturer, Lecturer) and 
                course in lecturer.courses_attached and 
                course in self.courses_in_progress):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Error'

    def avg_grade(self):
        if self.grades:
            all_grades = [grade for grades in self.grades.values() for grade in grades]
            return sum(all_grades) / len(all_grades)
        else:
            return 0

    def __str__(self):
        avg_grade = self.avg_grade()
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {avg_grade:.1f}\n"
                f"Курсы в процессе изучения: {courses_in_progress}\n"
                f"Завершенные курсы: {finished_courses}")

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.avg_grade() < other.avg_grade()
        return "Error"

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.avg_grade() == other.avg_grade()
        return "Error"


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


@total_ordering
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def avg_grade(self):
        if self.grades:
            all_grades = [grade for grades in self.grades.values() for grade in grades]
            return sum(all_grades) / len(all_grades)
        else:
            return 0

    def __str__(self):
        avg_grade = self.avg_grade()
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {avg_grade:.1f}")

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.avg_grade() < other.avg_grade()
        return "Error"

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.avg_grade() == other.avg_grade()
        return "Error"


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if grade < 0 or grade > 10:
            return 'Error'
        if (isinstance(student, Student) and 
                course in self.courses_attached and 
                course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Error'

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}")


def avg_student_grade(students, course):
    all_grades = []
    for student in students:
        if course in student.grades:
            all_grades.extend(student.grades[course])
    if all_grades:
        return sum(all_grades) / len(all_grades)
    else:
        return 0


def avg_lecturer_grade(lecturers, course):
    all_grades = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            all_grades.extend(lecturer.grades[course])
    if all_grades:
        return sum(all_grades) / len(all_grades)
    else:
        0


if __name__ == '__main__':
    # Создание экземпляров
    student1 = Student("Joe", "Doe", "male")
    student1.courses_in_progress = ["Python", "Git"]
    student1.finished_courses = ["Введение в программирование"]

    student2 = Student("Alice", "Wonder", "female")
    student2.courses_in_progress = ["Python"]

    lecturer1 = Lecturer("Some", "Buddy")
    lecturer1.courses_attached = ["Python"]

    lecturer2 = Lecturer("Jane", "Doe")
    lecturer2.courses_attached = ["Python"]

    reviewer1 = Reviewer("John", "Smith")
    reviewer1.courses_attached = ["Python"]

    reviewer2 = Reviewer("Emily", "White")
    reviewer2.courses_attached = ["Git"]

    # Вызов методов
    reviewer1.rate_hw(student1, "Python", 10)
    reviewer1.rate_hw(student1, "Python", 9)
    reviewer1.rate_hw(student2, "Python", 8)
    reviewer2.rate_hw(student1, "Git", 7)

    student1.rate_lec(lecturer1, "Python", 10)
    student1.rate_lec(lecturer1, "Python", 9)
    student2.rate_lec(lecturer1, "Python", 8)
    student1.rate_lec(lecturer2, "Python", 7)

    # Вывод объектов
    print(student1)
    print(student2)
    print(lecturer1)
    print(lecturer2)
    print(reviewer1)
    print(reviewer2)

    # Сравнение студентов и лекторов
    print(student1 > student2)  # True
    print(student1 < student2)  # False
    print(student1 != student2)  # True
    print(student1 == student2)  # False
    print(lecturer1 > lecturer2)  # True
    print(lecturer1 < lecturer2)  # False
    print(lecturer1 != lecturer2)  # True
    print(lecturer1 == lecturer2)  # False

    # Подсчет средней оценки
    students = [student1, student2]
    lecturers = [lecturer1, lecturer2]

    print("Средняя оценка за Д/З по Python:")
    print(f"{avg_student_grade(students, 'Python'):.1f}")
    print("Средняя оценка за лекции по Python:")
    print(f"{avg_lecturer_grade(lecturers, 'Python'):.1f}")
