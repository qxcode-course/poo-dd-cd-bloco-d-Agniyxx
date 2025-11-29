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

    def isFavorited(self):
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
        return f"{fav_str} [{self.name}, {fones_str}]"

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
    
    def search(self, pattern: str):
        results: list[Contact] = []
        pattern_lower = pattern.lower()

        for contact in self.contacts:
            contact_str_lower = str(contact).lower()
            if pattern_lower in contact_str_lower:
                results.append(contact)
        return results

    def getFavorite(self):
        return [contact for contact in self.contacts if contact.isFaviroted()]
    
    def getContacts(self):
        return self.contacts
    
    def __str__(self):
        return f"\n".join(str(contact) for contact in self.contacts)

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
        elif args[0] == "rmFone":
            agenda.rmContact()
        elif args[0] == "tfav":
            agenda.toogleFavorited()
        elif args[0] == "tFav":
            agenda.toogleFavorite()
        
main()
            