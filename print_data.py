def print_file():
    for i in range(1, 3):
        with open(f'data_{i}.csv', 'r', encoding='utf-8') as file:
            data = file.readlines()
        print(f"Вывод данных из {i}-ого файла:\n"
              f"{''.join(data)}")
        print()