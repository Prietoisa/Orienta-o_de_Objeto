class Animal:
    def __init__(self, nome, dono):
        self.nome = nome
        self.dono = dono

    def comer(self):
        print("Nhom Nhom", self.nome)

class Gato(Animal):
    def __init__(self, nome, dono, raca):
        super().__init__(nome, dono)
        self.raca = raca
    
    def miar (self):
        print('Minhauuuuu')

class Cachorro(Animal):
    def latir(self, **kwargs):
        print('Au auuuu')

gato = Gato('xuxuzinho','Matheus','siames')
Cachorro = Cachorro('rex', 'Barabara')
Animal = Animal('toddy', 'gabriel')
Cachorro.latir()

print(Cachorro.nome)
print(Cachorro.dono)