def get_input():
    f= open("day6/ok.txt", "r")
    data = f.read().split('\n')
    return data[0]


def generate_box(rest="abcdefghiklmnopqrstuvwxyz", x=0):
    key = get_input()
    box = ""
    real_box = []
    for i in key:
        if not i in box:
            box += i
    
    for i in rest:
        if len(box) == 25:  break
        if not i in box:
            box += i

    for i in range(5):
        # print(box[i*5:(i+1)*5])
        real_box.append(box[i*5:(i+1)*5])
    
    if x: return real_box
    return box



def get_pairs():
    f = open("day6/ok.txt", "r")
    data = f.read().split('\n')
    data = data[1].split(' ')
    # print(data)
    return data


def logic(pair, data):
    index_1 = data.index(pair[0])
    index_2 = data.index(pair[1])
    pos_1 = [index_1 // 5, index_1 % 5]
    pos_2 = [index_2 // 5, index_2 % 5]



    if pos_1[0] != pos_2[0] and pos_1[1] != pos_2[1]:
        print('rect')
        # print([pos_1[0], pos_2[1]]) # new pos_1
        newPos1 = [pos_1[0], pos_2[1]]
        # print([pos_2[0], pos_1[1]]) # new pos_2
        newPos2 = [pos_2[0], pos_1[1]]
    
    if pos_1[0] == pos_2[0] and pos_1[1] != pos_2[1]: # horizontal
        print('horiz')
        # print([pos_1[0], (pos_1[1] - 1) % 5])
        newPos1 = [pos_1[0], (pos_1[1] - 1) % 5]
        # print([pos_2[0], (pos_2[1] - 1) % 5])
        newPos2 = [pos_2[0], (pos_2[1] - 1) % 5]

    if pos_1[0] != pos_2[0] and pos_1[1] == pos_2[1]: # vertical
        print('vert')
        # print([(pos_1[0] - 1) % 5, pos_1[1]])
        newPos1 = [(pos_1[0] - 1) % 5, pos_1[1]]
        # print([(pos_2[0] - 1) % 5, pos_2[1]])
        newPos2 = [(pos_2[0] - 1) % 5, pos_2[1]]

    # print(generate_box('abcdefghiklmnopqrstuvwxyz', 1))
    print(generate_box('abcdefghiklmnopqrstuvwxyz', 1)[newPos1[0]][newPos1[1]])
    print(generate_box('abcdefghiklmnopqrstuvwxyz', 1)[newPos2[0]][newPos2[1]])
    return [generate_box('abcdefghiklmnopqrstuvwxyz', 1)[newPos1[0]][newPos1[1]], generate_box('abcdefghiklmnopqrstuvwxyz', 1)[newPos2[0]][newPos2[1]]]



    # print(pos_1)
    # print(pos_2)




# print(generate_box())
print([logic(x, list(generate_box())) for x in get_pairs()])
# logic(['w', 'p'], list(generate_box()))


# please I don't want to talk about how badly I coded this