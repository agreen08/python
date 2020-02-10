# здесь подключаются модули
import pygame
 
# здесь определяются константы, классы и функции
FPS = 60
d = 0
# здесь происходит инициация, создание объектов и др.
pygame.init()
pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()
 
# если надо до цикла отобразить объекты на экране
pygame.display.update()
 
# главный цикл
while True:
# задержка
    clock.tick(FPS)
# цикл обработки событий
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        pygame.display.set_caption(str(d))
    d += 1
 
# изменение объектов
# обновление дисплея
    pygame.display.update()
   
#-----------------------------------
import pygame
 
FPS = 60
WIN_WIDTH = 500
WIN_HEIGHT = 140
 
x1=0   #координата х
y1=30   #координата y
d=80        #длина квадрата
w=80        #ширина квадрата
WHITE = (255, 255, 255)#цвет белый
ORANGE = (119, 205, 251)#цвет голубой
 
pygame.init()
clock = pygame.time.Clock()    
sc=pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))#создаем окно игры
 
k=2     #константа направления движения, тут чтобы движение было вначале направо
while 1:
    sc.fill(WHITE)#удаление фигуры
 
    a=pygame.event.get()  # присваиваем переменную, чтобы окно закрылось без зависаний
    for j in a:#закрытие окна
        if j.type==pygame.QUIT:
            pygame.quit()
    pygame.draw.rect(sc, ORANGE, (x1,y1,d,w))#рисуем квадрат
    pygame.display.update()
 
    if x1==WIN_WIDTH-80:#  если кооснулось правой стенки то
        k=-2               #движение в обратную сторону
        x1+=k
    elif x1==0:     # движение влево после того как координата х = 0
        k=2
        x1+=k
    else:           # движение в правую сторону от левой стенки
        x1+=k    
 
    clock.tick(FPS)