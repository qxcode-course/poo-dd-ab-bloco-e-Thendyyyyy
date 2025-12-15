from abc import ABC, abstractmethod;

class Animal(ABC):
    def __init__(self, name:str, ):
        self.name = name;

    def __str__(self):
        return f"{self.name}";

    def apresentar_nome(self):
        print(f"Eu sou um(a) {self.name}!")

    @abstractmethod
    def fazer_Som(self):
        pass;

    @abstractmethod
    def Mover(self):
        pass;

class Leão(Animal):
    def __init__(self, name):
        super().__init__(name);

    def fazer_Som(self):
        print("roaaaaaar!");

    def Mover(self):
        print("O leão caminha pela savana.");

class Falcão(Animal):
    def __init__(self, name):
        super().__init__(name);

    def fazer_Som(self):
        print("Hawk tuah!");

    def Mover(self):
        print("O falcão voa pelos ares.");

class Dinossauro(Animal):
    def __init__(self, name):
        super().__init__(name);

    def fazer_Som(self):
        print("               ");

    def Mover(self):
        print("O dinossauro permanece exposto num museu.");

def Apresentar(animal: Animal):
    animal.apresentar_nome();
    animal.fazer_Som();
    animal.Mover();
    print(f"Tipo do animal: {type(animal).__name__}");
    print("-" * 30);

def main():
    animais = [
        Leão("leão"),
        Falcão("falcão"),
        Dinossauro("T-Rex")
    ];

    for animal in animais:
        Apresentar(animal);

main();