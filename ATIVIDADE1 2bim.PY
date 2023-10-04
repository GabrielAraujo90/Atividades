class Curso:
    def __init__(self, nome, duracao):
        self.nome = nome
        self.duracao = duracao

    def detalhes_do_curso(self):
        return f"Nome do Curso: {self.nome}\nDuração (anos): {self.duracao}"


class Presencial(Curso):
    def __init__(self, nome, duracao, numero_de_vagas):
        super().__init__(nome, duracao)
        self.numero_de_vagas = numero_de_vagas

    def detalhes_do_curso(self):
        curso_base = super().detalhes_do_curso()
        return f"{curso_base}\nNúmero de Vagas: {self.numero_de_vagas}"


class Online(Curso):
    def __init__(self, nome, duracao, plataforma_online):
        super().__init__(nome, duracao)
        self.plataforma_online = plataforma_online

    def detalhes_do_curso(self):
        curso_base = super().detalhes_do_curso()
        return f"{curso_base}\nPlataforma Online: {self.plataforma_online}"



curso_presencial = Presencial("Curso Presencial de Programação", 2, 30)
curso_online = Online("Curso Online de ciencia da computação", 1, "UNIVALE")

print("Detalhes do Curso Presencial:")
print(curso_presencial.detalhes_do_curso())

print("\nDetalhes do Curso Online:")
print(curso_online.detalhes_do_curso())
