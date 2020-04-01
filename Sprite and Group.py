""" добавление звука  """
from random import randint
import pygame
pygame.init()
pygame.time.set_timer(pygame.USEREVENT, 2000)
W = 400
H = 400
WHITE = (255, 255, 255)
 
sc = pygame.display.set_mode((W, H))
CARS=('car.bmp', 'car1.bmp')
CARS_SURF=[]
 
pygame.mixer.music.load('Песенка паровозика.mp3')
pygame.mixer.music.play()
 
sound1 = pygame.mixer.Sound('boom.wav')
 
for i in range(len(CARS)):
    CARS_SURF.append(pygame.image.load(CARS[i]).convert())
 
class Car(pygame.sprite.Sprite):
    def __init__(self, x, surf,group):
        pygame.sprite.Sprite.__init__(self)
        self.image = surf
        self.rect = self.image.get_rect(center=(x, W))
        self.add(group)
        self.speed=(randint(1,5))
        self.image.set_colorkey((255,255,255))
    def update(self):
        if self.rect.y > -100:
            self.rect.y -= self.speed
        else:
            self.kill
 
cars = pygame.sprite.Group()#
Car(randint(25,W-25), CARS_SURF[0],cars)
 
class Car_up(pygame.sprite.Sprite):
    def __init__(self,x,surf):
        pygame.sprite.Sprite.__init__(self)
        self.image = surf
        self.rect = self.image.get_rect(center=(x, 50))
        self.image.set_colorkey((255,255,255))
 
car_up=Car_up(200, CARS_SURF[1])
sc.blit(car_up.image, car_up.rect)#
 
while 1:
    a=pygame.event.get()
    for i in a:
        if i.type== pygame.USEREVENT:#        
            Car(randint(25,W-25), CARS_SURF[0],cars)
 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        car_up.rect.x+=2
    elif keys[pygame.K_LEFT]:
        car_up.rect.x-=2
 
    if pygame.sprite.spritecollide(car_up,cars,False):
        sound1.play()
        pygame.time.delay(int(sound1.get_length())*1000)
        
        pygame.quit()
 
    sc.fill(WHITE)#
    cars.draw(sc)
    sc.blit(car_up.image, car_up.rect)
    pygame.display.update()
    pygame.time.delay(20)
    cars.update()#обновить класс машин
    
#------------------------------------------------------------------
    
from random import randint
import pygame
pygame.init()
pygame.time.set_timer(pygame.USEREVENT, 250)
 
FPS = 24
W = 600
H = 800
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
CARS = ('/home/user/Изображения/car1.png', '/home/user/Изображения/car2.png', \
        '/home/user/Изображения/car3.png')
CARS_SURF = []  
motion = 'STOP'
clock = pygame.time.Clock()
font = pygame.font.Font(pygame.font.match_font('dejavusans'), 36)
text1 = font.render('Game over', 1, (180,0,0))
 
sc = pygame.display.set_mode((W, H))
 
for i in range(len(CARS)):
    CARS_SURF.append(pygame.image.load(CARS[i]).convert_alpha())
 
 
class Car(pygame.sprite.Sprite):
    def __init__(self, x, surf, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = surf
        self.rect = self.image.get_rect(center=(x, 0))
        self.add(group)
        self.speed = randint(1, 3)  
 
    def update(self):
        if self.rect.y < H:
            self.rect.y += self.speed
        else:
            self.kill()
 
class User_car(pygame.sprite.Sprite):
    def __init__(self, x, surf):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.rotate(surf, 180)
        self.rect = self.image.get_rect(center=(x, H))
 
cars = pygame.sprite.Group()
 
Car(randint(1, W), CARS_SURF[randint(0, 2)], cars)
user_car1 = User_car(randint(1, W), CARS_SURF[randint(0, 2)])
 
while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            break
        elif i.type == pygame.USEREVENT:
            Car(randint(1, W), CARS_SURF[randint(0, 2)], cars)
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                motion = 'LEFT'
            elif i.key == pygame.K_RIGHT:
                motion = 'RIGHT'
            elif i.key == pygame.K_UP:
                motion = 'UP'
            elif i.key == pygame.K_DOWN:
                motion = 'DOWN'            
            else:
                motion = 'STOP'
 
    if motion == 'LEFT':
        user_car1.rect[0] -= 3
    elif motion == 'RIGHT':
        user_car1.rect[0] += 3
    elif motion == 'UP':
        user_car1.rect[1] -= 3
    elif motion == 'DOWN':
        user_car1.rect[1] += 3
 
    if pygame.sprite.spritecollideany(user_car1, cars) != None:
        sc.fill(BLACK)
        sc.blit(text1, (W//2,H//2))
        pygame.display.update()
        break
    else:
        sc.fill(WHITE)
        sc.blit(user_car1.image, user_car1.rect)
        cars.draw(sc)
        pygame.display.update()
        cars.update()
 
    pygame.time.delay(FPS)