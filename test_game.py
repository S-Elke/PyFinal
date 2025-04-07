import random
import pygame

WIDTH = 1920
HEIGHT = 1080
SURFACE_COLOR = (79, 7, 26)

pygame.init()

size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Test Game")
font = pygame.font.Font(None, 36)
# Load dungeon backgrounds
dungeon_1 = pygame.image.load("Dungeon 1.1.png").convert()
dungeon_2 = pygame.image.load("Dungeon 3.png").convert()
dungeon_images = [dungeon_1, dungeon_2,]
current_dungeon = 0
room_complete = False
game_over = False

exit_zone = pygame.Rect(0, 0, 0, 0)

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
    def __init__(self, pos, image, combat_image):
        super().__init__()
        self.image = image
        self.normal_image = image
        self.combat_image = combat_image
        self.rect = self.image.get_rect(center=pos)
        self.attack_strength = 5 #placeholder
        self.action = "None"
        self.defense = 0
        self.armor = 5 #placeholder
        self.health = 10 #placeholder

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

    def increment_health(self, num):
        self.health += num
        if self.health <= 0:
            self.visible = False

    def enter_combat(self):
        self.position = self.rect
        position = (250, 240)
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.image = self.combat_image
        pass

    def exit_combat(self, position):
        self.image = self.normal_image
        self.rect = self.position
        pass
        
        
        
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
    def __init__(self, intent_icon, probability, action):
        self.intent_icon = intent_icon
        self.probability = probability
        self.action = action


def attack(entity, val):
    entity.increment_health(val)

#goblin_attack = attack(player, 
#attack = Action()


    
#Enemy class takes 3 arguments to initialize
#pos = position of enemy on the map
#image = sprite
#actions = list of actions from the action class, detailed above
class Enemy(pygame.sprite.Sprite): 
    def __init__(self,pos,image,actions: list):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=pos)
        self.health = 11
        self.visible = True
        self.actions = actions
        self.current_action = self.actions[0]

    def movement(self):
        ""

    def increment_health(self, num):
        self.health += num
        if self.health <= 0:
            self.visible = False;

    def intent(self, player):
        random_action = self.actions[random.randint(1,len(self.actions))]
        self.current_action = random_action

    def act(self, player):
        self.current_action.action()

    def enter_combat(self):
        pass

    def exit_combat(self):
        pass
        
            
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
                        
#callable enemy attacks


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

def reset_room():
    global enemies_remaining, room_complete
    enemies_remaining = 3
    room_complete = False
    player.rect.x, player.rect.y = 200, 300


player = Player((200,300), player_image, player_combat_image)
exit_zone = pygame.Rect(WIDTH // 2 - 50, 0, 100, 50)
goblin1 = Enemy((400, 500), goblin_image, [attack(player, 5)])
goblin2 = Enemy((100, 800), goblin_image, [attack(player, 5)])
magicGoblin = Enemy((600,600), magic_goblin_image, [attack(player, 5)])

menu_bar = Interactable((960,880), menu_image, on_click, clickable = False)
attack_button = Interactable((450, 880), attack_button_image, player.attack)
spell_button = Interactable((950, 880), spell_button_image, player.spell)
shield_button = Interactable((1450, 880), shield_button_image, player.block)

goblin_combat = Enemy((1250, 500) , goblin_combat_image, [attack(player, 5)])

player_sprites_list.add(player)
enemy_sprites_list.add(goblin1)
enemy_sprites_list.add(goblin2)
enemy_sprites_list.add(magicGoblin)

#contains enemies in current combat as a list of objects
enemy_object_list = []

exit = True
combat_state = False
clock = pygame.time.Clock()
combat_turn = "Start"
enemies_remaining = 3

def end_player_turn():
    global combat_turn
    print("Callback ran")
    if combat_turn == "Player":
        combat_turn = "Enemy"

attack_timer = timer(2, end_player_turn)

while exit:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                exit = False

    # Background draw (first!)
    screen.blit(dungeon_images[current_dungeon], (0, 0))

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
            if ((each.rect.x - 50 < player.rect.x < each.rect.x + 50) and
                (each.rect.y - 50 < player.rect.y < each.rect.y + 50)):
                enemy_sprites_list.empty()
                combat_state = True

    if combat_state == True:
        menu_sprites_list.add(menu_bar)
        menu_sprites_list.add(attack_button)
        menu_sprites_list.add(spell_button)
        menu_sprites_list.add(shield_button)
        enemy_object_list.append(goblin_combat)
        enemy_sprites_list.empty()
        for enemy in enemy_object_list:
            if enemy.visible:
                enemy_sprites_list.add(enemy)

        if combat_turn == "Start":
            player.enter_combat()
            for enemy in enemy_object_list:
                enemy.enter_combat()
            combat_turn = "Player"
        elif combat_turn == "Player":
            if player.action == "None":
                target = 0
                if keys[pygame.K_d]:
                    target = (target + 1) % len(enemy_object_list)
                elif keys[pygame.K_a]:
                    target = (target - 1) % len(enemy_object_list)
            elif player.action == "Attack":
                attack(enemy_object_list[target], -player.attack_strength)
                attack_timer.start()
                player.action = "None"
            elif player.action == "Defend":
                player.defense += player.armor
        elif combat_turn == "Enemy":
            for enemy in enemy_object_list:
                enemy.act(player)
                enemy.intent(player)

        if all(not enemy.visible for enemy in enemy_object_list):
            print("Room cleared!")
            enemy_object_list.clear()
            menu_sprites_list.empty()
            combat_state = False
            room_complete = True

    # 🟨 Update exit zone dynamically based on dungeon
    if current_dungeon == 0:
        exit_zone = pygame.Rect(WIDTH // 2 - 50, 0, 100, 50)  # Top-middle
    elif current_dungeon == 1:
        exit_zone = pygame.Rect(WIDTH // 2 - 50, HEIGHT - 50, 100, 50)  # Bottom-middle

    # ✅ Show room cleared message
    if room_complete and not game_over:
        text = font.render("Room Cleared! Go to the exit to continue...", True, (255, 255, 255))
        screen.blit(text, (400, 1000))

    # 🚪 Check if player leaves room
    if player.rect.colliderect(exit_zone) and room_complete:
        current_dungeon += 1
        if current_dungeon >= len(dungeon_images):
            print("Game Over – You Win!")
            exit = False
        else:
            reset_room()

    # 🎮 Update & draw everything
    player_sprites_list.update()
    enemy_sprites_list.update()
    menu_sprites_list.update(events)
    terrain_sprites_list.update()

    player_sprites_list.draw(screen)
    enemy_sprites_list.draw(screen)
    menu_sprites_list.draw(screen)
    terrain_sprites_list.draw(screen)

    pygame.display.flip()
    clock.tick(60)

    for t in timers:
        t.update()

pygame.quit()
