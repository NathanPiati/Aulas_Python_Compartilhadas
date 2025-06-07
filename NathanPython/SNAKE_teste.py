import pygame
import random
import sys
import os

# Inicialização
pygame.init()

# Tamanho da tela e elementos
TAMANHO = 20
GRID = 25
LARGURA = ALTURA = TAMANHO * GRID
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Cobrinha Minimalista")

# Cores
COR_FUNDO = (30, 30, 30)
COR_TEXTO = (255, 255, 255)

# Carregar spritesheets
snake_spritesheet = pygame.image.load("snake_spritesheet.png").convert_alpha()
food_rabbit_spritesheet = pygame.image.load("food_rabbit_spritesheet.png").convert_alpha()

# Definir retângulos para cada sprite (ajustado conforme a disposição das imagens)
SPRITE_SIZE = 20
# Snake sprites (baseado na primeira imagem 3x3)
head_up = pygame.Surface.subsurface(snake_spritesheet, (0, 0, SPRITE_SIZE, SPRITE_SIZE))    # Cabeça para cima
head_down = pygame.Surface.subsurface(snake_spritesheet, (SPRITE_SIZE, 0, SPRITE_SIZE, SPRITE_SIZE))  # Cabeça para baixo
head_left = pygame.Surface.subsurface(snake_spritesheet, (2 * SPRITE_SIZE, 0, SPRITE_SIZE, SPRITE_SIZE))  # Cabeça para esquerda
head_right = pygame.Surface.subsurface(snake_spritesheet, (0, SPRITE_SIZE, SPRITE_SIZE, SPRITE_SIZE))  # Cabeça para direita
body = pygame.Surface.subsurface(snake_spritesheet, (SPRITE_SIZE, SPRITE_SIZE, SPRITE_SIZE, SPRITE_SIZE))  # Corpo
# Food e Rabbit (baseado na segunda imagem)
food = pygame.Surface.subsurface(food_rabbit_spritesheet, (0, 0, SPRITE_SIZE, SPRITE_SIZE))  # Comida
rabbit = pygame.Surface.subsurface(food_rabbit_spritesheet, (0, SPRITE_SIZE, SPRITE_SIZE, SPRITE_SIZE))  # Coelho

# Fonte
fonte = pygame.font.SysFont('Arial', 20)

# Cobra
cobra = [(5, 5), (4, 5), (3, 5)]
direcao = "DIREITA"
proxima_direcao = direcao

# Comida
def nova_comida():
    while True:
        pos = (random.randint(0, GRID - 1), random.randint(0, GRID - 1))
        if pos not in cobra:
            return pos

comida_atual = "food"
comida_pos = nova_comida()

# Pontuação
pontuacao = 0
recorde = 0
if os.path.exists("recorde.txt"):
    with open("recorde.txt", "r") as f:
        recorde = int(f.read())

# Movimentação segura
direcoes_opostas = {
    "CIMA": "BAIXO", "BAIXO": "CIMA",
    "ESQUERDA": "DIREITA", "DIREITA": "ESQUERDA"
}

# Desenhar cobra com sprites
def desenhar_cobra():
    for i, (x, y) in enumerate(cobra):
        px, py = x * TAMANHO, y * TAMANHO
        if i == 0:
            # Escolher sprite da cabeça com base na direção
            if direcao == "CIMA":
                TELA.blit(head_up, (px, py))
            elif direcao == "BAIXO":
                TELA.blit(head_down, (px, py))
            elif direcao == "ESQUERDA":
                TELA.blit(head_left, (px, py))
            else:  # DIREITA
                TELA.blit(head_right, (px, py))
        else:
            TELA.blit(body, (px, py))

# Movimento da comida (foge da cobra)
def mover_comida():
    global comida_pos, comida_atual
    direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    melhor_pos = comida_pos
    max_dist = -1
    for dx, dy in direcoes:
        novo = (comida_pos[0] + dx, comida_pos[1] + dy)
        if 0 <= novo[0] < GRID and 0 <= novo[1] < GRID and novo not in cobra:
            dist = min([abs(novo[0] - cx) + abs(novo[1] - cy) for cx, cy in cobra])
            if dist > max_dist:
                max_dist = dist
                melhor_pos = novo
    comida_pos = melhor_pos
    # Alternar entre comida e coelho aleatoriamente
    if random.random() < 0.2:  # 20% de chance de virar coelho
        comida_atual = "rabbit"
    else:
        comida_atual = "food"

# Tela de game over
def game_over():
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_r:
                return True  # Reinicia o jogo
        TELA.fill(COR_FUNDO)
        texto_game_over = fonte.render("Game Over! Pressione R para reiniciar", True, COR_TEXTO)
        texto_pontos = fonte.render(f"Pontuação: {pontuacao}  Recorde: {recorde}", True, COR_TEXTO)
        TELA.blit(texto_game_over, (LARGURA // 4, ALTURA // 2 - 20))
        TELA.blit(texto_pontos, (LARGURA // 4, ALTURA // 2 + 20))
        pygame.display.update()

# Loop principal
clock = pygame.time.Clock()
rodando = True
while rodando:
    clock.tick(10)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Entrada de teclado
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_UP] and direcao != "BAIXO":
        proxima_direcao = "CIMA"
    elif teclas[pygame.K_DOWN] and direcao != "CIMA":
        proxima_direcao = "BAIXO"
    elif teclas[pygame.K_LEFT] and direcao != "DIREITA":
        proxima_direcao = "ESQUERDA"
    elif teclas[pygame.K_RIGHT] and direcao != "ESQUERDA":
        proxima_direcao = "DIREITA"

    # Atualiza direção apenas se for válida
    if proxima_direcao != direcoes_opostas[direcao]:
        direcao = proxima_direcao

    # Movimento da cobra
    x, y = cobra[0]
    if direcao == "CIMA":
        y -= 1
    elif direcao == "BAIXO":
        y += 1
    elif direcao == "ESQUERDA":
        x -= 1
    elif direcao == "DIREITA":
        x += 1
    nova_pos = (x, y)

    # Colisão
    if nova_pos in cobra or not (0 <= x < GRID and 0 <= y < GRID):
        if game_over():
            # Reiniciar jogo
            cobra = [(5, 5), (4, 5), (3, 5)]
            direcao = "DIREITA"
            proxima_direcao = direcao
            pontuacao = 0
            comida_pos = nova_comida()
            comida_atual = "food"
        continue

    cobra.insert(0, nova_pos)
    if nova_pos == comida_pos:
        pontuacao += 1 if comida_atual == "food" else 3  # 3 pontos para coelho
        if pontuacao > recorde:
            recorde = pontuacao
            with open("recorde.txt", "w") as f:
                f.write(str(recorde))
        comida_pos = nova_comida()
        mover_comida()
    else:
        cobra.pop()

    mover_comida()

    # Desenho
    TELA.fill(COR_FUNDO)
    desenhar_cobra()
    if comida_atual == "food":
        TELA.blit(food, (comida_pos[0] * TAMANHO, comida_pos[1] * TAMANHO))
    else:
        TELA.blit(rabbit, (comida_pos[0] * TAMANHO, comida_pos[1] * TAMANHO))
    texto = fonte.render(f"Pontos: {pontuacao}  |  Recorde: {recorde}", True, COR_TEXTO)
    TELA.blit(texto, (10, 10))
    pygame.display.update()

pygame.quit()