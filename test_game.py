import random
import pygame

WIDTH = 1920
HEIGHT = 1080
SURFACE_COLOR = (79, 7, 26)

pygame.init()

size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Test Game")
font = pygame.font.SysFont(None, 36, bold=True)
# Load dungeon backgrounds
dungeon_1 = pygame.image.load("Dungeon_1_1920x1080.png").convert()
dungeon_3 = pygame.image.load("Dungeon_3_1920x1080.png").convert()
combat_background = pygame.image.load('dungeon_background_1920x1080.png')
dungeon_images = [dungeon_1, dungeon_3]
current_dungeon = 0
room_complete = False
game_over = False

exit_zone = pygame.Rect(0, 0, 0, 0)

#loading sprites
goblin_image = pygame.image.load('goblin_final_192x192.png').convert_alpha()
magic_goblin_image = pygame.image.load('magic_goblin_192_transparent.png').convert_alpha()
buff_goblin_image = pygame.image.load('buff_goblin_256px_transparent.png').convert_alpha()
boss = pygame.image.load('boss_goblin_blue_320px_transparent.png').convert_alpha()
player_image = pygame.image.load('character_192x192_transparent.png').convert_alpha()
menu_image = pygame.image.load('menu_backdrop.png').convert_alpha()
attack_button_image = pygame.image.load('button_attack.png').convert_alpha()
spell_button_image = pygame.image.load('button_spell.png').convert_alpha()
shield_button_image = pygame.image.load('button_block.png').convert_alpha()
fireball_button_image = pygame.image.load('button_fireball.png').convert_alpha()
meteor_button_image = pygame.image.load('button_meteor.png').convert_alpha()
bolt_button_image = pygame.image.load('button_bolt.png').convert_alpha()
player_combat_image = pygame.image.load('player_combat.png').convert_alpha()
goblin_combat_image = pygame.image.load('goblin_combat.png').convert_alpha()
swoosh_gray_image = pygame.image.load('swoosh_true_gray_192 (1).png').convert_alpha()
swoosh_blue_image = pygame.image.load('swoosh_blue_192.png').convert_alpha()
swoosh_red_image = pygame.image.load('swoosh_red_192.png').convert_alpha()
shield_wood_image = pygame.image.load('shield_wooden_fixed_192.png').convert_alpha()
shield_metal_image = pygame.image.load('shield_metal_fixed_192.png').convert_alpha()
shield_magic_image = pygame.image.load('shield_magic_fixed_192.png').convert_alpha()
lightning_image = pygame.image.load('lightning_192x192_transparent_192.png').convert_alpha()
fireball_image = pygame.image.load('fireball_192x192_transparent_192.png').convert_alpha()
meteor_image = pygame.image.load('meteor_192x192_transparent_192.png').convert_alpha()
health_bar_image = pygame.image.load('health_bar.png')
shield_bar_image = pygame.image.load('shield_bar.png')

#functions for image maniupulation
def scale_image(image, scale):
    image = pygame.transform.smoothscale(image, (image.get_size()[0] * scale, image.get_size()[1] * scale))
    return image

def scale_rect(rect, scale):
    rect.x += rect[2] * (1 - scale) / 2
    rect.y += rect[3] * (1 - scale) / 2
    return rect

#scaling sprites for different purposes
attack_intent_image = pygame.image.load('swoosh_red_192.png').convert_alpha()
scale_image(attack_intent_image, 0.5)
defend_intent_image = pygame.image.load('shield_metal_fixed_192.png').convert_alpha()
scale_image(defend_intent_image, 0.5)
lightning_intent_image = pygame.image.load('lightning_192x192_transparent_192.png').convert_alpha()
scale_image(lightning_intent_image, 0.5)
fireball_intent_image = pygame.image.load('fireball_192x192_transparent_192.png').convert_alpha()
scale_image(fireball_intent_image, 0.5)
meteor_intent_image = pygame.image.load('meteor_192x192_transparent_192.png').convert_alpha()
scale_image(meteor_intent_image, 0.5)




