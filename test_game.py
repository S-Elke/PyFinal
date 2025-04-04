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

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=pos)
        self.attack_strength = 5 #placeholder
        self.action = "None"

    def moveRight(self, pixels):
        self.rect.x += pixels

    def moveLeft(self, pixels):
        self.rect.x -= pixels

    def moveForward(self, speed):
        self.rect.y += speed * speed/15

    def moveBack(self, speed):
        self.rect.y -= speed * speed/15

    def spell(self):
        print("Cast Spell")
        
    def attack(self):
        self.action = "Attack"
        print(self.action)

    def block(self):
        print("Block")
        
timers = []

class timer():
    def __init__(self, duration, callback):
        super().__init__()
        self.start_time = pygame.time.get_ticks()
        self.duration = duration * 1000
        self.callback = callback
        timers.append(self)
        

    def update():
        if self.start_time - pygame.time.get_ticks() >= self.duration:
            self.callback()
            self.time_out()

    def time_out():
        timers.remove(self)

    
        

    


class Enemy(pygame.sprite.Sprite):
    def __init__(self,pos,image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=pos)
        self.health = 11
        self.visible = True

    def movement(self):
        ""

    def combat(self,attacks):
        #choice = random.randint(1,10)
        choice = 7
        if(choice < 3):  #block
            ''
        elif(choice < 5): #spell
            ""
        else: #attack
            attack_mode = random.randint(1,10)

            if(attack_mode < 3): #heavy attack
                return(attacks[0])
            else: #light attack
                return(attacks[1])

    def increment_health(self, num):
        self.health += num
        if self.health <= 0:
            self.visible = False;
            
def scale_image(image, scale):
    image = pygame.transform.smoothscale(image, (image.get_size()[0]*scale, image.get_size()[1]*scale))
    return image

def scale_rect(rect, scale):
    rect.x += rect[2]*(1-scale)/2
    rect.y += rect[3]*(1-scale)/2
    return rect


class Interactable(pygame.sprite.Sprite):
    def __init__(self,pos,image, callback, clickable = True):
        super().__init__()  
        self.image = image
        self.image_og = image
        self.clickable = clickable
        self.rect = self.image.get_rect(center=pos)
        self.rect_og = self.image.get_rect(center=pos)
        self.callback = callback
        self.pressed = False

    def update(self,events):
        if self.clickable == True:
            for event in events:
                if event.type == pygame.MOUSEBUTTONUP:
                    if self.rect.collidepoint(event.pos):
                        self.callback()
                    if self.pressed:
                        self.image = self.image_og
                        self.rect = scale_rect(self.rect, 1.5)
                        self.pressed = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.rect.collidepoint(event.pos):
                        self.image = scale_image(self.image, 0.5)
                        self.rect = scale_rect(self.rect, 0.5)
                        self.pressed = True
                        
                        

    

class Terrain(pygame.sprite.Sprite):
    def __init__(self,pos,image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=pos)

def on_click():
    ''

player_sprites_list = pygame.sprite.Group()
enemy_sprites_list = pygame.sprite.Group()
menu_sprites_list = pygame.sprite.Group()
terrain_sprites_list = pygame.sprite.Group()

player = Player((200,300), player_image)
goblin1 = Enemy((400, 500), goblin_image)
goblin2 = Enemy((100, 800), goblin_image)
magicGoblin = Enemy((600,600), magic_goblin_image)

menu = Interactable((960,880), menu_image, on_click, clickable = False)
attack = Interactable((350, 880), attack_button_image, player.attack)
spell = Interactable((850, 880), spell_button_image, player.spell)
shield = Interactable((1350, 880), shield_button_image, player.block)

player_combat = Player((250, 500), player_combat_image)
goblin_combat = Enemy((1250, 500) , goblin_combat_image)

player_sprites_list.add(player)
enemy_sprites_list.add(goblin1)
enemy_sprites_list.add(goblin2)
enemy_sprites_list.add(magicGoblin)


enemy_object_list = []

exit = True
combat_state = False
clock = pygame.time.Clock()
combat_start = True

while exit:
    events = pygame.event.get()
    for event in events:
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
        if combat_start:
            combat_start = False
        else:
            menu_sprites_list.add(menu)
            menu_sprites_list.add(attack)
            menu_sprites_list.add(spell)
            menu_sprites_list.add(shield)
            player_sprites_list.add(player_combat)
            enemy_object_list.append(goblin_combat)
            for enemy in enemy_object_list:
                enemy_sprites_list.empty()
                if enemy.visible == True:
                    enemy_sprites_list.add(enemy)
            
            if player.action != "None":
                target = 0;
                if player.action == "Attack":
                    enemy_object_list[target].increment_health(-player.attack_strength)
                    player.action = "None"

            damage = int(goblin1.combat((6,2)))

            health = 10
            health -= damage


    player_sprites_list.update()
    enemy_sprites_list.update()
    menu_sprites_list.update(events)
    terrain_sprites_list.update()
    screen.fill(SURFACE_COLOR)
    player_sprites_list.draw(screen)
    enemy_sprites_list.draw(screen)
    menu_sprites_list.draw(screen)
    terrain_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)
    for timer in timers:
        timer.update()

pygame.quit()
