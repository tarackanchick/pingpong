from pygame import *
from random import randint


window = display.set_mode((700, 500))
display.set_caption('Ping Pong')
background = transform.scale(image.load('bluebackground.png'), (700, 500))

game = True
clock = time.Clock()
FPS = 60
finish = False

font.init()
font = font.SysFont('Arial', 50)
lose1 = font.render('PLAYER 1 LOST', True, (255, 0, 0))
lose2 = font.render('PLAYER 2 LOST', True, (255, 0, 0))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, speed_y, player_x, player_y, length, width):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (length, width))
        self.speed_y = speed_y
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update1(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed_y
        if key_pressed[K_s] and self.rect.y < 400:
            self.rect.y += self.speed_y
    def update2(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed_y
        if key_pressed[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed_y

class Ball(GameSprite):
    def __init__(self, image, speed_x, speed_y, player_x, player_y, length, width):
        super().__init__(image, speed_y, player_x, player_y, length, width)
        self.speed_x = speed_x
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.y <= 0 or self.rect.y >= 470:
            self.speed_y *= -1
player1 = Player('platform.png', 6, 35, 10, 25, 100)
player2 = Player('platform.png', 6, 640, 10, 25, 100)
ball = Ball('Golf_ball.svg.png', 3, 3, 300, 0, 30, 30)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(FPS)
    if not finish:
        window.blit(background, (0, 0))
        player1.reset()
        player1.update1()
        player2.reset()
        player2.update2()
        ball.reset()
        ball.update()
        if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
            ball.speed_x *= -1
        if ball.rect.x <= -30:
            finish = True
            window.blit(lose1, (200, 200))
        if ball.rect.x >= 700:
            finish = True
            window.blit(lose2, (200, 200))