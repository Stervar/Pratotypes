# # Пратотип номер (1)

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




# Пратотип номер (2)



# Импорт библиотеки для работы с консолью и управления выходом из программы
import sys

# Библиотека ASED, где хранятся все модули (Примерная структура)
ASED_library = {
    1: {"name": "Python Basics", "description": "Основы Python, циклы и паттерны."},
    2: {"name": "JavaScript Expressions", "description": "Выражения и операторы в JavaScript."},
    3: {"name": "HTML Fundamentals", "description": "Основы HTML."},
    # Добавьте другие модули по мере необходимости
}

# Приветственное сообщение для пользователя
def welcome_message():
    print("Привет дорогой пользователь, это библиотека ASED!")
    print("Здесь ты можешь найти информацию по Python, JavaScript и HTML.")
    print("Выберите один из вариантов ниже для получения информации:")
    main_menu()

# Главное меню для выбора языка программирования
def main_menu():
    print("\n1) Хочу получить понятия Python")
    print("2) Хочу получить понятия JavaScript")
    print("3) Хочу получить понятия HTML")
    print("4) Выйти из программы")

    choice = input("\nВыберите опцию (введите номер): ")
    if choice == "1":
        module_search_menu("Python")
    elif choice == "2":
        module_search_menu("JavaScript")
    elif choice == "3":
        module_search_menu("HTML")
    elif choice == "4":
        sys.exit()
    else:
        print("Неправильный ввод, попробуйте снова.")
        main_menu()

# Меню для выбора между поиском по модулю или просмотром всех модулей
def module_search_menu(language):
    print(f"\nВы выбрали {language}.")
    print("1) Ввести модуль вручную")
    print("2) Ознакомиться со списком всех модулей")
    print("3) Вернуться к выбору языка")

    choice = input("\nВыберите опцию (введите номер): ")
    if choice == "1":
        manual_module_search(language)
    elif choice == "2":
        list_all_modules(language)
    elif choice == "3":
        main_menu()
    else:
        print("Неправильный ввод, попробуйте снова.")
        module_search_menu(language)

# Ввод модуля вручную по названию или номеру
def manual_module_search(language):
    module_input = input("\nВведите номер или название модуля: ")
    if module_input.isdigit():
        module_num = int(module_input)
        display_module_info(module_num)
    else:
        for num, module in ASED_library.items():
            if module_input.lower() == module["name"].lower():
                display_module_info(num)
                return
        print("Модуль не найден, попробуйте снова.")
        manual_module_search(language)

# Вывод всех доступных модулей для выбранного языка
def list_all_modules(language):
    print("\nСписок доступных модулей:")
    for num, module in ASED_library.items():
        print(f"{num}: {module['name']} - {module['description']}")
    input("\nНажмите Enter, чтобы вернуться к выбору модуля.")
    manual_module_search(language)

# Функция для отображения информации о выбранном модуле
def display_module_info(module_num):
    if module_num in ASED_library:
        module = ASED_library[module_num]
        print(f"\nМодуль {module_num}: {module['name']}")
        print("Описание модуля:")
        print(module["description"])
        print("\nПример кода в модуле:")
        # Пример кода для демонстрации (можно расширять)
        example_code = "print('Hello, World!')" if module_num == 1 else "console.log('Hello, JavaScript!')"
        print(f"Пример кода:\n{example_code}")
        post_module_menu(module_num)
    else:
        print("Модуль не найден.")
        manual_module_search("Python")

# Меню после отображения информации о модуле
def post_module_menu(module_num):
    print("\n1) Полностью выйти")
    print("2) Найти другой модуль")
    print("3) Перейти к списку модулей")
    print("4) Посмотреть другие языки")

    choice = input("\nВыберите опцию (введите номер): ")
    if choice == "1":
        sys.exit()
    elif choice == "2":
        manual_module_search("Python")
    elif choice == "3":
        list_all_modules("Python")
    elif choice == "4":
        main_menu()
    else:
        print("Неправильный ввод, попробуйте снова.")
        post_module_menu(module_num)

# Запуск программы
if __name__ == "__main__":
    welcome_message()