#animations handler
class Animations(pygame.sprite.Sprite):
    def __init__(self, pos, type):
        super().__init__()
        self.enemy = enemy
        self.type = type
        self.animation_type = type

        self.lightning0 = pygame.image.load('lightning0.png').convert_alpha()
        self.lightning1 = pygame.image.load('lightning1.png').convert_alpha()
        self.lightning2 = pygame.image.load('lightning2.png').convert_alpha()
        self.lightning3= pygame.image.load('lightning3.png').convert_alpha()

        self.fireball0 = pygame.image.load('fireball0.png').convert_alpha()
        self.fireball1 = pygame.image.load('fireball1.png').convert_alpha()
        self.fireball2 = pygame.image.load('fireball2.png').convert_alpha()
        self.fireball3 = pygame.image.load('fireball3.png').convert_alpha()
        self.fireball4 = pygame.image.load('fireball4.png').convert_alpha()
        self.fireball5 = pygame.image.load('fireball5.png').convert_alpha()

        self.meteor0 = pygame.image.load('meteor0.png').convert_alpha()
        self.meteor1 = pygame.image.load('meteor1.png').convert_alpha()
        self.meteor2 = pygame.image.load('meteor2.png').convert_alpha()
        self.meteor3 = pygame.image.load('meteor3.png').convert_alpha()
        self.meteor4 = pygame.image.load('meteor4.png').convert_alpha()
        self.meteor5 = pygame.image.load('meteor5.png').convert_alpha()

        self.swoosh_gray0 = pygame.image.load('swoosh_gray0.png').convert_alpha()
        self.swoosh_gray1 = pygame.image.load('swoosh_gray1.png').convert_alpha()
        self.swoosh_gray2 = pygame.image.load('swoosh_gray2.png').convert_alpha()
        self.swoosh_gray3 = pygame.image.load('swoosh_gray3.png').convert_alpha()
        self.swoosh_gray4 = pygame.image.load('swoosh_gray4.png').convert_alpha()
        self.swoosh_gray5 = pygame.image.load('swoosh_gray5.png').convert_alpha()

        self.swoosh_blue0 = pygame.image.load('swoosh_blue0.png').convert_alpha()
        self.swoosh_blue2 = pygame.image.load('swoosh_blue2.png').convert_alpha()
        self.swoosh_blue3 = pygame.image.load('swoosh_blue3.png').convert_alpha()
        self.swoosh_blue4 = pygame.image.load('swoosh_blue4.png').convert_alpha()
        self.swoosh_blue5 = pygame.image.load('swoosh_blue5.png').convert_alpha()
        self.swoosh_blue6 = pygame.image.load('swoosh_blue6.png').convert_alpha()
        self.swoosh_blue7 = pygame.image.load('swoosh_blue7.png').convert_alpha()

        self.swoosh_red0 = pygame.image.load('swoosh_red0.png').convert_alpha()
        self.swoosh_red1 = pygame.image.load('swoosh_red1.png').convert_alpha()
        self.swoosh_red2 = pygame.image.load('swoosh_red2.png').convert_alpha()
        self.swoosh_red3 = pygame.image.load('swoosh_red3.png').convert_alpha()
        self.swoosh_red4 = pygame.image.load('swoosh_red4.png').convert_alpha()
        self.swoosh_red5 = pygame.image.load('swoosh_red5.png').convert_alpha()
        self.swoosh_red6 = pygame.image.load('swoosh_red6.png').convert_alpha()
        self.swoosh_red7 = pygame.image.load('swoosh_red7.png').convert_alpha()
        self.swoosh_red8 = pygame.image.load('swoosh_red8.png').convert_alpha()

        self.wood_shield0 = pygame.image.load('wooden_shield1.png').convert_alpha()
        self.wood_shield1 = pygame.image.load('wooden_shield2.png').convert_alpha()
        self.wood_shield2 = pygame.image.load('wooden_shield3.png').convert_alpha()
        self.wood_shield3 = pygame.image.load('wooden_shield4.png').convert_alpha()
        self.wood_shield4 = pygame.image.load('wooden_shield5.png').convert_alpha()

        self.metal_shield0 = pygame.image.load('metal_shield_0.png').convert_alpha()
        self.metal_shield1 = pygame.image.load('metal_shield_1.png').convert_alpha()
        self.metal_shield2 = pygame.image.load('metal_shield_2.png').convert_alpha()
        self.metal_shield3 = pygame.image.load('metal_shield_3.png').convert_alpha()
        self.metal_shield4 = pygame.image.load('metal_shield_4.png').convert_alpha()
        self.metal_shield5 = pygame.image.load('metal_shield_5.png').convert_alpha()

        self.magic_shield0 = pygame.image.load('magic_shield0.png').convert_alpha()
        self.magic_shield1 = pygame.image.load('magic_shield1.png').convert_alpha()
        self.magic_shield2 = pygame.image.load('magic_shield2.png').convert_alpha()
        self.magic_shield3 = pygame.image.load('magic_shield3.png').convert_alpha()
        self.magic_shield4 = pygame.image.load('magic_shield4.png').convert_alpha()
        self.magic_shield5 = pygame.image.load('magic_shield5.png').convert_alpha()


        self.lightning_animation = [self.lightning0, self.lightning1, self.lightning2, self.lightning3, self.lightning2, self.lightning1, self.lightning0]
        self.fireball_animation = [self.fireball0, self.fireball1, self.fireball2, self.fireball3, self.fireball4, self.fireball5]
        self.meteor_animation = [self.meteor0, self.meteor1, self.meteor2, self.meteor3, self.meteor4, self.meteor5]
        self.swoosh_gray_animation = [self.swoosh_gray0, self.swoosh_gray1, self.swoosh_gray2, self.swoosh_gray3, self.swoosh_gray4, self.swoosh_gray5]
        self.swoosh_blue_animation = [self.swoosh_blue0, self.swoosh_blue2, self.swoosh_blue3, self.swoosh_blue4, self.swoosh_blue5,self.swoosh_blue6, self.swoosh_blue7]
        self.swoosh_red_animation = [self.swoosh_red0, self.swoosh_red1, self.swoosh_red2, self.swoosh_red3, self.swoosh_red4, self.swoosh_red5, self.swoosh_red6, self.swoosh_red7, self.swoosh_red8]
        self.wood_shield_animation = [self.wood_shield0, self.wood_shield1, self.wood_shield2, self.wood_shield3, self.wood_shield4]
        self.metal_shield_animation = [self.metal_shield0, self.metal_shield1, self.metal_shield2, self.metal_shield3, self.metal_shield4, self.metal_shield5]
        self.magic_shield_animation = [self.magic_shield0, self.magic_shield1, self.magic_shield2, self.magic_shield3, self.magic_shield4, self.magic_shield5]
        self.current_sprite = 0
        self.speed = 0.125
        self.repeat_number = 1
        self.count = 0
        if(type == "lightning"):
            self.animation_type = self.lightning_animation
            self.speed = 0.125
            self.repeat_number = 0
        elif(type == "fireball"):
            self.animation_type = self.fireball_animation
            self.speed = 0.2
            self.repeat_number = 0
        elif(type == "meteor"):
            self.animation_type = self.meteor_animation
            self.speed = 0.2
            self.repeat_number = 2
        elif(type == "swoosh_gray"):
            self.animation_type = self.swoosh_gray_animation
            self.speed = 0.2
            self.repeat_number = 2
        elif(type == "swoosh_blue"):
            self.animation_type = self.swoosh_blue_animation
            self.speed = 0.2
            self.repeat_number = 2
        elif(type == "swoosh_red"):
            self.animation_type = self.swoosh_red_animation
            self.speed = 0.2
            self.repeat_number = 2
        elif(type == "wood_shield"):
            self.animation_type = self.wood_shield_animation
            self.speed = 0.2
            self.repeat_number = 0
        elif(type == "metal_shield"):
            self.animation_type = self.metal_shield_animation
            self.speed = 0.2
            self.repeat_number = 0
        elif(type == "magic_shield"):
            self.animation_type = self.magic_shield_animation
            self.speed = 0.2
            self.repeat_number = 0

        self.image = self.animation_type[self.current_sprite]


        self.rect = self.image.get_rect(center=pos)
    def update(self):

        self.current_sprite += self.speed
        if self.current_sprite >= len(self.animation_type):
            self.current_sprite = 0
            if(self.count >= self.repeat_number):
                animation_sprites_list.empty()
            else:
                self.count += 1
        self.image = self.animation_type[int(self.current_sprite)]



