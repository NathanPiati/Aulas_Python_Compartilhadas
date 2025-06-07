import pygame
from sqlalchemy import true
import sys
import random

pygame.init()


screen = pygame.display.set_mode((1200, 900))
verde = true
x = 30
y = 30
LARGURA, ALTURA = 1200, 900
TAMANHO_QUADRADO = 50
VELOCIDADE = 10

snake = [(200, 200), (220, 200), (240, 200)]
direcao = (1, 0)
frutas = [(400, 300)]

fps = pygame.time.Clock()

pygame.display.set_caption("Jogo do Senai")

clock = pygame.time.Clock()

done = False
def colisao_com_fruta():
    if snake[0] in frutas:
        frutas.remove(snake[0])
        return True
    return False

def move_snake():
    cabeca = snake[0]
    x, y = cabeca
    snake.insert(0, (x + direcao[0]*TAMANHO_QUADRADO, y + direcao[1]*TAMANHO_QUADRADO))
    if snake[0] in snake[1:]:
        pygame.quit()
        sys.exit()
    snake.pop()
def spawn_fruta():
    x = random.randint(0, LARGURA - TAMANHO_QUADRADO) // TAMANHO_QUADRADO * TAMANHO_QUADRADO
    y = random.randint(0, ALTURA - TAMANHO_QUADRADO) // TAMANHO_QUADRADO * TAMANHO_QUADRADO
    frutas.append((x, y))


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        y -= 3
    if pressed[pygame.K_DOWN]:
        y += 3
    if pressed[pygame.K_LEFT]:
        x -= 3
    if pressed[pygame.K_RIGHT]:
        x += 3

    if verde:
        color = (255, 128, 0)
    else:
        color = (100, 0, 100)


    pygame.draw.circle(screen, color, (x, y), 20)    

    pygame.draw.rect(screen, (250, 250, 100),
                     pygame.Rect(50, 520, 50, 50))

    pygame.display.flip()            

    clock.tick(60)