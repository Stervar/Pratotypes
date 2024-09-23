# Пратотип номер (1)

# class Module_Fundamentals_of_Programming_1_1:
#     def __init__(self, module_name, description,version):
#         """
#         Инициализирует модуль с заданными параметрами.

#         Args:
#             module_name (str): Имя модуля
#             description (str): Описание модуля
#             version (str): Номер для вызова
#         """
#         self.module_name = module_name
#         self.description = description
#         self.version = version

#     def print_info(self):
#         """
#         Выводит информацию о модуле в консоль.
#         """
#         print(f"Имя модуля: {self.module_name}")
#         print(f"Описание: {self.description}")
#         print(f"Версия: {self.version}")


# class Module_Fundamentals_of_Programming_1_2:
#     def __init__(self, module_name, description,version,):
#         """
#         Инициализирует модуль с заданными параметрами.

#         Args:
#             module_name (str): Имя модуля
#             description (str): Описание модуля
#             version (str): Номер для вызовая
#         """
#         self.module_name = module_name
#         self.description = description
#         self.version = version

#     def print_info(self):
#         """
#         Выводит информацию о модуле в консоль.
#         """
#         print(f"Имя модуля: {self.module_name}")
#         print(f"Описание: {self.description}")
#         print(f"Номер для вызова: {self.version}")

# def main():
#     """
#     Основная функция программы.
#     """
#     modules = {
#         "Module_Fundamentals_of_Programming_1_1": Module_Fundamentals_of_Programming_1_1(
#             "Module_Fundamentals_of_Programming_1_1",
#             "Это первый модуль",
#             "Автор1",
#             "1.0"
#         ),
#         "Module_Fundamentals_of_Programming_1_2": Module_Fundamentals_of_Programming_1_2(
#             "Module_Fundamentals_of_Programming_1_2",
#             "Это второй модуль",
#             "Автор2",
#             "2.0",
#             ["Зависимость1", "Зависимость2"]
#         ),
  
     
#     }

#     while True:
#         print("Введите номер или имя класса для поиска:")
#         search_input = input("> ")

#         if search_input.lower() == "q":
#             break

#         for module_name, module in modules.items():
#             if search_input in module_name:
#                 print("\nИнформация о модуле:")
#                 module.print_info()
#                 print("\n")
#                 break
#         else:
#             print("Класс не найден. Попробуйте снова.")


# if __name__ == "__main__":
#     main()


## 1. Определение классов

## Определены два класса: Module_Fundamentals_of_Programming_1_1 и Module_Fundamentals_of_Programming_1_2.
## Классы имеют одинаковые методы и атрибуты, но с небольшими различиями в названиях и описаниях.

## 2. Методы классов

## Метод __init__: инициализирует объект класса с заданными параметрами: module_name, description и version.
## Метод print_info: выводит информацию о модуле в консоль.

## 3. Основная функция программы

## Функция main является основной функцией программы.
## В ней определяется словарь modules, который хранит объекты классов Module_Fundamentals_of_Programming_1_1 и Module_Fundamentals_of_Programming_1_2.
## Каждый объект класса инициализируется с заданными параметрами.

## 4. Цикл поиска

## В функции main реализован бесконечный цикл, который позволяет пользователю вводить номер или имя класса для поиска.
## Если пользователь вводит "q", цикл прерывается.
## Если пользователь вводит номер или имя класса, программа ищет соответствующий объект класса в словаре modules.
## Если объект класса найден, программа выводит информацию о модуле с помощью метода print_info.
## Если объект класса не найден, программа выводит сообщение "Класс не найден. Попробуйте снова."

## 5. Запуск программы

## Если файл запускается напрямую (а не импортируется как модуль), функция main вызывается с помощью конструкции if __name__ == "__main__":.























## Пратотип номер (2)



# # Импорт библиотеки для работы с консолью и управления выходом из программы
# import sys

# # Библиотека ASED, где хранятся все модули (Примерная структура)
# ASED_library = {
#     1: {"name": "Python Basics", "description": "Основы Python, циклы и паттерны."},
#     2: {"name": "JavaScript Expressions", "description": "Выражения и операторы в JavaScript."},
#     3: {"name": "HTML Fundamentals", "description": "Основы HTML."},
#     # Добавьте другие модули по мере необходимости
# }