class Player(pygame.sprite.Sprite):
    def __init__(self, pos, image):
        super().__init__()
        self.spells = []
        self.image = image
        self.normal_image = image
        self.rect = self.image.get_rect(center=pos)
        self.attack_strength = 5  # placeholder
        self.action = "None"
        self.defense = 5 # placeholder
        self.armor = 0
        self.max_health = 10
        self.health = self.max_health  # placeholder
        self.inventory = {
            "Sword": 1,
            "Shield": 1,
            "Book": 1
        }
        self.has_sword = False
        self.has_shield = False
        self.spells = []

        self.acted = False

    def flip_sprite(self):
        self.image = pygame.transform.flip(self.image, True, False)

    def moveRight(self, speed):
        self.rect.x += speed * speed / 15
        if (self.rect.x < 50):
            self.rect.x = 50
        if (self.rect.x > 1650):
            self.rect.x = 1650

    def moveLeft(self, speed):
        self.rect.x -= speed * speed / 15
        if (self.rect.x < 50):
            self.rect.x = 50
        if (self.rect.x > 1650):
            self.rect.x = 1650

    def moveForward(self, speed):
        self.rect.y += speed * speed / 15
        if (self.rect.y < 60):
            self.rect.y = 60
        if (self.rect.y > 800):
            self.rect.y = 800

    def moveBack(self, speed):
        self.rect.y -= speed * speed / 15
        if (self.rect.y < 60):
            self.rect.y = 60
        if (self.rect.y > 800):
            self.rect.y = 800

    def spell(self):
        print("Cast Spell")
        self.action = "Spell"
        

    def meteor(self):
        self.action = "Meteor"
        meteor = Animations((375, 300), "meteor")
        animation_sprites_list.add(meteor)

    def bolt(self):
        self.action = "Bolt"
        print(self.action)
        bolt = Animations((375, 300), "lightning")
        animation_sprites_list.add(bolt)

    def fireball(self):
        self.action = "Fireball"
        fireball = Animations((375, 300), "fireball")
        animation_sprites_list.add(fireball)

    def attack(self):
        self.action = "Attack"
        print(self.action)
        master_attack = Animations((600,500), "swoosh_red")
        animation_sprites_list.add(master_attack)

    def block(self):
        self.action = "Block"
        print(self.action)
        master_block = Animations((1275, 750), "magic_shield")
        animation_sprites_list.add(master_block)

    def increment_health(self, num):
        self.armor += num
        if self.armor <=0:
            self.health += self.armor
            self.armor = 0
            if self.health <= 0:
                self.visible = False

    def enter_combat(self):
        self.position = self.rect
        self.image = scale_image(self.image, 2)
        position = (1075, 550)
        self.rect.x = position[0]
        self.rect.y = position[1]
        pass

    def exit_combat(self):
        self.image = self.normal_image
        self.rect = self.position
        pass

