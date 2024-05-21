class Pessoa():
    def __init__(self, nome = None, idade=35):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        return "Olá"
    
if __name__ == '__main__':
    p = Pessoa('Lucas')
    print(Pessoa.cumprimentar(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Julio'
    print(p.nome)
    print(p.idade)