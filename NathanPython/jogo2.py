import pygame
import random
import sys

pygame.init()

# Modo tela cheia
info = pygame.display.Info()
largura, altura = info.current_w, info.current_h
tela = pygame.display.set_mode((largura, altura), pygame.FULLSCREEN)
pygame.display.set_caption("Jogo dos Peixes")
clock = pygame.time.Clock()
fonte = pygame.font.SysFont(None, 36)
fonte_nivel = pygame.font.SysFont(None, 24)

AZUL = (0, 100, 255)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)

jogador_img = pygame.image.load("peixe_jogador.png")
inimigo_img = pygame.image.load("peixe_inimigo.png")

class PeixeJogador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.nivel = 1
        self.pontos = 0
        self.image = pygame.transform.scale(jogador_img, (60, 40))
        self.rect = self.image.get_rect(center=(largura // 2, altura // 2))
        self.velocidade = 6

    def update(self, teclas):
        if teclas[pygame.K_LEFT]:
            self.rect.x -= self.velocidade
        if teclas[pygame.K_RIGHT]:
            self.rect.x += self.velocidade
        if teclas[pygame.K_UP]:
            self.rect.y -= self.velocidade
        if teclas[pygame.K_DOWN]:
            self.rect.y += self.velocidade

        self.rect.x = max(0, min(self.rect.x, largura - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, altura - self.rect.height))

    def crescer(self):
        self.nivel += 1
        self.pontos += 10
        novo_larg = 60 + self.nivel * 5
        novo_alt = 40 + self.nivel * 3
        self.image = pygame.transform.scale(jogador_img, (novo_larg, novo_alt))
        centro = self.rect.center
        self.rect = self.image.get_rect(center=centro)

class PeixeInimigo(pygame.sprite.Sprite):
    def __init__(self, nivel_base):
        super().__init__()
        self.nivel = max(0, random.randint(nivel_base - 2, nivel_base + 2))
        tam_x = 30 + self.nivel * 5
        tam_y = 20 + self.nivel * 4
        self.image = pygame.transform.scale(inimigo_img, (tam_x, tam_y))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(largura, largura + 300)
        self.rect.y = random.randint(0, altura - 60)
        self.velocidade = random.randint(2, 5)

    def update(self):
        self.rect.x -= self.velocidade
        if self.rect.right < 0:
            self.reset()

    def reset(self):
        self.__init__(nivel_base=jogador.nivel)

def desenhar_texto(tela, texto, x, y, cor=BRANCO, fonte_custom=fonte):
    imagem = fonte_custom.render(texto, True, cor)
    tela.blit(imagem, (x, y))

def mostrar_menu():
    while True:
        tela.fill(AZUL)
        desenhar_texto(tela, "Jogo dos Peixes", largura // 2 - 120, altura // 2 - 50)
        desenhar_texto(tela, "Pressione ENTER para começar", largura // 2 - 170, altura // 2 + 10)
        pygame.display.flip()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    return

def desenhar_nivel(sprite, nivel):
    x = sprite.rect.centerx
    y = sprite.rect.top - 15
    desenhar_texto(tela, f"Lv {nivel}", x - 15, y, BRANCO, fonte_nivel)

def jogar():
    global jogador
    jogador = PeixeJogador()
    inimigos = pygame.sprite.Group()
    todos_sprites = pygame.sprite.Group()
    todos_sprites.add(jogador)

    for _ in range(10):
        inimigo = PeixeInimigo(jogador.nivel)
        inimigos.add(inimigo)
        todos_sprites.add(inimigo)

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        teclas = pygame.key.get_pressed()
        jogador.update(teclas)
        inimigos.update()

        for inimigo in inimigos:
            if jogador.rect.colliderect(inimigo.rect):
                if jogador.nivel > inimigo.nivel:
                    jogador.crescer()
                    inimigo.reset()
                elif jogador.nivel <= inimigo.nivel:
                    tela.fill(VERMELHO)
                    desenhar_texto(tela, "GAME OVER", largura // 2 - 100, altura // 2, BRANCO)
                    pygame.display.flip()
                    pygame.time.wait(2000)
                    return

        tela.fill(AZUL)
        todos_sprites.draw(tela)

        desenhar_nivel(jogador, jogador.nivel)
        for inimigo in inimigos:
            desenhar_nivel(inimigo, inimigo.nivel)

        desenhar_texto(tela, f"Pontos: {jogador.pontos}", 10, 10)
        desenhar_texto(tela, f"Nível: {jogador.nivel}", 10, 40)
        pygame.display.flip()
        clock.tick(60)

# Iniciar jogo
while True:
    mostrar_menu()
    jogar()