class still_image(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        super().__init__()
        self.visible = False
        self.image = image
        self.rect = self.image.get_rect(center=pos)

intent_sprites_list = pygame.sprite.Group()
intent_list = []

intent_location = (315,435)
attack_intent_icon = still_image(attack_intent_image, intent_location)
intent_list.append(attack_intent_icon)

defend_intent_icon = still_image(defend_intent_image, intent_location)
intent_list.append(defend_intent_icon)

bolt_intent_icon = still_image(lightning_intent_image, intent_location)
intent_list.append(bolt_intent_icon)

fireball_intent_icon = still_image(fireball_intent_image, intent_location)
intent_list.append(fireball_intent_icon)

meteor_intent_icon = still_image(meteor_intent_image, intent_location)
intent_list.append(meteor_intent_icon)

class health_bar(pygame.sprite.Sprite):
    def __init__(self, image, parent):
        super().__init__()
        self.visible = True
        self.parent = parent
        self.image = pygame.transform.smoothscale(image, (parent.rect.width * parent.health / parent.max_health, 10))
        self.rect = self.image.get_rect(center=(parent.rect.x,parent.rect.y))
        
    def update(self):
        if self.parent.health <= 0:
            self.visible = False
        else:
            self.rect.y = self.parent.rect.y + self.parent.rect.height*1.5
            self.rect.x = self.parent.rect.x + self.parent.rect.width*.25
            self.rect.width = self.parent.rect.width * self.parent.health / self.parent.max_health
            self.image = pygame.transform.smoothscale(self.image, (self.parent.rect.width * self.parent.health / self.parent.max_health, 10))

class shield_bar(pygame.sprite.Sprite):
    def __init__(self, image, parent):
        super().__init__()
        self.visible = True
        self.parent = parent
        self.image = pygame.transform.smoothscale(image, (parent.rect.width * parent.health / parent.max_health, 10))
        self.rect = self.image.get_rect(center=(parent.rect.x,parent.rect.y))
        
    def update(self):
        if self.parent.armor <= 0:
            self.visible = False
        else:
            self.visible = True
            self.rect.y = self.parent.rect.y + self.parent.rect.height*1.5 - 20
            self.rect.x = self.parent.rect.x + self.parent.rect.width*.25
            self.rect.width = self.parent.rect.width * self.parent.armor / self.parent.max_health
            self.image = pygame.transform.smoothscale(self.image, (self.parent.rect.width * self.parent.armor / self.parent.max_health, 10))
        
        
        


timers = []


class timer():
    def __init__(self, duration, callback, start=False):
        super().__init__()
        if start:
            self.timing = True
            self.start_time = pygame.time.get_ticks()

            timers.append(self)

        self.duration = duration * 1000
        self.callback = callback

    def start(self):
        self.start_time = pygame.time.get_ticks()
        self.timing = True
        timers.append(self)

    def update(self):
        if pygame.time.get_ticks() - self.start_time >= self.duration and self.timing:
            self.callback()
            self.time_out()

    def time_out(self):
        timers.remove(self)
        self.timing = False
    


class Action:
    def __init__(self, intent_icon, action):
        self.intent = intent_icon
        self.action = action


def attack(entity, val):
    entity.increment_health(-val)

def burn(entity, strength, duration):
    entity.burn = [strength, duration]

#basic goblin actions: attack, defend
def goblin_attack_function():
    global player
    attack(player, 5)
    attack_anim = Animations((900, 725), "swoosh_red")
    animation_sprites_list.add(attack_anim)
    
goblin_attack = Action(attack_intent_icon, goblin_attack_function)

def goblin_defend_function():
    global enemy_object_list
    enemy_object_list[0].armor += 3
    defend = Animations((400,550), "wood_shield")
    animation_sprites_list.add(defend)

goblin_defend = Action(defend_intent_icon, goblin_defend_function)

#mage goblin actions: fire, bolt
def mage_fireball_function():
    global player
    attack(player, 6)
    fireball = Animations((1275, 600), "fireball")
    animation_sprites_list.add(fireball)

mage_fireball = Action(fireball_intent_icon, mage_fireball_function)

def mage_bolt_function():
    global player
    player.armor = 0
    attack(player, 2)
    attack_anim = Animations((1275, 600), "lightning")
    animation_sprites_list.add(attack_anim)

mage_bolt = Action(bolt_intent_icon, mage_bolt_function)

#Brute goblin actions: empower, attack, attack
brute_strength = 7
def brute_attack_function():
    global player
    global brute_strength
    attack(player, brute_strength)
    attack_anim = Animations((900, 725), "swoosh_gray")
    animation_sprites_list.add(attack_anim)
    

brute_attack = Action(attack_intent_icon, brute_attack_function)

def brute_empower_function():
    global brute_strength
    brute_strength += 1
    defend = Animations((400,550), "magic_shield")
    animation_sprites_list.add(defend)
brute_empower = Action(defend_intent_icon, brute_empower_function)

#boss goblin actions: atk, atk, bolt, defend/empower
temp_strength = 0
def boss_attack_function():
    global player
    global temp_strength
    attack(player, 8 + temp_strength)
    temp_strength = 0
    attack_anim = Animations((900, 725), "swoosh_blue")
    animation_sprites_list.add(attack_anim)
boss_attack = Action(attack_intent_icon, boss_attack_function)

def boss_bolt_function():
    global player
    player.armor = 0
    attack(player, 2)
    attack_anim = Animations((900, 725), "swoosh_red")
    animation_sprites_list.add(attack_anim)
boss_bolt = Action(bolt_intent_icon, boss_bolt_function)

def boss_defend_function():
    global enemy_object_list
    global temp_strength
    temp_strength = 3
    enemy_object_list[0].armor += 1
    defend = Animations((400,550), "magic_shield")
    animation_sprites_list.add(defend)
boss_defend = Action(defend_intent_icon, boss_defend_function)



# goblin_attack = attack(player,
# attack = Action()


# Enemy class takes 3 arguments to initialize
# pos = position of enemy on the map
# image = sprite
# actions = list of actions from the action class, detailed above
class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, image, actions: list, health = 10):
        super().__init__()
        self.image = image
        self.armor = 0
        self.rect = self.image.get_rect(center=pos)
        self.health = health
        self.max_health = self.health
        self.visible = True
        self.starting_actions = actions.copy()
        self.available_actions = actions
        self.current_action = self.available_actions[0]
        self.burn = [0, 0]
        

    def flip_sprite(self):
        self.image = pygame.transform.flip(self.image, True, False)

    def movement(self, end_pos_x, end_pos_y, increments):
        if (((self.rect.x < end_pos_x) and (self.rect.y < end_pos_y)) and (increments % 5 == 0)):
            up_down = random.randint(1, 2)
            if (up_down == 1):
                self.rect.y += random.randint(0, 20)
            else:
                self.rect.x += random.randint(0, 20)

    def increment_health(self, num):
        self.armor += num
        if self.armor <=0:
            self.health += self.armor
            self.armor = 0
            if self.health <= 0:
                self.visible = False

    def intent(self, player):     
        if len(self.available_actions) == 0:
            self.available_actions = self.starting_actions.copy()
        self.current_action = self.available_actions[0]
        self.current_action.intent.visible = True

    def act(self, player):
        self.current_action.action()
        self.current_action.intent.visible = False
        self.available_actions.pop(0)

    def enter_combat(self):
        self.image = scale_image(self.image, 2)
        self.flip_sprite()
        self.rect = each.image.get_rect(center=(315,435))

    def end_step(self):
        if self.burn[1] > 0:
            self.increment_health(-self.burn[0])
            print(self.burn[0])
            print(self.health)
            self.burn[1] -= 1

    def exit_combat(self):
        pass