# # Приветственное сообщение для пользователя
# def welcome_message():
#     print("Привет дорогой пользователь, это библиотека ASED!")
#     print("Здесь ты можешь найти информацию по Python, JavaScript и HTML.")
#     print("Выберите один из вариантов ниже для получения информации:")
#     main_menu()

# # Главное меню для выбора языка программирования
# def main_menu():
#     print("\n1) Хочу получить понятия Python")
#     print("2) Хочу получить понятия JavaScript")
#     print("3) Хочу получить понятия HTML")
#     print("4) Выйти из программы")

#     choice = input("\nВыберите опцию (введите номер): ")
#     if choice == "1":
#         module_search_menu("Python")
#     elif choice == "2":
#         module_search_menu("JavaScript")
#     elif choice == "3":
#         module_search_menu("HTML")
#     elif choice == "4":
#         sys.exit()
#     else:
#         print("Неправильный ввод, попробуйте снова.")
#         main_menu()

# # Меню для выбора между поиском по модулю или просмотром всех модулей
# def module_search_menu(language):
#     print(f"\nВы выбрали {language}.")
#     print("1) Ввести модуль вручную")
#     print("2) Ознакомиться со списком всех модулей")
#     print("3) Вернуться к выбору языка")

#     choice = input("\nВыберите опцию (введите номер): ")
#     if choice == "1":
#         manual_module_search(language)
#     elif choice == "2":
#         list_all_modules(language)
#     elif choice == "3":
#         main_menu()
#     else:
#         print("Неправильный ввод, попробуйте снова.")
#         module_search_menu(language)

# # Ввод модуля вручную по названию или номеру
# def manual_module_search(language):
#     module_input = input("\nВведите номер или название модуля: ")
#     if module_input.isdigit():
#         module_num = int(module_input)
#         display_module_info(module_num)
#     else:
#         for num, module in ASED_library.items():
#             if module_input.lower() == module["name"].lower():
#                 display_module_info(num)
#                 return
#         print("Модуль не найден, попробуйте снова.")
#         manual_module_search(language)

# # Вывод всех доступных модулей для выбранного языка
# def list_all_modules(language):
#     print("\nСписок доступных модулей:")
#     for num, module in ASED_library.items():
#         print(f"{num}: {module['name']} - {module['description']}")
#     input("\nНажмите Enter, чтобы вернуться к выбору модуля.")
#     manual_module_search(language) 

# # Функция для отображения информации о выбранном модуле
# def display_module_info(module_num):
#     if module_num in ASED_library:
#         module = ASED_library[module_num]
#         print(f"\nМодуль {module_num}: {module['name']}")
#         print("Описание модуля:")
#         print(module["description"])
#         print("\nПример кода в модуле:")
#         # Пример кода для демонстрации (можно расширять)
#         example_code = "print('Hello, World!')" if module_num == 1 else "console.log('Hello, JavaScript!')"
#         print(f"Пример кода:\n{example_code}")
#         post_module_menu(module_num)
#     else:
#         print("Модуль не найден.")
#         manual_module_search("Python")

# # Меню после отображения информации о модуле
# def post_module_menu(module_num):
#     print("\n1) Полностью выйти")
#     print("2) Найти другой модуль")
#     print("3) Перейти к списку модулей")
#     print("4) Посмотреть другие языки")

#     choice = input("\nВыберите опцию (введите номер): ")
#     if choice == "1":
#         sys.exit()
#     elif choice == "2":
#         manual_module_search("Python")
#     elif choice == "3":
#         list_all_modules("Python")
#     elif choice == "4":
#         main_menu()
#     else:
#         print("Неправильный ввод, попробуйте снова.")
#         post_module_menu(module_num)

# # Запуск программы
# if __name__ == "__main__":
#     welcome_message()

## Объяснение структуры программы: 

## (1) Приветственное сообщение – функция welcome_message() выводит начальное приветствие.

## (2) Главное меню – функция main_menu() позволяет пользователю выбрать язык.

## (3) Поиск модуля – функция module_search_menu() предоставляет выбор между вводом модуля вручную или просмотром всех модулей.

## (4) Ввод модуля – функция manual_module_search() позволяет пользователю искать модуль по названию или номеру.

## (5) Вывод всех модулей – функция list_all_modules() отображает список всех доступных модулей.

## (6) Отображение информации о модуле – функция display_module_info() выводит информацию и пример кода для выбранного модуля.

## (7) Меню после просмотра модуля – функция post_module_menu() позволяет пользователю выбрать дальнейшие действия (выйти, найти другой модуль, вернуться к списку).

