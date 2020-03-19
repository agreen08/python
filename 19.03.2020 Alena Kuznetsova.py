import pygame
""" Font меняем цвет и шрифт у поверхностей при их совмещении  """
pygame.init()
 
ORANGE = (255, 150, 100)
WHITE = (255, 255, 255)
S_Ser=(170, 170, 170)
RED = (225, 0, 50)
BLUE = (0, 0, 225)
sc = pygame.display.set_mode((600,500))
sc.fill((WHITE))
 
surf1 = pygame.Surface((170,160))
surf1.fill((S_Ser))
X=300
Y=250
rect1 = surf1.get_rect(center=(X, Y))
f1 = pygame.font.Font(None, 46)
b1='МИШЕНЬ'
b2='ПОПАЛ'
text1 = f1.render(b1 , 1, (RED))
 
surf2 = pygame.Surface((100,100))
surf2.fill((ORANGE))
x=80
y=70
rect2 = surf2.get_rect(center=(x,y))
f2 = pygame.font.SysFont(None, 48)
text_k = f2.render('куб', 0, (BLUE))
 
surf1.blit(text1, (10, 60))
surf2.blit(text_k, (10, 30))
 
sc.blit(surf1,rect1)
sc.blit(surf2,rect2)
 
pygame.display.update()#обновить окно
 
while 1:
    a=pygame.event.get()
    for i in a:#выключение игры
        if i.type == pygame.QUIT:
            pygame.quit()
    sc.fill((WHITE))#красим все в белый
    if i.type == pygame.MOUSEBUTTONDOWN:
        #начинаем движение
        rect2.left+=1
        rect2.top+=1
        sc.blit(surf2,rect2)
 
        #вводим условие пересечения/совмещения поверхностей 
        if rect2.left>215 and rect2.left<370 and rect2.top>170 and rect2.top<350:#
            surf1.fill((BLUE))
            text1 = f1.render(b2 , 1, (RED))# меняем текст 
            surf1.blit(text1, (10, 60))
            sc.blit(surf1,rect1)
            sc.blit(surf2,rect2)
 
    sc.blit(surf1,rect1)
    sc.blit(surf2,rect2)
    pygame.display.update()
    pygame.time.delay(20)

#=======================================================================================
    
import pygame
pygame.init()
 
 
def turning(car_surf):  # Function turning car(need for using original car_surf every time)
    if keys[pygame.K_UP] or keys[pygame.K_DOWN] \
            or keys[pygame.K_RIGHT] or keys[pygame.K_LEFT]:
        car_surf = pygame.transform.rotate(car_surf, turn)
        sc.fill(BLACK)
        sc.blit(car_surf, car_rect)
        pygame.display.update()
 
 
# Constants
FPS = 60
SCREEN_SIZE = WIN_WIDTH, WIN_HEIGHT = 800, 800
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
UP = 0
DOWN = 180
RIGHT = -90
LEFT = 90
speed = 3
 
sc = pygame.display.set_mode(SCREEN_SIZE)
sc.fill(BLACK)
clock = pygame.time.Clock()
 
car_surf = pygame.image.load('C:/Users/Dmitry/Desktop/car.png')
car_rect = car_surf.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2))  # Set car in center of screen
sc.blit(car_surf, car_rect)
 
pygame.display.update()
while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
 
    # Change direct car moving with keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        turn = UP
        car_rect.y -= speed
    elif keys[pygame.K_DOWN]:
        turn = DOWN
        car_rect.y += speed
    elif keys[pygame.K_RIGHT]:
        turn = RIGHT
        car_rect.x += speed
    elif keys[pygame.K_LEFT]:
        turn = LEFT
        car_rect.x -= speed
 
    turning(car_surf)
 
    clock.tick(FPS)

