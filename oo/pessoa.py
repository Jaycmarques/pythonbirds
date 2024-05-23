class Pessoa():
    olhos = 2 #atributo de classe, pode ser acessado pela classe diretamente

    def __init__(self, *filhos, nome = None, idade=35):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return "Olá"
    
class Homem(Pessoa):
    pass

class Mutante(Pessoa):
    olhos = 4

    
if __name__ == '__main__':
    lucas = Mutante(nome='Lucas')
    julio = Homem(lucas, nome='Julio')
    print(Pessoa.cumprimentar(lucas))
    print(id(julio))
    print(lucas.cumprimentar())
    print(lucas.nome)
    print(lucas.idade)
    for filho in julio.filhos:
        print(filho.nome)
    julio.sobrenome = 'Marques'
    del julio.filhos
    julio.olhos = 1
    del julio.olhos
    print(julio.__dict__)
    print(lucas.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(julio.olhos)
    print(lucas.olhos)
    