#Create your own shooter
from pygame import *
from math import *
import pygame
from random import randint,random
import random as Random
pygame.init()
icon = pygame.image.load('Kingsion.png')
pygame.display.set_icon(icon)
infoObject = pygame.display.Info()
win_width = 700
win_height = 500
bulletshoot = 1
#win_width = infoObject.current_w-100
#win_height = infoObject.current_h-100
window = pygame.display.set_mode((win_width,win_height))
#title
display.set_caption("cnonfiguhr")
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height,player_speedy,damage=0):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(width,height))
        self.speed = player_speed
        self.speedy= player_speedy
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.damage = damage
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def create_bullet(self,sx,sy,width,height):
        bullet = Bullet(bulipic,self.rect.centerx,self.rect.top,sx,width,height,sy)
        bullets.add(bullet)
    def fire(self):
        tbu = bulletshoot
        for i in range(0,tbu):
            i+=0.5
            i-=tbu/2
            self.create_bullet((sin(radians(i*180/tbu))*15),(cos(radians(i*180/tbu))*20),15,20)


 
class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speedy
        self.rect.x += self.speed
        if self.rect.y < 0:
            self.kill()
        if self.rect.x > win_width:
            self.kill()
        if self.rect.x < 0:
            self.kill()
    def if_collide(self, sprite):
        return sprite.rect.colliderect(self.rect)
        self.kill()
    def disaplay(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Enemy(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height,player_speedy,damage):
        super().__init__(player_image, player_x, player_y, player_speed, width, height,player_speedy,damage)
        self.player_image = player_image
        self.width = width
        self.height = height
        self.speedx = 0
        self.speedy = player_speed
        self.momemtumx = 0
        self.momemtumy = 1
        self.damage = damage
    def update(self):
        self.resistance = 0.99
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        self.speedy += self.momemtumy*self.resistance
        self.speedy *= self.resistance
        self.speedx += self.momemtumx*self.resistance
        self.speedx *= self.resistance
        self.speediax = self.width/self.speed*6
        if self.speediax <1:
            self.speediax = 1
        if self.speediax > self.width:
            self.speediax = self.width
        self.speediay = self.height/self.speed*12
        if self.speediay <1:
            self.speediay = 1
        if self.speediay > self.height:
            self.speediay = self.height
        if self.rect.x < 0:
            self.rect.x = 0
            self.speedx = 0
        if self.rect.x > win_width - self.width:
            self.rect.x = win_width - self.width
            self.speedx = 0
        self.image = transform.scale(image.load(self.player_image),(self.speediax,self.speediay))
        global lost
        if self.rect.y > win_height or sprite.spritecollide(player,monsters,False):
            self.rect.y = -40
            self.rect.x = randint(80,win_width-80)
            self.momemtumx = (player.rect.x - self.rect.x)/(abs(player.rect.x - self.rect.x)+1)
            self.momemtumx = self.momemtumx/2
            self.speedx = self.speedx/2
            self.speedy = self.speed/2
            self.momemtumy = randint(6,14)/10
            lost += self.damage
    def if_collide(self, sprite):
        return sprite.rect.colliderect(self.rect)
#background
background = transform.scale(image.load("galaxy.jpg"),(win_width,win_height))
#loop
nepic = "asteroid.png"
bulipic = "bullet.png"
poweruip = "bullet.png"
fps = 60
score = 0
lost = 0
defeat = 100
goal = 100
clock = time.Clock()
player = Player("rocket.png",5,win_height-80,10,80,80,0)
monsters = sprite.Group()
powerups = sprite.Group()
fire_sound = mixer.Sound("fire.ogg")
font.init()
font1 = font.SysFont("Serif",36)
font2 = font.SysFont("Serif",80)
finish = False
text_lose = font2.render("YOU LOSE!",True,(255,0,0))
text_win = font2.render("YOU WIN!",True,(255,215,0))

for i in range(6):
    monster = Enemy(nepic,randint(80,win_width-80),-40,randint(1,5),80,80,0,1) 
    monsters.add(monster)
for i in range(3):
    powerup = Enemy(poweruip,randint(80,win_width-80),-40,randint(1,5),10,10,0,0) 
    powerups.add(powerup)
bullets = sprite.Group()
mixer.init()
# mixer.music.load("space.ogg")
# mixer.music.play()
run = True
finish = False
limittimeforpowerup = 3
poweruptime = 0
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                player.fire()
                # fire_sound.play()
    # for bullet in bullets:
    #     bullet.update()
    #     if bullet.if_collide(monsters):
    #         score += 1
    #         bullet.kill()

    #         monster = Enemy(nepic,randint(80,win_width-80),-40,randint(1,5),80,80)
    #         monsters.add(monster)
    if not finish:
        window.blit(background,(0,0))
        player.update()
        player.reset()
        monsters.update()
        monsters.draw(window)
        bullets.update()
        bullets.draw(window)
        powerups.update()
        powerups.draw(window)
        collides = sprite.groupcollide(monsters,bullets,True,True)
        powerilacollides = sprite.groupcollide(powerups,bullets,True,True)
        for d in powerilacollides:
            powerup = Enemy(poweruip,randint(80,win_width-80),-40,randint(1,5),10,10,0,0)
            powerups.add(powerup)
            poweruptime = fps*limittimeforpowerup
        for c in collides:
            score += 1
            monster = Enemy(nepic,randint(80,win_width-80),-40,randint(1,5),80,80,0,1)
            monsters.add(monster)
            if lost > 0:
                lost -= 1
        if lost >= defeat:
            finish = True
            window.blit(text_lose,(200,200))
        if score >= goal:
            finish = True
            window.blit(text_win,(200,200))
        if poweruptime > 0:
            poweruptime -= 1
            bulletshoot = 3
        else:
            bulletshoot = 1
        health = defeat-lost
        text_score = font1.render("Score: "+str(score),True,(255,255,255)) 
        window.blit(text_score,(10,10))
        text_miss = font1.render("Health: "+str(health),True,(255,255,255))
        window.blit(text_miss,(10,40))
        display.update()
        clock.tick(fps)



pygame.quit()

