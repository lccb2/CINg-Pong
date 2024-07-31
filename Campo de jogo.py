import pygame
from pygame import QUIT


class Mesa_ping_pong:
    pygame.init()

    altura = 800
    largura = 1500

    tela = pygame.display.set_mode((largura, altura))

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
        pygame.draw.rect(tela, (0,0,255),(150,100,1200,600))
        pygame.draw.line(tela,(255,255,255),(150,100),(150,700),5)
        pygame.draw.line(tela, (255, 255, 255), (150, 100), (1350, 100), 5)
        pygame.draw.line(tela, (255, 255, 255), (150, 700), (1350, 700), 5)
        pygame.draw.line(tela, (255, 255, 255), (1350, 100), (1350, 700), 5)
        pygame.draw.line(tela,(0,0,0), (748,100), (748,700), 7)
        pygame.draw.line(tela, (0, 0, 0), (752, 100), (752, 700), 7)
        pygame.draw.line(tela, (255,255,255), (750,100), (750,700), 5)
        pygame.draw.line(tela,(255,165,0),(152,400),(747,400), 3)
        pygame.draw.line(tela, (255, 165, 0), (753, 400), (1348, 400), 3)


        pygame.display.update()

