#В каждой группе учится от 20 до 30 студентов. По итогам экзамена все оценки заносятся в таблицу.
#Каждой группе отведена своя строка. Определите группу с наилучшим средним баллом.
from random import randint

groups = 5
grades = [0] * groups

for i in range(len(grades)):
	grades[i] = list(randint(2, 5) for s in range(randint(20, 30)))

mean_grades = []

for grades_in_group in grades:
	mean = 0
	for grade in grades_in_group:
		mean += grade
	mean_grades.append(round(mean/len(grades_in_group), 2))
for grades_in_group in grades:
	print(grades_in_group)

print(mean_grades)

max_grade = max(mean_grades)
number_group = mean_grades.index(max_grade)
print(f'наилучший средний балл {max_grade}, его получила группа {number_group+1}')
