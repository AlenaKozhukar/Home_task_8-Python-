from return_data_file import data_file


def add_row():
    name = input("Введите имя: ")
    surname = input("Введите фамилию: ")
    phone = input("Введите номер телефона: ")
    address = input("Введите адрес: ")
    data, nf = data_file()
    now_number_row = len(data) + 1
    with open(f'data_{nf}.csv', 'a', encoding='utf-8') as file:
        file.write(f'{now_number_row}; {name}; '
                   f'{surname}; {phone}; {address}\n')
    print("Данные успешно записаны!")