def database():
    f = open("day5/ok.txt", 'r')
    _data = f.read()
    _data = _data.split('\n')
    data = [x.split(' ') for x in _data]

    real = [[x for x in j if x != ''] for j in data]
    real[0].insert(0, '----')
    # for x in real:  print(x)

    return real


def relations():
    relationships = {}

    unformatted = database()

    for x in unformatted[1:]:
        for i, item in enumerate(x[1:]):
            relationships[x[0] + '->' + unformatted[0][i+1]] = int(item)

    # print(relationships)
    return relationships



def data():
    f = open("day5/paths.txt", 'r')
    data = f.read()
    data = data.split('\n')
    _data = [x.split(':') for x in data]
    # print(_data)


    f.close()

    for i in _data:
        i[1] = i[1].split('->')
    # print(_data)

    for i in _data:
        relatives = [i[1][x-1].strip() + '->' + i[1][x].strip() for x in range(1, len(i[1]))]
        i[1] = relatives


    # print(_data)



    # print(data[0], stops)
    # print(relatives)
    return [ [y for y in x[1]] for x in _data]




def main():
    relationships = relations()
    distance = 0
    path = data()
    for i in path:
        for j in i:
            distance += relationships[j]
    # print(distance)
    print(relationships)

main()