class Memoria:
    def __init__(self, tamanho=256):
        self.tamanho = tamanho
        self.data = [0] * tamanho
    
    def read(self, endereco):
        if 0 <= endereco < self.tamanho: return self.data[endereco]

        raise Exception("Endereco invalido")
    
    def write(self, endereco, valor):
        if 0 <= endereco < self.tamanho:
            self.data[endereco] = valor
            return
        
        raise Exception("Endereco invalido")
    
    def reset(self):
        self.data = [0] * self.tamanho