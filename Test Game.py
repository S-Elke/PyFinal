import random
import pygame

WIDTH = 1920
HEIGHT = 1080
SURFACE_COLOR = (79, 7, 26)

pygame.init()

size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Test Game")

goblin_image = pygame.image.load('goblin.png').convert_alpha()
magic_goblin_image = pygame.image.load('magic_goblin.png').convert_alpha()
player_image = pygame.image.load('player.png').convert_alpha()
menu_image = pygame.image.load('menu_bar.png').convert_alpha()
attack_button_image = pygame.image.load('attack__button.png').convert_alpha()
spell_button_image = pygame.image.load('spell_button.png').convert_alpha()
shield_button_image = pygame.image.load('shield_button.png').convert_alpha()
player_combat_image = pygame.image.load('player_combat.png').convert_alpha()
goblin_combat_image = pygame.image.load('goblin_combat.png').convert_alpha()

class Sprite(pygame.sprite.Sprite):
    def __init__(self, pos, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=pos)

    def moveRight(self, pixels):
        self.rect.x += pixels

    def moveLeft(self, pixels):
        self.rect.x -= pixels

    def moveForward(self, speed):
        self.rect.y += speed * speed/15

    def moveBack(self, speed):
        self.rect.y -= speed * speed/15


player_sprites_list = pygame.sprite.Group()
enemy_sprites_list = pygame.sprite.Group()
menu_sprites_list = pygame.sprite.Group()
terrain_sprites_list = pygame.sprite.Group()

player = Sprite((200,300), player_image)
goblin1 = Sprite((400, 500), goblin_image)
goblin2 = Sprite((100, 800), goblin_image)
magicGoblin = Sprite((600,600), magic_goblin_image)

menu = Sprite((960,880), menu_image)
attack = Sprite((350, 880), attack_button_image)
spell = Sprite((850, 880), spell_button_image)
shield = Sprite((1350, 880), shield_button_image)

player_combat = Sprite((250, 500), player_combat_image)
goblin_combat = Sprite((1250, 500) , goblin_combat_image)

player_sprites_list.add(player)
enemy_sprites_list.add(goblin1)
enemy_sprites_list.add(goblin2)
enemy_sprites_list.add(magicGoblin)


exit = True
combat_state = False
clock = pygame.time.Clock()

while exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                exit = False

    if combat_state == False:
        keys = pygame.key.get_pressed()


        if keys[pygame.K_a]:
            player.moveLeft(8.5)
        if keys[pygame.K_d]:
            player.moveRight(8.5)
        if keys[pygame.K_s]:
            player.moveForward(8.5)
        if keys[pygame.K_w]:
            player.moveBack(8.5)

        for each in enemy_sprites_list.sprites():
            if((each.rect.x-50 < player.rect.x < each.rect.x+50) and (each.rect.y-50 < player.rect.y < each.rect.y+50)):
                enemy_sprites_list.empty()
                player_sprites_list.empty()
                combat_state = True
    if combat_state == True:
        menu_sprites_list.add(menu)
        menu_sprites_list.add(attack)
        menu_sprites_list.add(spell)
        menu_sprites_list.add(shield)
        player_sprites_list.add(player_combat)
        enemy_sprites_list.add(goblin_combat)

    player_sprites_list.update()
    enemy_sprites_list.update()
    menu_sprites_list.update()
    terrain_sprites_list.update()
    screen.fill(SURFACE_COLOR)
    player_sprites_list.draw(screen)
    enemy_sprites_list.draw(screen)
    menu_sprites_list.draw(screen)
    terrain_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)


pygame.quit()
