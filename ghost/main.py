import pygame
import pygame.locals
from pygame.locals import *


WIDTH = 500
HEIGHT = 500
FPS = 30 #частота кадров в секунду
SPEED = 10

isJump = False
jumpCount = 10



def load_image(name):
    image = pygame.image.load(name)
    return image

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.images.append(load_image('ghost/Sprite-0003.png'))
        self.images.append(load_image('ghost/Sprite-0004.png'))
        self.images.append(load_image('ghost/Sprite-0005.png'))
        self.images.append(load_image('ghost/Sprite-0006.png'))
        self.images.append(load_image('ghost/Sprite-0007.png'))
        self.images.append(load_image('ghost/Sprite-0008.png'))

        self.index = 0
        self.image = self.images[self.index]
        self.image = pygame.transform.scale(self.image, (115, 115))
        self.rect = self.image.get_rect()
        self.rect.center = (100, HEIGHT-100)


    def update(self):

        if self.index + 1 >= 30:
            self.index = 0

        self.image = self.images[self.index // 5]
        self.index += 1

        # self.index += 1
        # if self.index >= len(self.images):
        #     self.index = 0
        # self.image = self.images[self.index]

class Stown(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((80, 170))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT

    def update(self):
        self.rect.x -= 3
        if self.rect.right < 0:
            self.rect.left = WIDTH

#создаем игру и окно
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GAMEGAMEGAME")
clock = pygame.time.Clock()

#создание группы спрайтов
all_sprites = pygame.sprite.Group()
stowns = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
stown = Stown()
all_sprites.add(stown)
stowns.add(stown)

#цикл игры
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        player.rect.x -= SPEED
        if player.rect.right < 0:
            player.rect.left = WIDTH
    if keys[K_RIGHT]:
        player.rect.x += SPEED
        if player.rect.left > WIDTH:
            player.rect.right = 0
    if not(isJump):
        if keys[K_SPACE]:
            isJump = True
    else:
        player.rect.y -= jumpCount * 4
        jumpCount -= 1
        if jumpCount < -10:
            isJump = False
            jumpCount = 10

    # обновление
    all_sprites.update()

    hit = pygame.sprite.spritecollide(player, stowns, True)
    # if hit:
    #     running = False


    #рендеринг
    screen.fill((255, 182, 193))
    all_sprites.draw(screen)
    #после отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()
