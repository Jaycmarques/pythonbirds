from unittest import TestCase
from oo.carro import Motor

class CarroTesteCase(TestCase):
    def test_velocidade_inicial(self):
        motor = Motor()
        self.assertEqual(0, motor.velocidade)
    def test_acelera(self):
        motor = Motor()
        motor.acelerar()
        self.assertEqual(1, motor.velocidade)