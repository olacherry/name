from pygame import *

class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, player_speed, scale_player_x, scale_player_y):
       super().__init__()
       self.image = transform.scale(image.load(player_image), (scale_player_x, scale_player_y)) #вместе 55,55 - параметры
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
       self.point = 0


   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y>5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed 
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y>5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed 

racket1 = Player('racket.png', 30, 200, 4, 50,150)
racket2 = Player('racket.png', 520, 200, 4, 50, 150)
ball = Player('ball.png', 200, 300, 4, 50,50)


back = (100,20,190)
win_height = 500
win_width = 600
window = display.set_mode((win_width, win_height))
window.fill(back)

clock = time.Clock()
FPS = 60
finish = False
game = True

speed_x = 3
speed_y = 3

font.init()
font = font.Font(None, 35)
lose1 = font.render('ИГРОК 1 ПРОИГРАЛ!', True, (180, 40, 30))
lose2 = font.render('ИГРОК 2 ПРОИГРАЛ!', True, (180, 40, 30))



point_text = font.render('СЧЕТ:'+ str(racket1.point)+ 'vs'+ str(racket2.point), True, (255, 255, 255))


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish != True:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        window.blit(point_text, (150, 5))

   

        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
            racket1.point += 1
        if ball.rect.y < 0 or ball.rect.y > 450:
            speed_y *= -1

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200,200))
            game_over = True

        if ball.rect.x > 600:
            finish = True
            window.blit(lose2, (200,200))
            game_over = True





        racket1.reset()
        racket2.reset()
        ball.reset()
        
        



    window.blit(point_text, (150, 5))
    display.update()
    clock.tick(FPS)