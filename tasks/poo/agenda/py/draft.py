class Fone:
    def __init__(self, id: str, number: int):
        self.__id = id
        self.__number = number
        
        def getId(self):

        def getNumber(self):
         


         def __str__(self):
            return f"{self.__id}:{self.__number}"

class Contact:
    def __init__(self, name: str):
        self.name = name
        self.fones = []
        self.isFavorits = False

        def addFone(self, id: str, number: str):

        def rmFone(self, index: int):

        def toogleFavorited(self):

        def isFavoroted(self):


        def __str__(self):
            fones_str = ", ".join(str(f) for f in self.fones)
            return f"{self.name} : {self.fones_str}"

class Agenda(self):
    self.contacts: []

        def addContact(self):

        def getContact(self):
        
        def rmContact(self):
        
        def search(self):
        
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