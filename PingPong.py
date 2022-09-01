from pygame import *
import os.path

#game scene
background_color = (0, 128, 0)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(background_color)

#flags responsible for game state
game = True
finish = False
clock = time.Clock()
FPS = 60

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, x, y, speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#Subclass
class Player(GameSprite):
    def RIGHT_UPDATE(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height-80:
            self.rect.y += self.speed
    def LEFT_UPDATE(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height-80:
            self.rect.y += self.speed

filepath = os.path.dirname(__file__)
r = os.path.join(filepath, "racket.png")
t = os.path.join(filepath, "tennis_ball.png")

racket1 = Player(r, 30, 200, 4, 50, 150) #image, x, y, speed, width, height
racket2 = Player(r, 520, 200, 4, 50, 150) #image, x, y, speed, width, height
ball = GameSprite(t, 200, 200, 4, 50, 50) #image, x, y, speed, width, height

font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE', True, (180, 180, 0))
lose2 = font.render('PLAYER 2 LOSE', True, (180, 180, 0))

x = 3
y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish != True:
        window.fill(background_color)
        racket1.LEFT_UPDATE()
        racket2.RIGHT_UPDATE()

        ball.rect.x += x
        ball.rect.y += y

        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            y *=-1

        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            x *= -1

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))

        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (200, 200))
            
        racket1.reset()
        racket2.reset()
        ball.reset()
    
    display.update()
    clock.tick(FPS)
