import pygame as pg

class MainWindow:
    def __init__(self, cpu):
        pg.init()

        self.cpu = cpu
        self.largura = 1000
        self.altura = 700

        self.tela = pg.display.set_mode((self.largura, self.altura))
        pg.display.set_caption("Meu Little MIC-1")

        self.fonte = pg.font.SysFont("Arial", 24)
        self.clock = pg.time.Clock()

        self.rodando = True

        self.PRETO = (0, 0, 0)
        self.BRANCO = (255, 255, 255)
        self.AZUL = (50, 120, 255)
        self.CINZA = (220, 220, 220)
        self.VERMELHO = (255, 80, 80)
    
    def desenharRegistradores(self):
        x = 50
        y = 50

        for nome, reg in self.cpu.registradores.items():
            pg.draw.rect(self.tela, self.AZUL, (x, y, 250, 40), border_radius=5)

            texto = self.fonte.render(f"{nome}: {reg.read()}", True, self.BRANCO)

            self.tela.blit(texto, (x + 10, y + 5))
            y += 55
        
    def desenharTituloCpu(self):
        titulo = self.fonte.render("Arquitetura MIC-1", True, self.PRETO)
        self.tela.blit(titulo, (350, 20))
    
    def desenharBarramento(self):
        pg.draw.rect(self.tela, self.VERMELHO, (500, 250, 200, 100), border_radius=10)

        textoUla = self.fonte.render("ULA", True, self.BRANCO)
        self.tela.blit(textoUla, (575, 285))

        pg.draw.line(self.tela, self.PRETO, (300, 300), (500, 300), 5)

        pg.draw.line(self.tela, self.PRETO, (700, 300), (900, 300), 5)
    
    def desenharMemoria(self):
        pg.draw.rect(self.tela, self.CINZA, (750, 100, 180, 400), border_radius=10)

        texto = self.fonte.render("MEMÓRIA", True, self.PRETO)
        self.tela.blit(texto, (790, 120))
    
    def desenharBotoes(self):
        pg.draw.rect(self.tela, self.VERMELHO, (450, 600, 120, 50), border_radius=8)

        texto = self.fonte.render("RESET", True, self.BRANCO)
        self.tela.blit(texto, (470, 610))
    
    def cliqueMouse(self, posicao):
        x, y = posicao
        if 450 <= x <= 570 and 600 <= y <= 650: self.cpu.reset()
    
    def renderizar(self):
        self.tela.fill(self.BRANCO)
        
        self.desenharTituloCpu()
        self.desenharRegistradores()
        self.desenharBarramento()
        self.desenharMemoria()
        self.desenharBotoes()

        pg.display.flip()
    
    def rodar(self):
        while self.rodando:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    self.rodando = False
                
                if evento.type == pg.MOUSEBUTTONDOWN:
                    self.cliqueMouse(pg.mouse.get_pos())
            
            self.renderizar()
            self.clock.tick(60)
        pg.quit()