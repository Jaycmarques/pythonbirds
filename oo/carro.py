class Motor:
    def __init__(self, velocidade=0):
        self.velocidade = velocidade

    def acelerar(self):
        self.velocidade += 1
        return f"Motor acelerando. Velocidade atual: {self.velocidade} km/h."

    def frear(self):
        self.velocidade = max(0, self.velocidade - 2)  # Garantir que a velocidade não seja negativa
        return f"Motor freando. Velocidade atual: {self.velocidade} km/h."

class Direcao:
    def __init__(self, coordenada):
        self.coordenada = coordenada

    def girar_direita(self):
        coordenadas = ['N', 'L', 'S', 'O']
        nova_coordenada = coordenadas[(coordenadas.index(self.coordenada) + 1) % 4]
        self.coordenada = nova_coordenada
        return f"Direção virada para  {self.coordenada}."

    def girar_esquerda(self):
        coordenadas = ['N', 'O', 'S', 'L']
        nova_coordenada = coordenadas[(coordenadas.index(self.coordenada) + 1) % 4]
        self.coordenada = nova_coordenada
        return f"Direção virada para  {self.coordenada}."

class Carro:
    def __init__(self, motor=0, direcao='N'):
        self.motor = Motor(motor)
        self.direcao = Direcao(direcao)

    def acelerar_carro(self):
        return self.motor.acelerar()

    def frear_carro(self):
        return self.motor.frear()

    def virar_direita(self):
        return self.direcao.girar_direita()

    def virar_esquerda(self):
        return self.direcao.girar_esquerda()

# Exemplo de uso
meu_carro = Carro(0, 'N')
print(meu_carro.acelerar_carro())
print(meu_carro.acelerar_carro())
print(meu_carro.frear_carro())
print(meu_carro.virar_direita())
print(meu_carro.virar_esquerda())
print(meu_carro.frear_carro())
