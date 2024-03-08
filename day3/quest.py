def data():
    f = open('day3/j.txt', 'r')
    data = f.read().split(' ')
    return list(map(int, data))



ok = ''
print(data())



for i, j in enumerate(data()):
    print(i, j)
    if not i % 2:
        ok += '.' * j
    else:
        ok += '#' * j


for i, j in enumerate(ok):
    if not i % 100:
        print()

    print(j,end='')