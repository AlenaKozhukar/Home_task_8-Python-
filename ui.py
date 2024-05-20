from print_data import print_file
from add_data import add_row
from change_data import change_row
from delete_data import delete_row


def check_number(n):
    while n < 1 or n > 4:
        n = int(input("Ошибка, такого номера команды не "
                      "существует! Введите цифру от 1 до 4\n"
                      "Выберите функцию:\n"
                      "1. Добавить\n"
                      "2. Удалить\n"
                      "3. Изменить\n"
                      "4. Вывод\n"
                      "Введите номер команды: "))
    return n


def interface():
    command = int(input("Добрый день! Вы попали на специальный бот-справочник от GeekBrains!\n"
                        "Выберите функцию:\n"
                        "1. Добавить\n"
                        "2. Удалить\n"
                        "3. Изменить\n"
                        "4. Вывод\n"
                        "Введите номер команды: "))
    command = check_number(command)
    if command == 1:
        add_row()
    elif command == 2:
        delete_row()
    elif command == 3:
        change_row()
    elif command == 4:
        print_file()