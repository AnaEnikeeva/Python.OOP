class Student:
  def __init__(self, name, surname, gender):
      self.name = name
      self.surname = surname
      self.gender = gender
      self.finished_courses = []
      self.courses_in_progress = []
      self.grades = {}


  def lecturer_grades(self,lecturer, course, grade, ):
      if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
          if course in lecturer.grades:
              lecturer.grades[course] += [grade]
          else:
              lecturer.grades[course] = [grade]
      else:
          return 'Ошибка'

  def average_grades(self):
      mid_sum = 0
      for course_grades in self.grades.values():
          course_sum = 0
          for grade in course_grades:
              course_sum += grade
          course_mid = course_sum / len(course_grades)
          mid_sum += course_mid
      if mid_sum == 0:
          return (f'Оценок нет!')
      else:
          return round(mid_sum / len(self.grades.values()), 2)


  def __lt__(self, other): 
    if isinstance(other, Student):
      return self.average_grades() < other.average_grades()
    else:
      return 'Ошибка'




  def __str__(self):
      self.courses_in_progress = ", ".join(self.courses_in_progress)
      self.finished_courses = ", ".join(self.finished_courses)
      return (f'Имя: {self.name}\nФамилия: {self.surname}\n'
              f'Средняя оценка за домашние задания: {self.average_grades()}\n'
              f'Курсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}')



class Mentor:
  def __init__(self, name, surname):
      self.name = name
      self.surname = surname
      self.courses_attached = []


class Lecturer(Mentor):
  def __init__(self, name, surname):
      super().__init__(name, surname)
      self.grades = {}

  def average_grades_lecturer(self):
      mid_sum = 0
      for course_grades in self.grades.values():
          course_sum = 0
          for grade in course_grades:
              course_sum += grade
          course_mid = course_sum / len(course_grades)
          mid_sum += course_mid
      if mid_sum == 0:
          return f'Оценок нет!'
      else:
          return round(mid_sum / len(self.grades.values()), 2) 

  def __lt__(self, other):
    if isinstance(other, Lecturer):
      return self.average_grades_lecturer() < other.average_grades_lecturer()
    else:
      return 'Ошибка'



  def __str__(self):
      return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции:{self.average_grades_lecturer()}"




class Reviewer(Mentor):
  def __init__(self, name, surname):
      super().__init__(name, surname)

  def rate_hw(self, student, course, grade):
      if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
          if course in student.grades:
              student.grades[course] += [grade]
          else:
              student.grades[course] = [grade]
      else:
          return 'Ошибка'
  def __str__(self):
      return (f"Имя: {self.name}\nФамилия: {self.surname}")



student_1 = Student("Петр", "Петров", "М")
student_1.courses_in_progress += ["Python"]
student_1.finished_courses += ["Git"]

student_2 = Student("Иван", "Иванов", "М")
student_2.courses_in_progress += ["Python"]
student_2.finished_courses += ["Git"]

lecturer_1 = Lecturer("Олег", "Булыгин")
lecturer_1.courses_attached += ['Python']
lecturer_1.courses_attached += ['Git']

lecturer_2 = Lecturer("Елена", "Никитина")
lecturer_2.courses_attached += ['Python']
lecturer_2.courses_attached += ['Git']


reviewer_1 = Reviewer("Алена", "Батитская")
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['Git']

reviewer_2 = Reviewer("Александр", "Бардин")
reviewer_2.courses_attached += ['Python']
reviewer_2.courses_attached += ['Git']



reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_2.rate_hw(student_2, 'Python', 7)


reviewer_1.rate_hw(student_1, 'Git', 10)
reviewer_2.rate_hw(student_2, 'Git', 8)


student_1.lecturer_grades(lecturer_1, 'Python', 10)
student_2.lecturer_grades(lecturer_2, 'Python', 10)

student_1.lecturer_grades(lecturer_1, 'Git', 10)
student_2.lecturer_grades(lecturer_2, 'Git', 10)


print(f'Студенты:\n{student_1}\n{student_2}')
print(f'Лекторы:\n{lecturer_1}\n{lecturer_2}')

if student_1 > student_2:
  print(f' Успеваемость лучше у {student_1.name} {student_1.surname}, чем у {student_2.name} {student_2.surname}')
elif student_1 < student_2:
  print(f' Успеваемость лучше у {student_2.name} {student_2.surname}, чем у {student_1.name} {student_1.surname}')
elif student_1 == student_2:
  print(f' Успеваемость у студентов {student_1.name} {student_1.surname} и {student_2} {student_2} одинакова')

print(lecturer_1, lecturer_2, sep='\n')

if lecturer_1 > lecturer_2:
  print(f'Лектор {lecturer_1.name} {lecturer_1.surname} лучше, чем лектор {lecturer_2.name} {lecturer_2.surname}')
elif lecturer_1 < lecturer_2:
  print(f'Лектор {lecturer_2.name} {lecturer_2.surname} лучше, чем лектор {lecturer_1.name} {lecturer_1.surname}')
elif lecturer_1 == lecturer_2:
  print(f'Лектор {lecturer_2.name} {lecturer_2.surname} и лектор {lecturer_1.name} {lecturer_1.surname} одинаково хороши')