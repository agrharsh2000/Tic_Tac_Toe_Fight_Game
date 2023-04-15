import pygame
import random

pygame.init()
size=(1000,800) 
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Welcome to the Rock Paper Scissor Game")

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

b_left=50
b_right=size[0]-50
b_top=50
b_down=size[1]-50

class RKP(pygame.sprite.Sprite):
    def __init__(self,color,types,img):
        super().__init__()
        self.image= pygame.Surface([40,40])
        self.image=pygame.image.load(img).convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.x=random.randint(b_left, b_right)
        self.rect.y=random.randint(b_top, b_down)
        self.direction =random.choice(["up", "down", "left", "right"])
        self.type=types

    def update(self):
        if self.direction == "up":
            self.rect.y -= 1
        elif self.direction == "down":
            self.rect.y += 1
        elif self.direction == "left":
            self.rect.x -= 1
        elif self.direction == "right":
            self.rect.x += 1
        
        if self.rect.left < b_left:
            self.rect.left = b_left
            self.direction = random.choice(["up","down","right"])
        elif self.rect.right > b_right:
            self.rect.right = b_right
            self.direction = random.choice(["up","down","left"])
        elif self.rect.top < b_top:
            self.rect.top = b_top
            self.direction = random.choice(["left","right","down"])
        elif self.rect.bottom > b_down:
            self.rect.bottom = b_down
            self.direction = random.choice(["left","right","up"])

all_sprites = pygame.sprite.Group()
scissors_group = pygame.sprite.Group()
stones_group = pygame.sprite.Group()
papers_group = pygame.sprite.Group()

scissor_len=50
stone_len=50
paper_len=50
for i in range(150):
    scissor = RKP(WHITE,"scissor",'sci.png')
    all_sprites.add(scissor)
    scissors_group.add(scissor)

# create stones
for i in range(150):
    stone = RKP(RED,"stone",'sto.png')
    all_sprites.add(stone)
    stones_group.add(stone)

# create papers
for i in range(150):
    paper = RKP(GREEN,"paper",'pap.png')
    all_sprites.add(paper)
    papers_group.add(paper)


def rock_paper_scissors(sprite1, sprite2):
    if sprite1.type =="stone" and sprite2.type=="scissor":
        sprite2.kill()

    elif sprite1.type =="scissor" and sprite2.type=="stone":
        sprite1.kill()
   
    elif sprite1.type=="paper" and sprite2.type=="stone":
        sprite2.kill()

    elif sprite1.type=="stone" and sprite2.type=="paper":
        sprite1.kill()
    
    elif sprite1.type=="scissor" and sprite2.type=="paper":
        sprite2.kill()
    
    elif sprite1.type=="paper" and sprite2.type=="scissor":
        sprite1.kill()
     

clock=pygame.time.Clock()
FPS=60
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

   
    all_sprites.update()
    
    
    scissor_stone = pygame.sprite.groupcollide(scissors_group,stones_group,False,False)
    for scissor, stones in scissor_stone.items():
        for stone in stones:
            rock_paper_scissors(stone, scissor)

    stone_paper = pygame.sprite.groupcollide(stones_group,papers_group,False,False)
    for stone, papers in stone_paper.items():
        for paper in papers:
            rock_paper_scissors(paper,stone)

    paper_scissor = pygame.sprite.groupcollide(papers_group,scissors_group,False, False)
    for paper, scissors in paper_scissor.items():
        for scissor in scissors:
            rock_paper_scissors(paper, scissor)
    
    screen.fill(BLACK)


    all_sprites.draw(screen)
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()