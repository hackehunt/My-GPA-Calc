#-----------------------Importing from Classes.py and ErrorMsg.py

from Classes.Course import Course
from Classes.ErrorMsg import ErrorMsg

#-----------------------Main calculator programme

class Calculator:
    gpa = 0
    points = 0
    courses = [[]]  # array of arrays from 1 point courses to 10 point courses

    def __init__(self):
        for x in range(19):
            self.courses.append([])

    # adds a course to the calculator
    def add_course(self, name, points, grade):
        if len(name) > 30:
            return ErrorMsg("Course name must be less then 30 characters!")
        if grade < 0 or grade > 100:
            return ErrorMsg("Grade must be in range 0-100!")
        course = Course(name, points, grade)
        # put new course in appropriate array and keep it sorted
        i = 0
        for x in self.courses[points * 2 - 2]:
            if course.grade < x.grade:
                self.courses[points * 2 - 2].insert(i, course)
                break
            i += 1

        if i == len(self.courses[points * 2 - 2]):  # last position
            self.courses[points * 2 - 2].append(course)

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
# x = calc.add_course("one", 4, 88)
# if type(x) is ErrorMsg:
#     print(x.msg)
# x = calc.add_course("two", 5, 150)
# if type(x) is ErrorMsg:
#     print(x.msg)
# x = calc.add_course(
#     "twdwadwadadwdawdwdawdwdwadawdadwdwadwdwadwadwdwadwdaddawddawdaddwdwadsdwadwdaddawdawdadwdawdwdadwdadwdwadadwdasdwadwdawdwo",
#     5, 60)
# if type(x) is ErrorMsg:
#     print(x.msg)
# temp = calc.add_course("three", 5, 68)
# calc.add_course("four", 6, 90)
# calc.add_course("five", 3, 55)
# calc.add_course("six", 5, 90)
# calc.add_course("seven", 5, 55)
# calc.remove_course(temp)
#
# for x in calc.courses[8]:
#     print(x.name)
# print(calc.courses[8][0].name, calc.courses[8][1].name)
# print(calc.gpa, calc.points)
#
# calc.remove_course(temp)
# print(calc.gpa, calc.points)
#
# for course_list in calc.courses:
#     if course_list:
#         for course in course_list:
#             print(course.name)

# ut.sort(key=lambda x: x.count, reverse=True)
