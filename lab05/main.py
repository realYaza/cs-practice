from lab05.tablestats import read_rows, count_types, total_minutes

path = input('Введите путь к файлу: ')

with open(path, encoding = "utf-8") as table:
    rows = read_rows(table)