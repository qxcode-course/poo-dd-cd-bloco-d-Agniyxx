class Fone:
    def __init__(self, nome: str, fone: int):
        self.__nome = nome
        self.__numero = fone

        def __str__(self):
            return f"{self.__nome}:{self.__numero}"

class Contact:
    def __init__(self):
        self.favoritos: Fone | None = []


class Agenda(self):
    


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