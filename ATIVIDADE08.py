#Atividade 08

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        desconto_valor = self.preco * percentual / 100
        novo_preco = self.preco - desconto_valor
        return novo_preco

class Livro(Produto):
    def __init__(self, nome, preco, autor):
        super().__init__(nome, preco)
        self.autor = autor

    def desconto(self, percentual):
        desconto_geral = super().desconto(percentual)
        desconto_livro = desconto_geral * 0.1  # 10% de desconto adicional
        novo_preco = desconto_geral - desconto_livro
        return novo_preco

class Jogo(Produto):
    def __init__(self, nome, preco, plataforma):
        super().__init__(nome, preco)
        self.plataforma = plataforma


produto = Produto("Produto Genérico", 100)
print(f"Preço original do produto: R${produto.preco:.2f}")
desconto_valor = produto.desconto(20)
print(f"Preço com desconto: R${desconto_valor:.2f}")


livro = Livro("Aventura Fantástica", 50, "Autor Desconhecido")
print(f"Preço original do livro: R${livro.preco:.2f}")
desconto_valor_livro = livro.desconto(15)
print(f"Preço do livro com desconto: R${desconto_valor_livro:.2f}")


jogo = Jogo("Fantasia Épica", 60, "PS5")
print(f"Preço original do jogo: R${jogo.preco:.2f}")
desconto_valor_jogo = jogo.desconto(10)
print(f"Preço do jogo com desconto: R${desconto_valor_jogo:.2f}")
