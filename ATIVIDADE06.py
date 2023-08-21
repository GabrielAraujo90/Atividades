#Atividade 06

# A composição é um conceito fundamental na programação orientada a objetos (POO), onde um objeto é construído pela combinação de outros objetos. 
# Em vez de herdar propriedades e comportamentos de uma classe base, um objeto usa instâncias de outras classes para cumprir suas responsabilidades. 
# Isso promove o reuso de código e permite que as classes sejam mais modularizadas e flexíveis.

# Exemplo 1 
# Neste exemplo, temos duas classes, Motor e Carro, onde um objeto Carro é composto por um objeto Motor. 
# O carro não herda do motor, mas tem um motor como uma parte essencial.

class Motor:
    def __init__(self, tipo):
        self.tipo = tipo

    def ligar(self):
        print(f"Motor {self.tipo} ligado")

    def desligar(self):
        print(f"Motor {self.tipo} desligado")

class Carro:
    def __init__(self, marca, modelo, tipo_motor):
        self.marca = marca
        self.modelo = modelo
        self.motor = Motor(tipo_motor)

    def ligar(self):
        print(f"{self.marca} {self.modelo} ligado")
        self.motor.ligar()

    def desligar(self):
        print(f"{self.marca} {self.modelo} desligado")
        self.motor.desligar()

carro_gasolina = Carro("Toyota", "Corolla", "gasolina")
carro_gasolina.ligar()
carro_gasolina.desligar()

############################################################################################
# Exemplo 2
# Neste exemplo, temos uma classe Autor e uma classe Livro, onde um objeto Livro é composto por um ou mais objetos Autor.

class Autor:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

class Livro:
    def __init__(self, titulo, autores):
        self.titulo = titulo
        self.autores = autores  

    def exibir_autores(self):
        nomes_autores = [f"{autor.nome} {autor.sobrenome}" for autor in self.autores]
        return ", ".join(nomes_autores)


autor1 = Autor("J.K.", "Rowling")
autor2 = Autor("J.R.R.", "Tolkien")

livro = Livro("O Senhor dos Anéis", [autor1, autor2])
print(f"{livro.titulo} - Autores: {livro.exibir_autores()}")
