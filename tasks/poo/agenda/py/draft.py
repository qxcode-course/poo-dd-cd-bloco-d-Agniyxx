class Fone:
    def __init__(self, id: str, number: int):
        self.__id = id
        self.__number = number
        
        def getId(self):
            return self.__id

        def getNumber(self):
            return self.__number

        def __str__(self):
            return f"{self.__id}:{self.__number}"

class Contact:
    def __init__(self, name: str):
        self.name = name
        self.fones: list[Fone] = []
        self.isFavorits = False

        def addFone(self, id: str, number: str):
            new_fone = Fone(id, number):
            if new_fone.isValid():
                self.fones.append(new_fone)

        def rmFone(self, index: int):
            if 0 <= index < len(self.fones):
                self.fones.pop(index)

        def toogleFavorited(self):



        def isFavoroted(self):



        def __str__(self):
            fones_str = ", ".join(str(f) for f in self.fones)
            return f"{self.name} : {self.fones_str}"

class Agenda:
    def __init__(self):
        self.contacts: list[Contact] = []

        def addContact(self, name: str, fones: list[Fone]):

        def getContact(self, name: str):
        
        def rmContact(self, nsme: str):
        
        def search(self, pattern: str):
        
        def getFavorited(self):
        
        def getContacts(self):
        
        def __str__(self):
    


def main():
    agenda = Agenda()
    while True:
        line = input()
        print(f"${line}")
        args = line.split()

        if args[0] == "end":
            break
        elif args[0] == "show":
            print(agenda)
        elif args[0] == "rmFone":
            agenda.removeFone()
        elif args[0] == "rm":
            agenda.remove()
        elif args[0] == "tFav":
            agenda.toogleFavorite()
            