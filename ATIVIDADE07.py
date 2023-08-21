# Atividade 07
class Documento:
    def __init__(self, titulo, conteudo):
        self.titulo = titulo
        self.conteudo = conteudo

    def exibir(self):
        return f"Título: {self.titulo}, Conteúdo: {self.conteudo}"

class Email(Documento):
    def __init__(self, titulo, conteudo, remetente, destinatario):
        super().__init__(titulo, conteudo)
        self.remetente = remetente
        self.destinatario = destinatario

    def exibir(self):
        return f"Título: {self.titulo}, Conteúdo: {self.conteudo}, Remetente: {self.remetente}, Destinatário: {self.destinatario}"

class Relatorio(Documento):
    def __init__(self, titulo, conteudo, data):
        super().__init__(titulo, conteudo)
        self.data = data

    def exibir(self):
        return f"Título: {self.titulo}, Conteúdo: {self.conteudo}, Data: {self.data}"


doc = Documento("Documento Genérico", "Este é um documento de exemplo.")
print(doc.exibir())


email = Email("Convite", "Venha para a festa!", "remetente@example.com", "destinatario@example.com")
print(email.exibir())


relatorio = Relatorio("Relatório Mensal", "Desempenho das vendas deste mês.", "01/08/2023")
print(relatorio.exibir())
