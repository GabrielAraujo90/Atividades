class Motor:
    def __init__(self, tipo, potencia):
        self.tipo = tipo
        self.potencia = potencia

class Carro:
    def __init__(self, motor):
        self.motor = motor

# Exemplo de uso
motor_gasolina = Motor("Gasolina", 150)
carro1 = Carro(motor_gasolina)

motor_eletrico = Motor("Elétrico", 200)
carro2 = Carro(motor_eletrico)

print("Carro 1:")
print(f"Tipo de Motor: {carro1.motor.tipo}")
print(f"Potência do Motor: {carro1.motor.potencia} cavalos")

print("\nCarro 2:")
print(f"Tipo de Motor: {carro2.motor.tipo}")
print(f"Potência do Motor: {carro2.motor.potencia} cavalos")
