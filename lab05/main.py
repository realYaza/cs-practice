from lab05.tablestats import read_rows

path = input('Введите путь к файлу: ')

with open(path, encoding = "utf-8") as table:
    rows = read_rows(table)
    print(rows)