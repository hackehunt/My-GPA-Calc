from Classes.Course import Course


class Calculator:
    gpa = 0
    points = 0
    courses = [[]]  # array of arrays from 1 point courses to 10 point courses

    def __init__(self):
        for x in range(19):
            self.courses.append([])

    # adds a course to the calculator
    def add_course(self, name, points, grade):
        course = Course(name, points, grade)
        self.courses[points * 2 - 2].append(course)  # put new course in appropriate array
        new_points = self.points + points
        self.gpa = (self.points / new_points * self.gpa) + (points / new_points * grade)
        self.points += points
        return course

    # removes a course from the calculator
    def remove_course(self, course):
        if course in self.courses[course.points * 2 - 2]:
            self.courses[course.points * 2 - 2].remove(course)

        self.gpa = ((self.gpa * self.points) - (course.grade * course.points)) / (self.points - course.points)
        self.points = self.points - course.points


# calc = Calculator()
# calc.add_course("one", 4, 88)
# calc.add_course("two", 5, 70)
# temp = calc.add_course("three", 5, 68)
# calc.add_course("four", 6, 90)
# calc.add_course("five", 3, 55)
# print(calc.gpa, calc.points)
#
# calc.remove_course(temp)
# print(calc.gpa, calc.points)
#
# for course_list in calc.courses:
#     if course_list:
#         for course in course_list:
#             print(course.name)
