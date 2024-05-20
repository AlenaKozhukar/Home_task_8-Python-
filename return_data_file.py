from choice_file import choice_number_file


def data_file():
    nf = choice_number_file()
    with open(f'data_{nf}.csv', 'r', encoding='utf-8') as file:
        data = file.readlines()
    return data, nf