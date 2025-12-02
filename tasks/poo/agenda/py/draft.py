def _fones(fones_args: list[str]):
        fones: list[Fone] = []
        for fone_arg in fones_args:
            parts = fone_arg.split(':', 1)
            if len(parts) == 2:
                fones.append(Fone(parts[0], parts[1]))
        return fones
    
class Fone:
    def __init__(self, id: str, number: str):
        self.__id = id
        self.__number = number
        
    def getId(self):
        return self.__id

    def getNumber(self):
        return self.__number
    
    def isValid(self):
        valid = "0123456789"
        for c in self.__number:
            if c not in valid:
                return False
        return True

    def __str__(self):
        return f"{self.__id}:{self.__number}"

class Contact:
    def __init__(self, name: str):
        self.name = name
        self.fones: list[Fone] = []
        self.favorits = False

    def addFone(self, id: str, number: str):
        new_fone = Fone(id, number)
        if new_fone.isValid():
            self.fones.append(new_fone)

    def rmFone(self, index: int):
        if 0 <= index < len(self.fones):
            self.fones.pop(index)

    def toogleFavorited(self):
        self.favorits = not self.favorits

    def isFavorited(self):
        return self.favorits
        
    def getFones(self):
        return self.fones

    def getName(self):
        return self.name

    def setName(self, name: str):
        self.name = name

    def __str__(self):
        fav_str = "@" if self.favorits else "-"
        fones_str = ", ".join(str(f) for f in self.fones)
        return f"{fav_str} {self.name} [{fones_str}]"

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
        if find != -1:
            contact_exist = self.contacts[find]
            for fone in fones:
                contact_exist.addFone(fone.getId(), fone.getNumber())
        else:
            new_contact = Contact(name)
            for fone in fones:
                new_contact.addFone(fone.getId(), fone.getNumber())
            return
        
        new_contact = Contact(name)
        for fone in fones:
            new_contact.addFone(fone.getId(), fone.getNumber())

        self.contacts.append(new_contact)
        self.contacts.sort(key=lambda c: c.getName())

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
        return [contact for contact in self.contacts if contact.isFavorited()]
    
    def getContacts(self):
        return self.contacts
    
    def __str__(self):
        return f"\n".join(str(contact) for contact in self.contacts)

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
        elif args[0] == "add":
            name = args[1]
            fones_list = _fones(args[2:])
            agenda.addContact(name, fones_list)
        elif args[0] == "rmFone": 
            contact = agenda.getContact(name)
            name = args[1]
            index = int(args[2])
            agenda.rmFone(contact)
        elif args[0] == "rm":
            contact = agenda.getContact(name)
            name = args[1]
            contact.rmContact(name)
        elif args[0] == "search":
            pattern = args[1]
            results = agenda.search(pattern) 
        elif args[0] == "tfav":
            name = args[1]
            contact = agenda.getContact(name)
            contact.toogleFavorited()
        elif args[0] == "favs":
            fav = agenda.getFavorite()
        else:
            print("fail: comando inválido")
        
main()        