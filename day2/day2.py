


def read_file(filename):
    f = open(f'{filename}.txt', 'r')
    data = f.read()
    data = data.split('\n')
    f.close()
    return data

#  internal ship systems are in the 192.168.0.0 through to 192.168.254.254 

# passenger wifi is on the 10.0.0.0 to 10.0.254.254 IP

# Any other addresses are external to the ship 

data = read_file("what")


print(int(f"0x{data[0]}", 16))

totalpassenger = 0
totalinternal = 0

for ok in data:
    temp = []
    length = int(ok[4:8], 16)
    for i in range(1, len(ok), 2):
        bytes = int(f"0x{ok[i-1:i+1]}", 16)
        temp.append(bytes)
        

    numer = ''
    for i in str(temp[12:16]).split(','):
        numer += i
    

    number = str(numer[1:-1].replace(' ', ''))

    numer = ''
    for i in str(temp[16:]).split(','):
        numer += i
    number2 = str(numer[1:-1].replace(' ', ''))

    # print(number[:3])
    if number[:3] == '192':
        totalinternal += length

    if number[:3] == '100':
    # else:
        totalpassenger += length





        
        
    # print(temp[16:])

        # print(int(f"0x{ok[i-1:i+1]}", 16), end= " ")
    # print()


print(f"{totalinternal }/{totalpassenger}")
# print(totalpassenger)