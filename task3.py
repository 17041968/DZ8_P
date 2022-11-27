#В двумерном массиве хранятся средние дневные температуры с мая по сентябрь за прошлый год
#Каждому месяцу соответствует своя строка. Определите самый жаркий и самый холодный
#7-дневный промежуток этого периода. Выведите его даты.
from random import randint
import statistics

def find_data(days):
	for month_number in range(len(matrix)):
		days_in_month = len(matrix[month_number])
		if days_in_month >= days:
			return(month_number, days)
		else:
			days -= days_in_month

period = 10

monthsInfo = [('мая', 31), ('июня', 30), ('июля', 31), ('августа', 31),('сентября', 30)]
size = len(monthsInfo)
matrix = [0] * size

for i in range(size):
	matrix[i] = list(randint(12, 30) for c in range(monthsInfo[i][1]))

print('ежедневная температура')
for i in matrix:
	print(i)
print()

matrix_in_row = []

for row_matrix in matrix:
	for el in row_matrix:
		matrix_in_row.append(el)

mean_temp = []
for i in range(len(matrix_in_row) - period + 1):
	mean_temp.append(sum(matrix_in_row[i:i+period])/period)

max_el = max(mean_temp)
index_max_el = mean_temp.index(max_el)
print(f'средняя максимальная температура за период {max_el}')

dateStart = find_data(index_max_el +1)
dateFinish = find_data(index_max_el + period)
print(f'самый теплый {period} - дневный период')
print(f'{dateStart[1]} {monthsInfo[dateStart[0]][0]} - {dateFinish[1]} {monthsInfo[dateFinish[0]][0]}')

min_el = min(mean_temp)
index_min_el = mean_temp.index(min_el)
print(f'средняя минимальная температура за период {min_el}')

dateStart = find_data(index_min_el +1)
dateFinish = find_data(index_min_el + period)
print(f'самый холодный {period} - дневный период')
print(f'{dateStart[1]} {monthsInfo[dateStart[0]][0]} - {dateFinish[1]} {monthsInfo[dateFinish[0]][0]}')