import pygame
from sys import exit

class Bola:
    def __init__(self, win, x, y, raio, velocidade):
        self.win = win
        self.x = x
        self.y = y
        self.raio = raio
        self.velocidade = velocidade
        self.xcord = 1
        self.ycord = 1
        self.cor = (255, 255, 255)

    def draw(self):
        pygame.draw.circle(
            self.win,
            self.cor,
            (self.x, self.y),
            self.raio
        )
    
    def move(self):
        self.x += self.velocidade * self.xcord
        self.y += self.velocidade * self.ycord

        if self.x - self.raio < 0 or self.x + self.raio > self.win.get_width():
            self.xcord *= -1
        if self.y - self.raio < 0 or self.y + self.raio > self.win.get_height():
            self.ycord *= -1
        
        
pygame.init()
tela = pygame.display.set_mode((800, 600))
bola = Bola(tela, 400, 300, 5, 0.05)  

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT()
            exit()

    bola.move()
    tela.fill((40, 40, 40))
    bola.draw()


    pygame.display.flip()

pygame.quit()
exit()
