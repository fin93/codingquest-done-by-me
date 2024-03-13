class Filee:
    def __init__(self, name, size: int):
        self.name = name
        self.size = size
        self.to_remove = "delete" in self.name or "temporary" in self.name


    def get_size(self) -> int:
        return self.size
    
    def to_delete(self) -> int:
        if self.to_remove:  return 1
        else: return 0



class Folder:
    def __init__(self, number=0, files=[]):
        self.number = number
        self.files = files
        self.to_remove = 0




    def set_to_delete(self, delete=0) -> None:
        self.to_remove = delete




class Inputting:
    def __init__(self, filename=''):
        self.filename = filename
        self.relations = {}
        self.open()


    def open(self):
        # relations = {}

        f = open(self.filename, 'r')
        data = f.read().split("Folder:")[1:]

        for i in data:
            self.relations[i[1]] = [x for x in i[2:].split('\n - ') if x != ''] # do not forget the \n at the end of each item


        
        print(self.relations.keys())

    def get_relations(self) -> dict:
        return self.relations 



        






def main():
    folders = []
    data = Inputting('day7/realtext.txt')
    for i, j in data.get_relations().items():
        # folders.append(Folder(int(i), [Filee(x[0], x[1]) for x in j]))
        fine_temp = []
        for x in j:
            temp = x.split(' ')
            fine_temp.append(temp)

        # print(i, j)
        # folders.append(Folder(int(i), [Filee(x[0], int(x[1])) for x in fine_temp if x[1].isdigit()]))
        

    # print(data.get_relations())

    # print(len(folders))




main()