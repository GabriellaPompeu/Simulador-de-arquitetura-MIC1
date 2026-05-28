class Registrador:
    def __init__(self, nome):
        self.nome = nome
        self.valor = 0

    def read(self):
        return self.valor

    def write(self, valor):
        self.valor = valor
    
    def reset(self):
        self.valor = 0
    
    def __str__(self):
        return f"{self.nome}: {self.valor}"