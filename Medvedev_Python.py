import time


class Algoritms(object):

	def vvod_info_int(self):
		"""Этот метод реализует проверку числа"""
		time.sleep(1)
		condition = True 
		while condition:
			try:
				vvod_int = int(input("Введите целое число: "))
				if vvod_int > 7:
					print("Привет")
					condition = False
				elif vvod_int == 7:
					print("Введенное вами число равно \"7\", необходимо ввести число выше!")
				else:
					print("Введенное вами число меньше \"7\", необходимо ввести число выше 7!")
			except ValueError:
				print("Вы ввели не целое число!")
			
	def vvod_info_name(self):
		"""Этот метод реализует проверку имени (без учета регистра)"""
		time.sleep(1)
		condition = True
		while condition:
			vvod_name = input("Введите Имя: ")
			if vvod_name == "Вячеслав" or vvod_name == "вячеслав":
				print(f"Привет, {vvod_name}")
				condition = False
			else:
				print("Нет такого имени")

	def vvod_info_array(self):
		"""Этот метод риализует проверку массива и выбирает те элементы, которые кратны 3 (исключает дубликаты)"""
		time.sleep(1)
		try:
			vvod_mass = input("Введите элементы массива через пробел: ")
			main_mass = []
			result = []
			if " " in vvod_mass or len(vvod_mass) != 0:
				vvod_mass = vvod_mass.split(" ")
				for i in vvod_mass:
					main_mass.append(int(i))
				for j in main_mass:
					if j % 3 == 0:
						if j not in result:
							result.append(j)
				if len(result) == 0:
					print("В введенном вами массиве отсутствуют элементы кратные '3'")
				else:
					print(f"Элементы массива кратные '3': {tuple(result)}") 
			else:
				print("Вы ввели не массив!")
		except ValueError:
			print("Вы неправильно ввели массив!")

def main():
	try:
		input("Нажмите любую клавишу для начала работы ...")
		run = Algoritms() #создание экземпляра класса
		print("Задание 1")
		run.vvod_info_int() #вызов метода vvod_info_int 
		print("Задание 2")
		run.vvod_info_name() #вызов метода vvod_info_name
		print("Задание 3")
		run.vvod_info_array() #вызов метода vvod_info_array
		input("Для выхода нажмите любую клавишу...")
		print("Спасибо за внимание!")
		time.sleep(3)
	except KeyboardInterrupt:
		print("Ожидается принудительный выход из программы...")
		time.sleep(2)

if __name__ == "__main__":
	main() #вызов основной функции main в главном модуле
