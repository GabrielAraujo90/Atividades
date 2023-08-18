class SistemaOperacional:
    def __init__(self, nome, versao):
        self.nome = nome
        self.versao = versao

class Computador:
    def __init__(self, sistema):
        self.sistema = sistema

sistema_windows = SistemaOperacional("Windows", "10")
computador1 = Computador(sistema_windows)

sistema_linux = SistemaOperacional("Linux", "Ubuntu 20.04")
computador2 = Computador(sistema_linux)

print("Computador 1:")
print(f"Sistema Operacional: {computador1.sistema.nome}")
print(f"Versão: {computador1.sistema.versao}")

print("\nComputador 2:")
print(f"Sistema Operacional: {computador2.sistema.nome}")
print(f"Versão: {computador2.sistema.versao}")
