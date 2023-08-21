class Publicacao:
    def __init__(self, titulo, ano_publicacao):
        self.titulo = titulo
        self.ano_publicacao = ano_publicacao

    def descricao(self):
        return f"Título: {self.titulo}, Ano de Publicação: {self.ano_publicacao}"

class Livro(Publicacao):
    def __init__(self, titulo, ano_publicacao, autor, numero_paginas):
        super().__init__(titulo, ano_publicacao)
        self.autor = autor
        self.numero_paginas = numero_paginas

    def descricao(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Ano de Publicação: {self.ano_publicacao}, Número de Páginas: {self.numero_paginas}"

class Revista(Publicacao):
    def __init__(self, titulo, ano_publicacao, editora, edicao):
        super().__init__(titulo, ano_publicacao)
        self.editora = editora
        self.edicao = edicao

    def descricao(self):
        return f"Título: {self.titulo}, Editora: {self.editora}, Ano de Publicação: {self.ano_publicacao}, Edição: {self.edicao}"


livro = Livro("O Senhor dos Anéis", 1954, "J.R.R. Tolkien", 1178)
print(livro.descricao())


revista = Revista("National Geographic", 2023, "National Geographic Society", "Agosto")
print(revista.descricao())
