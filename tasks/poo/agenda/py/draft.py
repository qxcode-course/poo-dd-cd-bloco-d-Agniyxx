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
        new_fone = Fone(id, number)
        if new_fone.isValid():
            self.fones.append(new_fone)

    def rmFone(self, index: int):
        if 0 <= index < len(self.fones):
            self.fones.pop(index)

    def toogleFavorited(self):
        self.favorited = not self.favorited

    def isFavoroted(self):
            return self.favorited
        
    def getFones(self):
        return self.fones

    def getNames(self):
        return self.name

    def setNames(self, name: str):
        self.name = name

    def __str__(self):
        fav_str = "@" if self.favorited else "-"
        fones_str = ", ".join(str(f) for f in self.fones)
        return f"{fav_str} [{self.name}, {self.fones_str}]"

class Agenda:
    def __init__(self):
        self.contacts: list[Contact] = []

    def findByName(self, name: str):   
        for i, contact in enumerate(self.contacts):
            if contact.getName() == name:
                return i
            return -1

    def addContact(self, name: str, fones: list[Fone]):
        find = self.findByName(name)
        if find != 1:
            contact_exist = self.contacts[find]
            for fone in fones:
                contact_exist.addFone(fone.getId(), fone.getNumber())
        else:
            new_contact = Contact
        for fone in fones:
            new_contact.addFone(fone.getId(), fone.getNumber())
            self.contacts.append(new_contact)
            self.contacts.sort(key=lambda c: c.getNames())

    def getContact(self, name: str):
        find = self.findByName(name)
        return self.contacts[find] if find != -1 else None

    def rmContact(self, name: str):
        find = self.findByName(name)
        if find != -1:
            self.contacts.pop(find)

    

    



def main():
    while True:
        agenda = Agenda()
    
        line = input()
        print(f"${line}")
        args = line.split()

        if args[0] == "end":
            break
        elif args[0] == "show":
            print(agenda)
        elif args[0] == "add":
            agenda.addContact()
        elif args[0] == "rmFone":
            agenda.rmContact()
        elif args[0] == "tfav":
            agenda.toogleFavorited()
        elif args[0] == "tFav":
            agenda.toogleFavorite()
        
main()
            