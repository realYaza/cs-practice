def read_rows(lines):
    headers = []
    res = []
    for line in lines:
        line = line.strip() #убирает пробелы
        if line != '':  #проверка не пустая ли строка
            line = line.split(',') #разбивает строку на список по запятым
            line = [q.strip() for q in line] #генератором списком убирает пробелы в каждом элементе (на случай дата , тип.....)
            if len(headers) == 0: #проверка не нашли ли мы заголовок
                headers = line #если не нашли, то первая не пустая строка становится им
            elif len(line) == len(headers): #если длина строки совпадает с заголовком
                res.append({headers[0] : line[0], headers[1] : line[1], headers[2] : line[2]}) #добавление словаря в список

    return res


def count_types(rows):
    types = {}
    for row in rows: #проходимся по списку из словарей
        if 'тип' in row: #присутсвует ли ключ "тип" в словаре
            type = row['тип'] #какой тип у нашего словаря ({тип: ошибка} -- ошибка и есть наш тип)
            types[type] = types.get(type, 0) + 1 #проверяет если в словаре такой тип, если нет, то создаёт, и даём ему значение 0, и прибавляет 1
    return types


def total_minutes(rows, kind):
    cnt = 0
    for row in rows: #проходимся по списку из словарей
        if row["тип"] == kind: #если тип  соответсвует нашему
            try:
                cnt += float(row.get('минуты', '0').replace(',', '.')) #пробует в cnt прибавить кол-во минут
            except ValueError: #если выдаёт ошибку, значит что в минутах написан текст
                continue #не крашнется а просто проигнорит

    return round(cnt, 1)

def to_csv(counts):
    res = sorted( [(key, value) for key, value in counts.items()] ) #создаёт отсортированный по алфавиту список список типа [(ключ1, значение1), (....]
    lines = ['тип,количество']
    for q in res: #проходимся по отсортированному списку
        lines.append(f'{q[0]},{q[1]}') #добавляет в список строку типа "тип, количество

    return '\n'.join(lines) + '\n' #'\n' это перевести на след. строчку курсор, join(lines) - соединяет все строки в списке в одну большую

path = input().strip()

with open(path, encoding = "utf-8") as table: #открывает файл по ранее указанному пути в кодировке utf-8, чтобы открывалось везде, и на винде и на линуксе
    rows = read_rows(table)

with open("summary.csv", "w", encoding="utf-8") as out: #записываем в summary что просят
    types = len(count_types(rows))
    er_sum= total_minutes(rows, 'ошибка')
    print(f'{len(rows)}' + '\n' + f'{types}' + '\n' + f'{er_sum}')
    out.write(to_csv(count_types(rows)))