## (8) Ты можешь дополнять библиотеку новыми модулями, добавляя их в ASED_library.


















## Пратотип номер (3)









# class Shoe:
#     def __init__(self, gender: str, shoe_type: str, color: str, price: float, manufacturer: str, size: int):
#         """Конструктор для создания объекта обуви с начальными атрибутами."""
#         self.gender = gender            # Пол обуви (мужская или женская)
#         self.shoe_type = shoe_type      # Тип обуви (кроссовки, сапоги и т.д.)
#         self.color = color              # Цвет обуви
#         self.price = price              # Цена обуви
#         self.manufacturer = manufacturer # Производитель обуви
#         self.size = size                # Размер обуви

#     # Методы для изменения атрибутов
#     def set_gender(self, gender: str):
#         """Метод для изменения пола обуви (мужская/женская)."""
#         self.gender = gender

#     def set_shoe_type(self, shoe_type: str):
#         """Метод для изменения типа обуви (кроссовки, сапоги и т.д.)."""
#         self.shoe_type = shoe_type

#     def set_color(self, color: str):
#         """Метод для изменения цвета обуви."""
#         self.color = color

#     def set_price(self, price: float):
#         """Метод для изменения цены обуви."""
#         self.price = price

#     def set_manufacturer(self, manufacturer: str):
#         """Метод для изменения производителя обуви."""
#         self.manufacturer = manufacturer

#     def set_size(self, size: int):
#         """Метод для изменения размера обуви."""
#         self.size = size

#     def get_info(self):
#         """Метод для получения информации об обуви в виде словаря."""
#         return {
#             "Gender": self.gender,
#             "Shoe Type": self.shoe_type,
#             "Color": self.color,
#             "Price": self.price,
#             "Manufacturer": self.manufacturer,
#             "Size": self.size
#         }


# # Библиотека для хранения информации об обуви
# class ShoeLibrary:
#     def __init__(self):
#         """Конструктор для создания объекта библиотеки обуви."""
#         self.shoes = []  # Список для хранения всех записей об обуви

#     def add_shoe(self, shoe: Shoe):
#         """Добавляет объект обуви в библиотеку."""
#         self.shoes.append(shoe)

#     def display_all_shoes(self):
#         """Отображает информацию обо всех парах обуви в библиотеке."""
#         if not self.shoes:
#             print("Библиотека пуста.")
#         else:
#             for idx, shoe in enumerate(self.shoes):
#                 print(f"\nЗапись {idx + 1}:")
#                 shoe_info = shoe.get_info()
#                 for key, value in shoe_info.items():
#                     print(f"{key}: {value}")
#             print("\n")

# # Представление (View)
# class ShoeView:
#     @staticmethod
#     def display_shoe_info(shoe_info: dict):
#         """Отображает информацию об одной паре обуви."""
#         print("Shoe Information:")
#         for key, value in shoe_info.items():
#             print(f"{key}: {value}")


# # Контроллер (Controller)
# class ShoeController:
#     def __init__(self, model: Shoe, view: ShoeView):
#         """Инициализирует контроллер с моделью и представлением."""
#         self.model = model  # Модель обуви
#         self.view = view    # Представление для отображения данных

#     # Методы для изменения данных в модели
#     def set_gender(self, gender: str):
#         """Изменяет пол обуви через модель."""
#         self.model.set_gender(gender)

#     def set_shoe_type(self, shoe_type: str):
#         """Изменяет тип обуви через модель."""
#         self.model.set_shoe_type(shoe_type)

#     def set_color(self, color: str):
#         """Изменяет цвет обуви через модель."""
#         self.model.set_color(color)

#     def set_price(self, price: float):
#         """Изменяет цену обуви через модель."""
#         self.model.set_price(price)

#     def set_manufacturer(self, manufacturer: str):
#         """Изменяет производителя через модель."""
#         self.model.set_manufacturer(manufacturer)

#     def set_size(self, size: int):
#         """Изменяет размер обуви через модель."""
#         self.model.set_size(size)

#     # Метод для отображения информации об обуви
#     def display_shoe_info(self):
#         """Передает информацию модели в представление для отображения."""
#         shoe_info = self.model.get_info()
#         self.view.display_shoe_info(shoe_info)


