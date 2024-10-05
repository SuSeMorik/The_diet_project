# Импортирую необходимые библиотеки, называю их.

import os
import random
from plotly import offline
from plotly.graph_objs import Bar, Layout

# Списки и перменные.

foods = [['куриный суп', '2', '350'], ['борщ', '2', '250'],\
['пельмени', '2', '900'], ['рассольник', '2', '150'],\
['рис с овощами', '2', '450'], ['рыбные котлеты', '2', '450'],\
['гречка с грибами', '2', '500'], ['яичница', '3', '700'],\
['свинные паренные котлеты', '3', '925'], ['ассорти из орехов', '1', '1100'],\
['курине филе на гриле', '3', '500'], ['уха', '3', '300'],\
['творог', '3', '550'], ['жаренные котлеты куриные', '3', '900'],\
['белковый амлет', '3', '350'],\
['cвинина по-крестьянски', '1', '1060'], ['сырные шарики "Панко"', '1', '750'],\
['сало с мясной послойкой', '1', '1000'], ['сырные булочки', '1', '750'],\
['смесь семян', '1', '1100'], ['мясо с овощами', '1', '650']]
days = ['Понедельик', 'Вторник', 'Среда', 'Четверг',\
'Пятница', 'Суббота', 'Воскресенье']
graphic_y = []
time_check, day_check = 0, 0

# Функции для основной программы.

def dish_generation():

	"""Записывает данные о новом блюде"""

	dish = []
	dish_name = input('Как называется ваше блюдо? ')
	try:
		dish_category = input('Чего больше в блюде (число)?\
		\n1)жиров\n2)углеводов\n3)белков\n')
		if int(dish_category) > 3 or int(dish_category) < 1:
			print('Вводите положенные значения!')
			quit ()
		else:
			dish_calori = input('Сколько в блюде калорий (число)? ')
			dish.append(dish_name.lower())
			dish.append(dish_category)
			dish.append(int(dish_calori))
	except ValueError:
		print('Вводите положенные значения!')
		quit ()
	print('*****Новое блюдо добавлено!*****')
	print(f'***{dish_name.title()}***')
	print('*********************************')
	return (dish)

def sort_category(foods):

	"""Сортирует блюда по типам (жиры, углеводы, белки)"""

	fats_food = []
	carbohydrates_food = []
	proteins_food = []
	for food in foods:
		if food[1] == '1':
			fats_food.append(food)
		elif food[1] == '2':
			carbohydrates_food.append(food)
		elif food[1] == '3':
			proteins_food.append(food)
	return fats_food, carbohydrates_food, proteins_food

def sort_day (fats_food, carbohydrates_food, proteins_food):

	"""Формирует первичные данные о приёмах пищи для дня"""

	dish_mor = random.choice(fats_food)
	fats_food.remove(dish_mor)

	dish_din = random.choice(proteins_food)
	proteins_food.remove(dish_din)

	dish_eve = random.choice(carbohydrates_food)
	carbohydrates_food.remove(dish_eve)

	return dish_mor, dish_din, dish_eve

def day_creator (rester):

	"""Обрабатывает и записывает первичные данные в txt файл"""

	with open('The diet.txt', 'a') as out:
		for lunch in rester:

			out.write(f'************************\n')
			out.write(f'* Название: {lunch[0].capitalize()}\n')

			if lunch [1] == '1':
				out.write('* Тип: Жирная пища\n')
			elif lunch [1] == '2':
				out.write('* Тип: Углеводная пища\n')
			elif lunch [1] == '3':
				out.write('* Тип: Белковая пища\n')

			if lunch [1] == '1':
				out.write('* Масса: 200 грамм\n')
			else:
				out.write('* Масса: 400 грамм\n')

			out.write(f'* Калорий: {lunch[2]}\n')
			out.write(f'************************\n')

def day_writer(day_check):

	"""Высчитывай день недели по данной переменной"""

	with open('The diet.txt', 'a') as out:

		if day_check == 0:
			out.write('\n-----ПОНЕДЕЛЬНИК-----\n')
		if day_check == 1:
			out.write('\n-----ВТОРНИК-----\n')
		if day_check == 2:
			out.write('\n-----СРЕДА-----\n')
		if day_check == 3:
			out.write('\n-----ЧЕТВЕРГ-----\n')
		if day_check == 4:
			out.write('\n-----ПЯТНИЦА-----\n')
		if day_check == 5:
			out.write('\n-----СУББОТА-----\n')
		if day_check == 6:
			out.write('\n-----ВОСКРЕСЕНЬЕ-----\n')

# Уточняются цели пользователя для далнейшей работы.

time = input('Сколько блюд вы хотите добавить? \
\n(-1 если хотите воспользоваться стандартной библиотекой блюд)\n\
(0 если вы хотите создать свой список с чистого листа - 21 блюдо, минимум \
7 белковых, 7 жировых и 7 углеводных)\n\
(1 и более если вы хотите добавить несколько позиций)\
После вы сможете ознакомится с расписанием диеты в текстовом формате,\
\nа так же изучить график калорий.')

if int(time) == -1:
	time_check = 1
elif int(time) == 0:
	foods.clear()
	time = 20
	while time_check <= int(time):
		foods.append(dish_generation())
		time_check += 1
else:
	time_check = 1
	while time_check <= int(time):
		foods.append(dish_generation())
		time_check += 1

# Предохранитель удаляющий прошлый список (иначе они могут смешаться).

try: 
	os.remove("The diet.txt")
except:
	pass

# Разделяю пишу по типам с помощью функции модуля (жиры, углеводы, белки).

fats_food, carbohydrates_food, proteins_food = sort_category(foods)

# Создаю уникальное расписания с помощью функции модуля для каждого из дня.

day_1 = sort_day(fats_food, carbohydrates_food, proteins_food)
day_2 = sort_day(fats_food, carbohydrates_food, proteins_food)
day_3 = sort_day(fats_food, carbohydrates_food, proteins_food)
day_4 = sort_day(fats_food, carbohydrates_food, proteins_food)
day_5 = sort_day(fats_food, carbohydrates_food, proteins_food)
day_6 = sort_day(fats_food, carbohydrates_food, proteins_food)
day_7 = sort_day(fats_food, carbohydrates_food, proteins_food)

# Запись данных в txt файл (и костыль для подсчёта дня :3)

day_writer(day_check)
day_creator(day_1)

day_check += 1
day_writer(day_check)
day_creator(day_2)

day_check += 1
day_writer(day_check)
day_creator(day_3)

day_check += 1
day_writer(day_check)
day_creator(day_4)

day_check += 1
day_writer(day_check)
day_creator(day_5)

day_check += 1
day_writer(day_check)
day_creator(day_6)

day_check += 1
day_writer(day_check)
day_creator(day_7)

# Создания перменой week состоящей из списка дней, который в свою очередь
# Состоит из списка блюд с данными о них.

week = [day_1, day_2, day_3, day_4, day_5, day_6, day_7]

for graphic in week:
	graphic_day = (int(graphic[0][2])+int(graphic[1][2])+int(graphic[2][2]))
	graphic_y.append(graphic_day)

# Создания графика для подсчёт калорийности каждого дня в недели.

data = [Bar(x = days, y = graphic_y)]
x_axis_config = {'title': 'Дни'}
y_axis_config = {'title': 'Количество калорий'}
my_layout = Layout(title = f'График калорийности дней',
xaxis = x_axis_config, yaxis = y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename = 'The diet.html')
