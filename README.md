#aumento boneco coletavel
import pygame

pygame.init()


LARGURA_TELA = 800

ALTURA_TELA = 600

tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))

pygame.display.set_caption("Ping Pong")


TAMANHO_QUADRADO = 200  # Aumentado o tamanho do quadrado

VELOCIDADE = 5


imagem1 = pygame.image.load("imagem1.png")

imagem2 = pygame.image.load("imagem2.png")


imagem1 = pygame.transform.scale(imagem1, (TAMANHO_QUADRADO, TAMANHO_QUADRADO))

imagem2 = pygame.transform.scale(imagem2, (TAMANHO_QUADRADO, TAMANHO_QUADRADO))


class Player:

    def __init__(self, x, y, image, controls):

        self.x = x

        self.y = y

        self.image = image

        self.controls = controls


    def draw(self, tela):

        tela.blit(self.image, (self.x, self.y))


    def move(self, keys):

        if keys[self.controls['cima']]:

            self.y -= VELOCIDADE

        if keys[self.controls['baixo']]:

            self.y += VELOCIDADE

        if keys[self.controls['esquerda']]:

            self.x -= VELOCIDADE

        if keys[self.controls['direita']]:

            self.x += VELOCIDADE


        if self.x < 0:

            self.x = 0

        if self.x + TAMANHO_QUADRADO > LARGURA_TELA:

            self.x = LARGURA_TELA - TAMANHO_QUADRADO

        if self.y < 0:

            self.y = 0

        if self.y + TAMANHO_QUADRADO > ALTURA_TELA:

            self.y = ALTURA_TELA - TAMANHO_QUADRADO


controls1 = {'cima': pygame.K_UP, 'baixo': pygame.K_DOWN, 'esquerda': pygame.K_LEFT, 'direita': pygame.K_RIGHT}

controls2 = {'cima': pygame.K_w, 'baixo': pygame.K_s, 'esquerda': pygame.K_a, 'direita': pygame.K_d}


player1 = Player(100, 100, imagem1, controls1)

player2 = Player(200, 200, imagem2, controls2)


rodar = True

clock = pygame.time.Clock()


while rodar:

    clock.tick(60)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            rodar = False


    keys = pygame.key.get_pressed()


    player1.move(keys)

    player2.move(keys)


    tela.fill((0, 0, 0))

    player1.draw(tela)

    player2.draw(tela)

    pygame.display.flip()


pygame.quit()
