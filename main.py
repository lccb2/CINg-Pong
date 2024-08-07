import pygame
import sys
import random

preto = (0, 0, 0)
branco = (200, 200, 200)
azul = (0, 0, 200)
vermelho = (200, 0, 0)

LARGURA = 1500
ALTURA = 800
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("CINg-Pong")

pygame.init()

imagem1 = pygame.image.load('imagem1.png')
imagem2 = pygame.image.load('imagem2.png')
imagem3 = pygame.image.load('imagem3.png')
imagem4 = pygame.image.load('imagem4.png')

class TelaInicial:
    def __init__(self, tela):
        self.tela = tela
        self.largura = LARGURA
        self.altura = ALTURA
        self.imagem = pygame.image.load("imagem0.png")

        self.botao_sair = pygame.Rect(self.largura // 2 - 100, self.altura // 2 + 20, 200, 50)
        self.botao_jogar = pygame.Rect(self.largura // 2 - 100, self.altura // 2 - 50, 200, 50)
        self.botao_singleplayer = pygame.Rect(self.largura // 2 - 100, self.altura // 2 - 80, 200, 50)
        self.botao_multiplayer = pygame.Rect(self.largura // 2 - 100, self.altura // 2 - 10, 200, 50)
        self.botao_voltar = pygame.Rect(self.largura // 2 - 100, self.altura // 2 + 60, 200, 50)

        self.tela_atual = "principal"

    def desenhar_botao(self, cor, rect, texto):
        pygame.draw.rect(self.tela, cor, rect)
        fonte = pygame.font.SysFont(None, 35)
        texto_renderizado = fonte.render(texto, True, (255, 255, 255))
        texto_rect = texto_renderizado.get_rect(center=rect.center)
        self.tela.blit(texto_renderizado, texto_rect)

    def desenhar_tela_principal(self):
        self.tela.fill(preto)
        self.tela.blit(self.imagem, (self.largura // 2 - 200, self.altura // 2 - 200))
        self.desenhar_botao(vermelho, self.botao_sair, "SAIR")
        self.desenhar_botao(azul, self.botao_jogar, "JOGAR")

    def desenhar_tela_secundaria(self):
        self.tela.fill(preto)
        self.tela.blit(self.imagem, (self.largura // 2 - 200, self.altura // 2 - 200))
        self.desenhar_botao(azul, self.botao_singleplayer, "1 JOGADOR")
        self.desenhar_botao(azul, self.botao_multiplayer, "2 JOGADORES")
        self.desenhar_botao(vermelho, self.botao_voltar, "VOLTAR")

    def atualizar_tela_inicial(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.tela_atual == 'principal':
                        if self.botao_sair.collidepoint(event.pos):
                            pygame.quit()
                            sys.exit()
                        elif self.botao_jogar.collidepoint(event.pos):
                            self.tela_atual = 'secundaria'
                    elif self.tela_atual == 'secundaria':
                        if self.botao_voltar.collidepoint(event.pos):
                            self.tela_atual = 'principal'
                        elif self.botao_singleplayer.collidepoint(event.pos):
                            return 'jogo_singleplayer'
                        elif self.botao_multiplayer.collidepoint(event.pos):
                            return 'jogo_multiplayer'

            if self.tela_atual == "principal":
                self.desenhar_tela_principal()
            elif self.tela_atual == "secundaria":
                self.desenhar_tela_secundaria()

            pygame.display.flip()

class Placar:
    def __init__(self, tela):
        self.tela = tela
        self.fonte = pygame.font.SysFont(None, 80)
        self.pontuacao_1 = 0
        self.pontuacao_2 = 0
    
    def atualizar_pontuacao(self, jogador):
        if jogador == 1:
            self.pontuacao_1 += 1
        elif jogador == 2:
            self.pontuacao_2 += 1
    
    def criar_placar(self):
        texto = f"{self.pontuacao_1} - {self.pontuacao_2}"
        texto_renderizado = self.fonte.render(texto, True, branco)
        texto_rect = texto_renderizado.get_rect(center = (LARGURA // 2, 50))
        self.tela.blit(texto_renderizado, texto_rect)

    def score_check(self):
        if self.pontuacao_1 == 3:
            return 1
        elif self.pontuacao_2 == 3:
            return 2

class TelaJogo:
    def __init__(self, tela):
        self.tela = tela
        self.largura = LARGURA
        self.altura = ALTURA
        self.relogio = pygame.time.Clock()

    def draw_mesa(self):
        pygame.draw.rect(self.tela, (0, 0, 170), (150, 100, 1200, 600))
        pygame.draw.line(self.tela, (255, 255, 255), (150, 100), (150, 700), 5)
        pygame.draw.line(self.tela, (255, 255, 255), (150, 100), (1350, 100), 5)
        pygame.draw.line(self.tela, (255, 255, 255), (150, 700), (1350, 700), 5)
        pygame.draw.line(self.tela, (255, 255, 255), (1350, 100), (1350, 700), 5)
        pygame.draw.line(self.tela, (200, 200, 200), (748, 100), (748, 700), 7)
        pygame.draw.line(self.tela, (255, 255, 255), (152, 400), (742, 400), 3)
        pygame.draw.line(self.tela, (255, 255, 255), (753, 400), (1348, 400), 3)

    def resetar_posicoes(self, bola, player_1, player_2):
        bola.pos_x, bola.pos_y = LARGURA / 2, ALTURA / 2
        bola.direcao_x, bola.direcao_y = bola.velocidade_inicial, bola.velocidade_inicial
        player_1.pos_y = ALTURA / 2
        player_2.pos_y = ALTURA / 2

class Bola:
    def __init__(self, tela, cor, pos_x, pos_y, raio, direcao):
        self.tela = tela
        self.cor = cor
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.raio = raio
        self.direcao_x = direcao
        self.direcao_y = direcao
        self.velocidade_inicial = direcao
        self.aumentar_velocidade = 1

    def draw(self):
        pygame.draw.circle(self.tela, self.cor, (self.pos_x, self.pos_y), self.raio)

    def movimento(self):
        self.pos_x += self.direcao_x
        self.pos_y += self.direcao_y

        if self.pos_y >= ALTURA - self.raio or self.pos_y <= self.raio:
            self.direcao_y *= -1

    def colisao(self, colisor):
        bola_rect = pygame.Rect(self.pos_x - self.raio, self.pos_y - self.raio, self.raio * 2, self.raio * 2)
        if bola_rect.colliderect(colisor):
            if self.pos_x < LARGURA / 2:
                self.direcao_x = abs(self.direcao_x) + self.aumentar_velocidade
            else:
                self.direcao_x = -abs(self.direcao_x) - self.aumentar_velocidade

    def reinicio(self):
        if self.pos_x < 0:
            return 'red'
        
        if self.pos_x > LARGURA:
            return 'blue'
        
class Player:
    def __init__(self, tela, cor, pos_x, pos_y, largura, altura):
        self.tela = tela
        self.cor = cor
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.largura = largura
        self.altura = altura
        self.efeito = None
        self.tempo_efeito = 0
        self.velocidade = 5
        self.itens_coletados = {
            "aumentar_tamanho": 0,
            "diminuir_tamanho": 0,
            "aumentar_velocidade": 0,
            "diminuir_velocidade": 0,
        }

    def draw(self):
        pygame.draw.rect(self.tela, self.cor, (self.pos_x, self.pos_y, self.largura, self.altura))
    
    def movimento(self, tecla_up, tecla_down):
        keys = pygame.key.get_pressed()
        if keys[tecla_up] and self.pos_y > 0:
            self.pos_y -= self.velocidade
        if keys[tecla_down] and self.pos_y + self.altura < ALTURA:
            self.pos_y += self.velocidade

    def movimento_bot(self, pos_y_bola):
        if self.efeito == "aumentar_tamanho":
            self.altura = 200
        elif self.efeito == "diminuir_tamanho":
            self.altura = 20
        elif self.efeito == "aumentar_velocidade":
            self.velocidade = 20
        elif self.efeito == "diminuir_velocidade":
            self.velocidade = 2
        else:
            self.altura = 80
            self.velocidade = 5

        if self.pos_y < pos_y_bola and self.pos_y + self.altura < ALTURA:
            self.pos_y += self.velocidade
        if self.pos_y > pos_y_bola - self.altura and self.pos_y > 0:
            self.pos_y -= self.velocidade

    def aplicar_efeito(self, tipo, duracao):
        self.efeito = tipo
        self.tempo_efeito = pygame.time.get_ticks() + duracao
        
        if tipo in self.itens_coletados:
            self.itens_coletados[tipo] += 1

    def verificar_efeito(self):
        if self.efeito == "aumentar_tamanho":
            self.altura = 200
        elif self.efeito == "diminuir_tamanho":
            self.altura = 20
        elif self.efeito == "aumentar_velocidade":
            self.velocidade = 20
        elif self.efeito == "diminuir_velocidade":
            self.velocidade = 2

        if pygame.time.get_ticks() > self.tempo_efeito:
            self.resetar_efeito()

    def resetar_efeito(self):
        self.efeito = None
        self.altura = 80 
        self.velocidade = 5

class Item_Coletavel:
    def __init__(self, tela, tipo, x, y):
        self.tela = tela
        self.tipo = tipo
        self.x = x
        self.y = y

        if tipo == "aumentar_tamanho":
            self.imagem = pygame.transform.scale(imagem1, (40, 40))
        elif tipo == "diminuir_tamanho":
            self.imagem = pygame.transform.scale(imagem2, (60, 60))
        elif tipo == "aumentar_velocidade":
            self.imagem = pygame.transform.scale(imagem3, (45, 45))
        elif tipo == "diminuir_velocidade":
            self.imagem = pygame.transform.scale(imagem4, (40, 40))
        
        self.retangulo = pygame.Rect(self.x, self.y, self.imagem.get_width(), self.imagem.get_height())

    def draw(self):
        self.tela.blit(self.imagem, (self.x, self.y))
    
    def colisao(self, jogador_rect):
        return self.retangulo.colliderect(jogador_rect)
    
    def aplicar_efeito(self, jogador):
        duracao = 10000
        jogador.aplicar_efeito(self.tipo, duracao)



class Tela_da_Vitoria:
    def __init__(self, tela, vencedor, itens_coletados_1, itens_coletados_2):
        self.tela = tela
        self.vencedor = vencedor
        self.itens_coletados_1 = itens_coletados_1
        self.itens_coletados_2 = itens_coletados_2
        self.fonte = pygame.font.SysFont(None, 100)
        self.botao_home = pygame.Rect(LARGURA // 2 - 100, ALTURA - 180, 200, 50)
        self.botao_sair = pygame.Rect(LARGURA // 2 - 100, ALTURA - 100, 200, 50)

    def draw(self):
        self.tela.fill(preto)
        if self.vencedor == 2:
            linha_1 = (f"PLAYER 2")
            texto_renderizado = self.fonte.render(linha_1, True, (200, 0, 0))
        elif self.vencedor == 1:
            linha_1 = (f"PLAYER 1")
            texto_renderizado = self.fonte.render(linha_1, True, (0, 0, 200))
        texto_rect = texto_renderizado.get_rect(center=(LARGURA // 2, 70))
        self.tela.blit(texto_renderizado, texto_rect)
        linha_2 = ("GANHOU!")
        texto_renderizado = self.fonte.render(linha_2, True, (0, 0, 200) if self.vencedor == 1 else (200, 0, 0))
        texto_rect = texto_renderizado.get_rect(center=(LARGURA // 2, 140))
        self.tela.blit(texto_renderizado, texto_rect)

        if self.vencedor == 1:
            itens_mostrados = self.itens_coletados_1
        else:
            itens_mostrados = self.itens_coletados_2

        linha_3 = (f"--- Player {self.vencedor} coletou ---")
        texto_renderizado = self.fonte.render(linha_3, True, branco)
        texto_rect = texto_renderizado.get_rect(center=(LARGURA // 2, 225))
        self.tela.blit(texto_renderizado, texto_rect)


        linha_4 = (f"Cogumelos: {itens_mostrados['aumentar_tamanho']}")
        texto_renderizado = self.fonte.render(linha_4, True, branco)
        texto_rect = texto_renderizado.get_rect(center=(LARGURA // 2, 300))
        self.tela.blit(texto_renderizado, texto_rect)

        linha_5 = (f"Pizzas: {itens_mostrados['diminuir_tamanho']}")
        texto_renderizado = self.fonte.render(linha_5, True, branco)
        texto_rect = texto_renderizado.get_rect(center=(LARGURA // 2, 380))
        self.tela.blit(texto_renderizado, texto_rect)

        linha_6 = (f"Raios: {itens_mostrados['aumentar_velocidade']}")
        texto_renderizado = self.fonte.render(linha_6, True, branco)
        texto_rect = texto_renderizado.get_rect(center=(LARGURA // 2, 450))
        self.tela.blit(texto_renderizado, texto_rect)

        linha_7 = (f"Gelos: {itens_mostrados['diminuir_velocidade']}")
        texto_renderizado = self.fonte.render(linha_7, True, branco)
        texto_rect = texto_renderizado.get_rect(center=(LARGURA // 2, 520))
        self.tela.blit(texto_renderizado, texto_rect)

        pygame.draw.rect(self.tela, azul, self.botao_home)
        pygame.draw.rect(self.tela, vermelho, self.botao_sair)
        fonte = pygame.font.SysFont(None, 35)
        texto_home = fonte.render("HOME", True, branco)
        texto_sair = fonte.render("SAIR", True, branco)
        self.tela.blit(texto_home, texto_home.get_rect(center=self.botao_home.center))
        self.tela.blit(texto_sair, texto_sair.get_rect(center=self.botao_sair.center))
        pygame.display.flip()

    def atualizar_tela_vitoria(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.botao_home.collidepoint(event.pos):
                        return 'home'
                    elif self.botao_sair.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()

def criar_item():
    x_positions = [75, LARGURA - 120] 
    x = random.choice(x_positions) 
    y = random.randint(100, ALTURA - 100)
    tipo = random.choice(["aumentar_tamanho", "diminuir_tamanho", "aumentar_velocidade", "diminuir_velocidade"])
    item = Item_Coletavel(tela, tipo, x, y)
    itens.append(item)
    tempo_item.append(pygame.time.get_ticks())

tela_inicial = TelaInicial(tela)

while True:
    estado = tela_inicial.atualizar_tela_inicial()
    
    if estado in ['jogo_singleplayer', 'jogo_multiplayer']:
        tela_jogo = TelaJogo(tela)
        placar = Placar(tela)
        bola = Bola(tela, branco, LARGURA / 2, ALTURA / 2, 10, 5)
        player_1 = Player(tela, azul, 90, ALTURA / 2, 20, 80)
        player_2 = Player(tela, vermelho, LARGURA - 110, ALTURA / 2, 20, 80)

        itens = []
        tempo_item = []

        criar_item()

        if estado == 'jogo_singleplayer':
            bot = True
        else:
            bot = False

        while True:
            tela_jogo.relogio.tick(60)
            tela.fill(preto)
            tela_jogo.draw_mesa()

            bola.draw()
            player_1.draw()
            player_2.draw()
            placar.criar_placar()

            for item in itens:
                item.draw()
                if item.colisao(pygame.Rect(player_1.pos_x, player_1.pos_y, player_1.largura, player_1.altura)):
                    item.aplicar_efeito(player_1)
                    itens.remove(item)
                elif item.colisao(pygame.Rect(player_2.pos_x, player_2.pos_y, player_2.largura, player_2.altura)):
                    item.aplicar_efeito(player_2)
                    itens.remove(item)
            
            tempo_atual = pygame.time.get_ticks()
            i = 0
            while i < len(tempo_item):
                tempo = tempo_item[i]
                if tempo_atual - tempo > 10000:
                    tempo_item.pop(i)
                    criar_item()
                else:
                    i += 1

            player_1.verificar_efeito()
            player_2.verificar_efeito()

            bola.movimento()
            bola.colisao(pygame.Rect(player_1.pos_x, player_1.pos_y, player_1.largura, player_1.altura))
            bola.colisao(pygame.Rect(player_2.pos_x, player_2.pos_y, player_2.largura, player_2.altura))
            jogador_que_pontuou = bola.reinicio()

            if jogador_que_pontuou == "blue":
                placar.atualizar_pontuacao(1)
                player_1.resetar_efeito()
                player_2.resetar_efeito()
                tela_jogo.resetar_posicoes(bola, player_1, player_2)
                pygame.display.flip()
                pygame.time.wait(2000)  
            elif jogador_que_pontuou == "red":
                placar.atualizar_pontuacao(2)
                player_1.resetar_efeito()
                player_2.resetar_efeito()
                tela_jogo.resetar_posicoes(bola, player_1, player_2)
                pygame.display.flip()
                pygame.time.wait(2000)  
          
            vencedor = placar.score_check()
            if vencedor:
                tela_vitoria = Tela_da_Vitoria(tela, vencedor, player_1.itens_coletados, player_2.itens_coletados)
                while True:
                    tela_vitoria.draw()
                    acao = tela_vitoria.atualizar_tela_vitoria()
                    if acao == 'home':
                        break
                break

            if bot:
                player_2.movimento_bot(bola.pos_y)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            player_1.movimento(pygame.K_w, pygame.K_s)
            if not bot:
                player_2.movimento(pygame.K_UP, pygame.K_DOWN)

            pygame.display.flip()
