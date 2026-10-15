from lab05.tablestats import read_rows, count_types, total_minutes

path = input('Введите путь к файлу: ')

with open(path, encoding = "utf-8") as table:
    rows = read_rows(table)

with open("summary.csv", "w", encoding="utf-8") as out:
    types = len(count_types(rows))
    er_sum= total_minutes(rows, 'ошибка')

    out.write(f'{len(rows)}' + '\n' + f'{types}' + '\n' + f'{er_sum}')