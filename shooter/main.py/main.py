from pygame import* 
from random import randint 
from time import time as timer 
 
font.init() 
font1 = font.Font(None, 80) 
win = font1.render('YOU WIN', True, (255, 255, 255)) 
lose = font1.render('YOU LOSW', True(180, 0, 0)) 
font2 = font.Font(None, 36) 
 
mixer.init() 
mixer_music.load('background_music.mp3') 
mixer_music.play() 
fire_sound = mixer.Sound('fire.ogg') 
 
img_back = 'galaxy.jpg' 
img_hero = 'rocker.png' 
img_bullet = 'bullet.png' 
img_enemy = 'ufo.png' 
img_ast = 'asteroid.png' 
 
score = 0 
goal = 10 
lost = 0 
max_lost = 3  
life = 3 
 
class GameSprite(sprite.Sprite): 
    def init(self, player_image, player_x, player_y, size_x, size_y, player_speed): 
        sprite.Sprite.init(self) 
        self.image = transform.scale(image.load(player_image), (size_x, size_y)) 
        self.speed = player_speed 
        self.rect = self.image.get_rect() 
        self.rect_x = player_x 
        self.rect_y = player_y 
     
    def reset(self): 
        window.blit(self.image, (self.rect.x, self.rect.y)) 
 
class Player(GameSprite): 
    def update(self): 
        keys = key.get_pressed() 
        if keys[K_a] and self.rect.x > 5: 
            self.rect.x -= self.speed 
        if keys[K_d] and self.rect.y < win_wight - 80 : 
            self.rect.y += self.speed 
    def fire(self): 
        bullet = Bullet(img_bullet, self.rect.centerx, self.rect.top, 15, 20, -15) 
        bullets.add(bullet)