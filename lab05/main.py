from lab05.tablestats import to_csv


def read_rows(lines):
    headers = []
    res = []
    for line in lines:
        line = line.strip()
        if line != '':
            line = line.split(',')
            if len(headers) == 0:
                headers = [line[0], line[1], line[2]]
            elif len(line) == len(headers):
                res.append({headers[0] : line[0], headers[1] : line[1], headers[2] : line[2]})

    return res


def count_types(rows):
    types = {}
    for row in rows:
        if 'тип' in row:
            type = row['тип']
            types[type] = types.get(type, 0) + 1

    return types



def total_minutes(rows, kind):
    cnt = 0
    for row in rows:
        if row["тип"] == kind:
            try:
                cnt += float(row.get('минуты', '0').replace(',', '.'))
            except ValueError:
                continue #если в минутах текст то не крашнется а просто проигнорит
    return round(cnt, 1)

path = input().strip()

with open(path, encoding = "utf-8") as table:
    rows = read_rows(table)

with open("summary.csv", "w", encoding="utf-8") as out:
    types = len(count_types(rows))
    er_sum= total_minutes(rows, 'ошибка')
    print(f'{len(rows)}' + '\n' + f'{types}' + '\n' + f'{er_sum}')
    out.write(to_csv(count_types(rows)))