# # Меню для взаимодействия с пользователем
# def menu(controller: ShoeController, library: ShoeLibrary):
#     while True:
#         print("\n1. Показать информацию об обуви")
#         print("2. Изменить тип обуви")
#         print("3. Изменить цену")
#         print("4. Изменить производителя")
#         print("5. Изменить размер")
#         print("6. Изменить цвет")
#         print("7. Изменить тип (мужская/женская)")
#         print("8. Добавить обувь в список")
#         print("9. Показать всю обувь в списке")
#         print("10. Выйти")

#         choice = input("Выберите опцию: ")

#         if choice == "1":
#             controller.display_shoe_info()
#         elif choice == "2":
#             new_type = input("Введите новый тип обуви: ")
#             controller.set_shoe_type(new_type)
#         elif choice == "3":
#             new_price = float(input("Введите новую цену: "))
#             controller.set_price(new_price)
#         elif choice == "4":
#             new_manufacturer = input("Введите нового производителя: ")
#             controller.set_manufacturer(new_manufacturer)
#         elif choice == "5":
#             new_size = int(input("Введите новый размер: "))
#             controller.set_size(new_size)
#         elif choice == "6":
#             new_color = input("Введите новый цвет: ")
#             controller.set_color(new_color)
#         elif choice == "7":
#             new_gender = input("Введите тип (мужская/женская): ")
#             controller.set_gender(new_gender)
#         elif choice == "8":
#             library.add_shoe(controller.model)
#             print("Обувь добавлена в список.")
#         elif choice == "9":
#             library.display_all_shoes()
#         elif choice == "10":
#             print("Выход...")
#             break
#         else:
#             print("Неверный выбор. Попробуйте снова.")



# # Основной блок программы
# if __name__ == "__main__":
#     # Создаем модель обуви
#     shoe = Shoe(gender="Мужская", shoe_type="Кроссовки", color="Черный", price=100.0, manufacturer="Nike", size=42)

#     # Создаем представление
#     view = ShoeView()

#     # Создаем контроллер
#     controller = ShoeController(model=shoe, view=view)

#     # Создаем библиотеку для хранения всех записей
#     library = ShoeLibrary()

#     # Запускаем меню для взаимодействия
#     menu(controller, library)






























## Класс Shoe (Модель):


## Этот класс описывает данные об одной паре обуви.
## Каждый экземпляр этого класса содержит атрибуты, такие как пол (мужская или женская), тип (кроссовки, сапоги и т.д.), цвет, цена, производитель и размер.


## Методы set_gender, set_shoe_type, set_color, set_price, set_manufacturer, set_size позволяют изменять данные объекта обуви.


## Класс ShoeLibrary:


## Этот класс хранит все созданные записи об обуви.
## Он использует список shoes для хранения объектов обуви.


## Метод add_shoe добавляет новый экземпляр обуви в библиотеку.


## Метод display_all_shoes выводит информацию обо всех парах обуви, хранящихся в библиотеке.


## Класс ShoeView (Представление):

## Этот класс отвечает за отображение информации об обуви. 
## Он получает словарь с данными об обуви и выводит их на экран через метод display_shoe_info.


## Класс ShoeController (Контроллер):


## Контроллер управляет взаимодействием между моделью и представлением.
## Он позволяет изменять данные модели через методы изменения, такие как set_gender, set_shoe_type и т.д.


## Метод display_shoe_info передает данные из модели в представление для отображения.
## Функция menu:


## Предоставляет пользователю интерфейс для взаимодействия с контроллером и библиотекой.
## Опции 1-7 позволяют изменять данные об обуви через контроллер.
## Опция 8 добавляет текущую обувь в библиотеку.
## Опция 9 выводит все записи об обуви, хранящиеся в библиотеке.
## Опция 10 завершает выполнение программы.


## Основной блок программы:
## Здесь создаются объекты модели, представления, контроллера и библиотеки.
## Функция menu предоставляет пользователю меню для изменения данных и работы с библиотекой.








## Пример работы программы:

## 1. Показать информацию об обуви
## 2. Изменить тип обуви
## 3. Изменить цену
## 4. Изменить производителя
## 5. Изменить размер
## 6. Изменить цвет
## 7. Изменить тип (мужская/женская)
## 8. Добавить обувь в библиотеку
## 9. Показать всю обувь в библиотеке
## 10. Выйти
## Выберите опцию: 1
## Shoe Information:
## Gender: Мужская
## Shoe Type: Кроссовки
## Color: Черный
## Price: 100.0
## Manufacturer: Nike
## Size: 42