class Interactable(pygame.sprite.Sprite):
    def __init__(self, pos, image, callback, clickable=True):
        super().__init__()
        self.image = image
        self.image_og = image
        self.clickable = clickable
        self.rect = self.image.get_rect(center=pos)
        self.rect_og = self.image.get_rect(center=pos)
        self.callback = callback
        self.pressed = False

    def update(self, events):
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
    def __init__(self, pos, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=pos)


def on_click():
    ''


def reset_room():
    global enemies_remaining, room_complete
    enemies_remaining = 3
    room_complete = False
    player.rect.x, player.rect.y = 200, 300


player_sprites_list = pygame.sprite.Group()
enemy_sprites_list = pygame.sprite.Group()
menu_sprites_list = pygame.sprite.Group()
animation_sprites_list = pygame.sprite.Group()

player = Player((150, 600), player_image)
player.flip_sprite()
exit_zone = pygame.Rect(WIDTH // 2 - 50, 0, 100, 50)

# callable enemy attacks


goblin = Enemy((225, 250), goblin_image, [goblin_attack, goblin_defend])
goblin2 = Enemy((450,700), goblin_image, [goblin_attack, goblin_defend])
buff_goblin = Enemy((1500, 600), buff_goblin_image, [brute_empower, brute_attack, brute_attack], health = 42)
boss_goblin = Enemy((1500,600), boss, [boss_attack, boss_attack, boss_bolt, boss_defend], health = 40)
magicGoblin = Enemy((825,350), magic_goblin_image, [mage_fireball, mage_bolt], health = 20)

menu_bar = Interactable((1675, 300), menu_image, on_click, clickable=False)
attack_button = Interactable((1675, 150), attack_button_image, player.attack)
spell_button = Interactable((1675, 300), spell_button_image, player.spell)
shield_button = Interactable((1675, 450), shield_button_image, player.block)

meteor_button = Interactable((1675, 150), meteor_button_image, player.meteor)
bolt_button = Interactable((1675, 300), bolt_button_image, player.bolt)
fireball_button = Interactable((1675, 450), fireball_button_image, player.fireball)

player.spells.append(meteor_button)
player.spells.append(bolt_button)
player.spells.append(fireball_button)


room_enemy_list = []
player_sprites_list.add(player)
#room_enemy_list.append(goblin)
#room_enemy_list.append(goblin2)
room_enemy_list.append(magicGoblin)
#room_enemy_list.append(buff_goblin)

for enemy in room_enemy_list:
    enemy_sprites_list.add(enemy)


# contains enemies in current combat as a list of objects
enemy_object_list = []

exit = True
combat_state = False
clock = pygame.time.Clock()
combat_turn = "Start"
enemies_remaining = 3
last_direction_key = pygame.K_0
speed_boost = 1.15
health_bar_list = []
menu_state = "Actions"





def end_player_turn():
    global combat_turn
    if combat_turn == "Player":
        combat_turn = "Enemy"

def use_inventory(item, player):
    if item == "Sword" and not player.has_sword:
        player.attack_strength += 5
        player.has_sword = True
        print("Sword equipped. Attack increased.")

    elif item == "Shield" and not player.has_shield:
        player.armor += 3
        player.has_shield = True
        print("Shield equipped. Armor increased.")

    elif item == "Book":
        possible_spells = ["Lightning", "Fireball", "Meteor"]
        for spell in possible_spells:
            if spell not in player.spells:
                player.spells.append(spell)
                print(f"Learned {spell} spell.")
                break

def draw_inventory(screen, player):
    x, y = 25, 25  # Inventory HUD position
    for item, count in player.inventory.items():
        text = font.render(f"{item}: {count}", True, (255, 255, 255))
        screen.blit(text, (x, y))
        x += 200

room_complete = True

attack_timer = timer(2, end_player_turn)

while exit:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                exit = False
                    # Inventory hotkeys (only work out of combat)
            elif event.key == pygame.K_1 and not combat_state:
                use_inventory("Sword", player)
            elif event.key == pygame.K_2 and not combat_state:
                use_inventory("Shield", player)
            elif event.key == pygame.K_3 and not combat_state:
                use_inventory("Book", player)


    # Background draw (first!)
    screen.blit(dungeon_images[current_dungeon], (0, 0))

    if combat_state == False:
        for each in enemy_sprites_list:
            enemy_object_list.append(each)
            

        if current_dungeon == 0:
            exit_zone = pygame.Rect(852, 66, 192, 192)  # Top-middle
        elif current_dungeon == 1:
            exit_zone = pygame.Rect((842, 800, 192, 192))  # Bottom-middle

        # Show room cleared message
        if room_complete and not game_over:
            text = font.render("Room Cleared! Go to the exit to continue...", True, (255, 255, 255))
            screen.blit(text, (400, 1000))

        #  Check if player leaves room
        if player.rect.colliderect(exit_zone):
            if room_complete:
                current_dungeon += 1
                player.rect = exit_zone
                enemy_object_list.append(boss_goblin)
                enemy_sprites_list.add(boss_goblin)
                if current_dungeon == 2:
                    current_dungeon = 1
                    enemy_sprites_list.empty()
                    #animaiton shtuff
                    exit = False
                else:
                    reset_room()
        count = 0
        for enemy in enemy_object_list:
            if(enemy.visible == False):
                count+= 1
        if(count == len(enemy_object_list)):
            enemy_object_list.clear()
            menu_sprites_list.empty()
            combat_state = False
            room_complete = True

        keys = pygame.key.get_pressed()

        #goblin.movement(random.randint(1, 1800), random.randint(1, 1000), pygame.time.get_ticks())
        #buff_goblin.movement(random.randint(1, 1800), random.randint(1, 1000), pygame.time.get_ticks())
        #magicGoblin.movement(random.randint(1, 1800), random.randint(1, 1000), pygame.time.get_ticks())
        #boss.movement(random.randint(1, 1800), random.randint(1, 1000), pygame.time.get_ticks())

        if keys[pygame.K_a]:
            player.moveLeft(8.5 * speed_boost)
            if (last_direction_key != pygame.K_a):
                player.flip_sprite()
            last_direction_key = pygame.K_a
        if keys[pygame.K_d]:
            player.moveRight(8.5 * speed_boost)
            if (last_direction_key != pygame.K_d):
                player.flip_sprite()
            last_direction_key = pygame.K_d
        if keys[pygame.K_s]:
            player.moveForward(8.5 * speed_boost)
            print(player.rect)
        if keys[pygame.K_w]:
            player.moveBack(8.5 * speed_boost)

        for each in enemy_sprites_list.sprites():
            if ((each.rect.x - 50 < player.rect.x < each.rect.x + 50) and (
                    each.rect.y - 50 < player.rect.y < each.rect.y + 50)):
                enemy_sprites_list.empty()
                enemy_sprites_list.add(each)
                enemy_object_list.clear()
                enemy_object_list.append(each)
                if (last_direction_key == pygame.K_d):
                    player.flip_sprite()
                combat_state = True

    if combat_state == True:
        screen.blit(combat_background, (0,0))
        intent_sprites_list.empty()
        menu_sprites_list.empty()
        menu_sprites_list.add(menu_bar)
        if menu_state == "Actions":
            
            menu_sprites_list.add(attack_button)
            menu_sprites_list.add(spell_button)
            menu_sprites_list.add(shield_button)
        elif menu_state == "Spells":
            #menu_sprites_list.add(menu_button)
            for spell in player.spells:
                menu_sprites_list.add(spell)
                #placement logic? if only 2 can skip
        enemy_sprites_list.empty()
        
                

        if combat_turn == "Start":
            player.enter_combat()
            for enemy in enemy_object_list:
                enemy.intent(player)
                enemy.enter_combat()
                enemy_health_bar = health_bar(health_bar_image, enemy)
                player_health_bar = health_bar(health_bar_image, player)
                health_bar_list.append(enemy_health_bar)
                health_bar_list.append(player_health_bar)
                enemy_shield_bar = shield_bar(shield_bar_image, enemy)
                player_shield_bar = shield_bar(shield_bar_image, player)
                health_bar_list.append(enemy_shield_bar)
                health_bar_list.append(player_shield_bar)
            combat_turn = "Player"
        elif combat_turn == "Player":
            if player.acted == False:
                if player.action == "None":
                    target = 0
                    if keys[pygame.K_d]:
                        target = (target + 1) % len(enemy_object_list)
                    elif keys[pygame.K_a]:
                        target = (target - 1) % len(enemy_object_list)
                elif player.action == "Attack":
                    attack(enemy_object_list[target], player.attack_strength)
                    attack_timer.start()
                    player.acted = True
                elif player.action == "Block":
                    player.armor += player.defense
                    attack_timer.start()
                    player.acted = True
                elif player.action == "Spell":
                    menu_state = "Spells"
                elif player.action == "Back":
                    menu_state = "Menu"
                    attack_timer.start()
                    player.acted = True
                elif player.action == "Meteor":
                    print(player.attack_strength//2)
                    attack(enemy_object_list[target], player.attack_strength//2-1)
                    burn(enemy_object_list[target], player.attack_strength//4+1, 3)
                    attack_timer.start()
                    player.acted = True
                elif player.action == "Bolt":
                    enemy_object_list[target].armor = 0
                    attack(enemy_object_list[target], player.attack_strength - 1)
                    attack_timer.start()
                    player.acted = True
                elif player.action == "Fireball":
                    attack(enemy_object_list[target], player.attack_strength)
                    attack_timer.start()
                    player.acted = True
                    pass
                    
        elif combat_turn == "Enemy":
            for enemy in enemy_object_list:
                enemy.armor = 0
                enemy.act(player)
                enemy.intent(player)
                combat_turn = "End Step"
        elif combat_turn == "End Step": #each turn
            print("Player hp:", player.health)
            for enemy in enemy_object_list:
                print("Enemy hp:", enemy.health)
                enemy.end_step()
            combat_turn = "Player"
            player.acted = False
            player.action = "None"
            
            print("shield Rect:", player_shield_bar.rect)
            print("Health rect:", player_health_bar.rect)
            player.armor = 0
            menu_state = "Actions"
            
            
            
            enemies_left = False
            for enemy in enemy_object_list:
                if enemy.visible == True:
                    enemies_left = True
            if enemies_left == False: #cleanup step
                player.exit_combat()
                for enemy in room_enemy_list:
                    if enemy.visible:
                        enemy_sprites_list.add(enemy)
                combat_turn = "Start"
                menu_sprites_list.empty()
                for bar in health_bar_list:
                    bar.visible == False
                player.max_health += 1
                player.health = player.max_health
                for intent in intent_list:
                    intent.visible = False
                combat_state = False
                player.acted = False

        for enemy in enemy_object_list:
            if enemy.visible:
                enemy_sprites_list.add(enemy)
        for bar in health_bar_list:
            bar.update()
            if bar.visible:
                
                enemy_sprites_list.add(bar)
        for intent in intent_list:
            if intent.visible:
                intent_sprites_list.add(intent)

    

    # Update exit zone dynamically based on dungeon


    # Update & draw everything
    player_sprites_list.update()
    enemy_sprites_list.update()
    intent_sprites_list.update()
    menu_sprites_list.update(events)
    animation_sprites_list.update()

    
    player_sprites_list.draw(screen)
    enemy_sprites_list.draw(screen)
    menu_sprites_list.draw(screen)
    animation_sprites_list.draw(screen)
    intent_sprites_list.draw(screen)

    if not combat_state:
        draw_inventory(screen, player)


    pygame.display.flip()
    clock.tick(60)

    for t in timers:
        t.update()
    #if player.health <= 0:
     #   pygame.quit()

pygame.quit()
