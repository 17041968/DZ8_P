#Дана квадратная матрица, заполненная случайными числами
#Определите, сумма элементов каких строк превосходит сумму главной диагонали матрицы.
from random import randint

size = 4
matrix = [0] * size

for i in range(size):
	matrix[i] = list(randint(1, 10) for c in range(size))

for i in matrix:
	print(i)

sum_diagonal = 0
for i in range(size):
	for j in range(size):
		if i == j:
			print(matrix[i][j], end = ' ')
			sum_diagonal += matrix[i][j]

print()
print(sum_diagonal)

sum_in_rows = []
for i in matrix:
	sum_in_rows.append(sum(i))

print(sum_in_rows)

for i in range(len(sum_in_rows)):
	if sum_in_rows[i] > sum_diagonal:
		print(f"в {i+1} группе сумма больше, чем сумма элементов диагонали")
