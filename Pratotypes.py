

class Module_Fundamentals_of_Programming_1_1:
    def __init__(self, module_name, description,version):
        """
        Инициализирует модуль с заданными параметрами.

        Args:
            module_name (str): Имя модуля
            description (str): Описание модуля
            version (str): Номер для вызова
        """
        self.module_name = module_name
        self.description = description
        self.version = version

    def print_info(self):
        """
        Выводит информацию о модуле в консоль.
        """
        print(f"Имя модуля: {self.module_name}")
        print(f"Описание: {self.description}")
        print(f"Версия: {self.version}")


class Module_Fundamentals_of_Programming_1_2:
    def __init__(self, module_name, description,version,):
        """
        Инициализирует модуль с заданными параметрами.

        Args:
            module_name (str): Имя модуля
            description (str): Описание модуля
            version (str): Номер для вызовая
        """
        self.module_name = module_name
        self.description = description
        self.version = version

    def print_info(self):
        """
        Выводит информацию о модуле в консоль.
        """
        print(f"Имя модуля: {self.module_name}")
        print(f"Описание: {self.description}")
        print(f"Номер для вызова: {self.version}")

def main():
    """
    Основная функция программы.
    """
    modules = {
        "Module_Fundamentals_of_Programming_1_1": Module_Fundamentals_of_Programming_1_1(
            "Module_Fundamentals_of_Programming_1_1",
            "Это первый модуль",
            "Автор1",
            "1.0"
        ),
        "Module_Fundamentals_of_Programming_1_2": Module_Fundamentals_of_Programming_1_2(
            "Module_Fundamentals_of_Programming_1_2",
            "Это второй модуль",
            "Автор2",
            "2.0",
            ["Зависимость1", "Зависимость2"]
        ),
  
     
    }

    while True:
        print("Введите номер или имя класса для поиска:")
        search_input = input("> ")

        if search_input.lower() == "q":
            break

        for module_name, module in modules.items():
            if search_input in module_name:
                print("\nИнформация о модуле:")
                module.print_info()
                print("\n")
                break
        else:
            print("Класс не найден. Попробуйте снова.")


if __name__ == "__main__":
    main()