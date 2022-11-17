import random
import pygame
pygame.init()
xgoal1 = random.randint(0,500)
ygoal1 = random.randint(0,500)
xgoal2 = random.randint(0,500)
ygoal2 = random.randint(0,500)
x = 500
y = 500
cyan = (0, 255, 255)
Run = True
win = pygame.display.set_mode((x,y))
class thing1:
    def __init__(self):
        self.y = 0
        self.x = 0
        self.height = 50
        self.width = 50
        #put any thing in the pygame.image.load("")
        self.image = pygame.transform.scale(pygame.image.load("guy.png"), (self.height, self.width))
class thing2:
    def __init__(self):
        self.y = 0
        self.x = 0
        self.height = 50
        self.width = 50
        #put any thing in the pygame.image.load("")
        self.image = pygame.transform.scale(pygame.image.load("dirt.png"), (self.height, self.width))
t1 =thing1()
t2 =thing2()
while Run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Run = False
    win.fill(cyan)
    win.blit(t1.image, (t1.x, t1.y))
    win.blit(t1.image, (t2.x, t2.y))
    m1 = pygame.math.Vector2(xgoal1,ygoal1)
    m2 = pygame.math.Vector2(xgoal2, ygoal2)
    s1 = pygame.math.Vector2(t1.x,t1.y)
    s2 = pygame.math.Vector2(t2.x, t2.y)
    t1.x,t1.y=pygame.math.Vector2.lerp(s1,m1,random.randint(5,50)/100000)
    t2.x, t2.y = pygame.math.Vector2.lerp(s2, m2, random.randint(5, 50) / 100000)
    a = random.randint(1,2500)
    b = random.randint(1, 2500)
    if a == 1:
        xgoal1 = random.randint(0, 500)
        ygoal1 = random.randint(0, 500)
    if b == 1:
        xgoal2 = random.randint(0, 500)
        ygoal2 = random.randint(0, 500)
    pygame.display.update()

