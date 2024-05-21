class Pessoa():
    def __init__(self, *filhos, nome = None, idade=35):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return "Olá"
    
if __name__ == '__main__':
    lucas = Pessoa(nome='Lucas')
    julio = Pessoa(lucas, nome='Julio')
    print(Pessoa.cumprimentar(lucas))
    print(id(julio))
    print(lucas.cumprimentar())
    print(lucas.nome)
    print(lucas.idade)
    for filho in julio.filhos:
        print(filho.nome)