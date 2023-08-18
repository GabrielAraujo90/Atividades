class Autor:
    def __init__(self, nome, data_nascimento):
        self.nome = nome
        self.data_nascimento = data_nascimento

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

# Exemplo de uso
autor1 = Autor("G.A fernanes", "10 Maio de 2002")
livro1 = Livro("Senhores dos Anéis", autor1)

autor2 = Autor("Leonardo Messi", "25 de Maio de 2001")
livro2 = Livro("2007", autor2)

print("Livro 1:")
print(f"Título: {livro1.titulo}")
print(f"Autor: {livro1.autor.nome}")
print(f"Data de Nascimento do Autor: {livro1.autor.data_nascimento}")

print("\nLivro 2:")
print(f"Título: {livro2.titulo}")
print(f"Autor: {livro2.autor.nome}")
print(f"Data de Nascimento do Autor: {livro2.autor.data_nascimento}")
