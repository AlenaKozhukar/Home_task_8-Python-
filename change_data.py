from return_data_file import data_file


def change_row():
    data, nf = data_file()
    count_rows = len(data)
    number_row = int(input(f"Введите номер строки "
                           f"от 1 до {count_rows}: "))
    while number_row < 1 or number_row > count_rows:
        number_row = int(input(f"Ошибка!"
                               f"Введите номер строки "
                               f"от 1 до {count_rows}: "))
    name = input("Введите свое имя: ")
    surname = input("Введите свою фамилию: ")
    phone = input("Введите номер телефона: ")
    address = input("Введите адрес: ")
    data[number_row - 1] = f'{number_row}; {name}; {surname}; {phone}; {address}\n'
    with open(f'data_{nf}.csv', 'w', encoding='utf-8') as file:
        file.writelines(data)
    print("Данные успешно изменены!")