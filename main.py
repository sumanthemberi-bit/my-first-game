import pygame
import sys
import random
import time

pygame.init()

class enemy(pygame.sprite.Sprite):

    def __init__(self, group , rect_input , *args):
        super().__init__( group)

        self.image = pygame.transform.scale(i_enemy , size=(20 , 20))
        self.rect = self.image.get_frect()
        self.rect.x = rect_input[0]
        self.rect.y = rect_input[1]



    def update(self , character_position : pygame.Rect):
            # direction_x = (character_position.x - self.rect.x) / (character_position.x - self.rect.x)
            # self.rect.x +=  direction_x * enemy_speed
            # direction_y = (character_position.y - self.rect.x) / (character_position.y - self.rect.x)
            # self.rect.y +=  direction_x * enemy_speed

            direction = pygame.Vector2(character_position.x - self.rect.x ,character_position.y - self.rect.y)
            direction = direction.normalize() if direction else direction
            self.rect.center += direction * enemy_speed

class weapon_1(pygame.sprite.Sprite):
    def __init__(self , group , pos):

        super().__init__(group)

        self.image = pygame.transform.scale(i_weapon_1 , size = (50 ,50))
        self.start_time = time.time()
        self.rect = self.image.get_frect()
        self.rect.center = pos


    def update(self):


        if time.time() - self.start_time >= 1:
            self.kill()

        if 0 > self.rect.x > v_width:
            self.kill()

        if 0 > self.rect.y > v_height: 
            self.kill()

speed = 10
enemy_speed = 5
i_logo_icon = pygame.image.load("assets/images/logo.png") 
i_character = pygame.image.load("assets/images/character_image.png")
i_enemy = pygame.image.load("assets/images/enemy_image.png")
i_weapon_1 = pygame.image.load("assets/images/weapon_1.png")

v_width = 600
v_height = 400

screen = pygame.display.set_mode((v_width , v_height))
pygame.display.set_icon(i_logo_icon)
pygame.display.set_caption("Summe")
clock = pygame.time.Clock()

o_shape = pygame.transform.scale(i_character , (128 , 128) )
v_shape_rect = o_shape.get_frect(center = (80 , 80))
go_down = False

song = pygame.mixer.music.load("assets/sound/O Maahi By AI Modi Voice ( Full Version)  O Maahi  Arijit x Modi  Dunki.mp3")
weapon_sound = pygame.mixer.Sound("assets/sound/Angen ghatram nayne vaktram nyayen rajyam #lavdenbhojyam.mp3")

enemy_spawn = pygame.event.custom_type()
pygame.time.set_timer(enemy_spawn, 500)

enemy_sprite_group = pygame.sprite.Group()
weapon_sprit_group = pygame.sprite.Group()
weapon_cooldown = 11
last_time = time.time()
pygame.mixer.music.play(-1)
while (True):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == enemy_spawn:
            enemy(group=enemy_sprite_group , rect_input=(random.randint(0 , v_width) , random.randint(0 , v_height)))

        
    keypressed = pygame.key.get_pressed()
    mouse_pos = pygame.mouse.get_pos()
    mouse_clicked = pygame.mouse.get_pressed()

    if keypressed[pygame.K_s]:
        v_shape_rect.y += speed

    if keypressed[pygame.K_w]:
        v_shape_rect.y -= speed

    if keypressed[pygame.K_d]:
        v_shape_rect.x += speed

    if keypressed[pygame.K_a]:
        v_shape_rect.x -= speed

    if mouse_clicked[0] and (time.time() - last_time) >= weapon_cooldown:
        weapon_1(weapon_sprit_group , mouse_pos)
        weapon_sound.play()
        last_time = time.time()

    screen.fill("#FFFFFF")
    

    screen.blit(o_shape , v_shape_rect)
    enemy_sprite_group.draw(screen)
    weapon_sprit_group.draw(screen)

    enemy_sprite_group.update(v_shape_rect)
    weapon_sprit_group.update()

    pygame.sprite.groupcollide(enemy_sprite_group , weapon_sprit_group , True , False)


    pygame.display.flip()
    clock.tick(60)



