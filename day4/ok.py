

def get_data():
    d = []
    new = []
    total = []
    f = open('day4/why.txt', 'r')
    data = f.read().split('\n')[1:]
    for i in data:
        d.append(i.split('  '))
    
    for i in d:
        new = []
        for j in i:
            if j != '':
                new.append(j.strip())

        total.append(new)

    
    
    
    return total


# print(get_data())
    
# get_data()
    


def main():
    data = get_data()
    di = {}
    for i in data:
        di[i[0]] = list(map(float, i[1:]))
        # print(i[1:])

    minimum = 100000000000000000000000000

    for i, j in di.items():
        for k, z in di.items():
            # distance = sum(list(map(lambda x: x**2, [j[0] - z[0], j[1] - z[1], j[2] - z[2]]))) ** 0.5
            squares = [j[1] - z[1], j[2] - z[2], j[3] - z[3]]
            newsquares = [x ** 2 for x in squares]
            distance = sum(newsquares) ** 0.5
                
            if distance < minimum and distance:
                minimum = distance
    print(minimum)

main()