import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Configuração da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo de Fazenda")

# Cores
WHITE = (255, 255, 255)
GREEN = (50, 205, 50)
BROWN = (139, 69, 19)
BLACK = (0, 0, 0)
DARK_GREEN = (0, 150, 0)
GRAY = (211, 211, 211)

# Fonte
font = pygame.font.SysFont("arial", 24)

# Carregar imagens
plant_sprites = [
    pygame.image.load("plant_vazia.png"),  # Imagem da planta vazia
    pygame.image.load("plant_seed.png"),   # Imagem da semente
    pygame.image.load("plant_growing.png"), # Imagem da planta crescendo
    pygame.image.load("plant_mature.png")   # Imagem da planta madura
]

animal_sprites = {
    "cow": [
        pygame.image.load("cow_idle_1.png"),
        pygame.image.load("cow_idle_2.png")
    ],
    "chicken": [
        pygame.image.load("chicken_idle_1.png"),
        pygame.image.load("chicken_idle_2.png")
    ]
}

# Definir o tamanho dos sprites
plant_size = (50, 50)
animal_size = (60, 60)

# Classe Planta
class Planta:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.estado = -1  # -1 = vazio, 0 = semente, 1 = crescendo, 2 = pronta
        self.timer = 0

    def plantar(self):
        if self.estado == -1:
            self.estado = 0
            self.timer = 0

    def regar(self):
        if self.estado >= 0 and self.estado < 2:
            self.timer += 1

    def atualizar(self):
        if self.estado == 0 and self.timer > 3:
            self.estado = 1
        elif self.estado == 1 and self.timer > 5:
            self.estado = 2

    def colher(self):
        if self.estado == 2:
            self.estado = -1
            self.timer = 0
            return True
        return False

    def desenhar(self, tela):
        tela.blit(plant_sprites[self.estado], (self.x, self.y))

# Classe Animal
class Animal(pygame.sprite.Sprite):
    def __init__(self, tipo, x, y):
        super().__init__()
        self.tipo = tipo
        self.x = x
        self.y = y
        self.image = animal_sprites[tipo][0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.frame = 0
        self.timer = 0

    def atualizar(self):
        self.timer += 1
        if self.timer > 20:
            self.frame = (self.frame + 1) % len(animal_sprites[self.tipo])
            self.image = animal_sprites[self.tipo][self.frame]
            self.timer = 0

    def desenhar(self, tela):
        tela.blit(self.image, self.rect)

# Instanciar plantas
plantas = [Planta(100 + i * 60, 300) for i in range(5)]

# Instanciar animais
animais = pygame.sprite.Group()
animais.add(Animal("cow", 300, 400))
animais.add(Animal("chicken", 400, 400))

# Variáveis do jogador
dinheiro = 100
sementes = 3
preco_semente = 20

# Função da loja
def desenhar_loja(tela):
    pygame.draw.rect(tela, GRAY, (600, 50, 180, 50))
    texto = font.render("Comprar Semente (R$20)", True, BLACK)
    tela.blit(texto, (610, 65))

# Loop do jogo
clock = pygame.time.Clock()

while True:
    screen.fill((135, 206, 235))  # Céu azul claro
    pygame.draw.rect(screen, (139, 69, 19), (0, 280, WIDTH, HEIGHT))  # Solo

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()

            # Clique nas plantas
            for planta in plantas:
                if planta.x <= mx <= planta.x + 50 and planta.y <= my <= planta.y + 50:
                    if planta.estado == -1 and sementes > 0:
                        planta.plantar()
                        sementes -= 1
                    elif planta.estado < 2:
                        planta.regar()
                    elif planta.estado == 2:
                        if planta.colher():
                            dinheiro += 10

            # Comprar sementes
            if 600 <= mx <= 780 and 50 <= my <= 100:
                if dinheiro >= preco_semente:
                    sementes += 1
                    dinheiro -= preco_semente

    # Atualizar
    for planta in plantas:
        planta.atualizar()
        planta.desenhar(screen)

    for animal in animais:
        animal.atualizar()
        animal.desenhar(screen)

    # Desenhar loja
    desenhar_loja(screen)

    # UI
    dinheiro_txt = font.render(f"Dinheiro: R$ {dinheiro}", True, BLACK)
    sementes_txt = font.render(f"Sementes: {sementes}", True, BLACK)
    screen.blit(dinheiro_txt, (10, 10))
    screen.blit(sementes_txt, (10, 40))

    pygame.display.flip()
    clock.tick(60)

    # Controle de FPS
    clock.tick(60)