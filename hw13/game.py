#!usr/bin/env python
import pygame
from pygame import Rect, Surface
from pygame.locals import *
from pygame.sprite import Sprite, Group
from random import randrange

##Global variables
#Game things
scrWidth = 600
scrHeight = 800
fps = 30
screen_size = scrWidth,scrHeight
done = False
Playing = True
backg = (0,0,0)
bomb = False

#Player attributes
vLeft = -10
vRight = 10
static = 0
blue = (102,0,255)
green = (0,245,61)


#Bullets
white = (255,255,255)
bRed = (255,51,30)
up = -25
bOrange = (255,128,10)
bOrange2 = (255,100,0)
bombSplode = False
#Enemies
red = (255,10,35)
blue2 = (153,0,51)
yellow = (255,255,100)
yellow2 = (255,200,0)
liBlue = (66,255,246)
#Text

pygame.font.init()
scoreFont = pygame.font.Font(None,25)


############################################################################

class Bullet(Sprite):
    width = 10
    height = 20
    def __init__(self,player):
        Sprite.__init__(self)
        self.rect = Rect(player.rect.midtop,(self.width, self.height))
        self.image = Surface(self.rect.size)
        self.image.fill(bRed)
    def update(self):
        self.rect.y += up
        if self.rect.bottom <0:
            self.kill
    
class bulletEnemy(Sprite):
    width = 10
    height = 15
    def __init__(self,enemy2):
        Sprite.__init__(self)
        self.rect = Rect(enemy2.rect.midbottom,(self.width, self.height))
        self.image = Surface(self.rect.size)
        self.image.fill((0,0,0))
        self.image.set_colorkey((0,0,0))
        pygame.draw.ellipse(self.image,yellow,self.image.get_rect())
    def update(self):
        self.rect.y += 15
        if self.rect.top > scrHeight:
            self.kill
        
############################################################################
class Player(Sprite):
    ##These will control the hitbox and not the way it looks
    width = 39
    height = 40
    health = 10
    score = 0
    bombs = 3
    
    
    def __init__(self):
        Sprite.__init__(self)
        self.dX = static
        #Self . rect, .image
        self.rect = Rect(300,760,self.width,self.height)
        self.image = Surface(self.rect.size)
        self.image.fill((0,0,0))
        self.image.set_colorkey((0,0,0))
        self.shield = 1
        #Player draw
        pygame.draw.ellipse(self.image, blue, self.image.get_rect())
        
    
        

    def damage(self,n):
        "Function to damage player health"
        if self.shield>0:
            self.shield -=1
        else:
            self.health-=n
        if self.health <=0:
            gameData.loseLife()
            self.kill()
            
            
    def update(self):
        #Movement, based on controls and dX
        self.rect.x += self.dX
        if self.rect.right > scrWidth:
            self.dX = static
            self.rect.right = scrWidth - 1
        if self.rect.left < 0:
            self.dX = static
            self.rect.left = 0
        if pygame.sprite.spritecollide(player,enemyGroup,True):
            self.damage(1)
        if pygame.sprite.spritecollide(player,eBulletGroup,True):
            self.damage(1)
        if pygame.sprite.spritecollide(player,enemyGroup2,True):
            self.damage(3)
        if pygame.sprite.spritecollide(player,enemyGroup3,True):
            self.damage(2)
        gameData.scoreCount(player.score)
############################################################################     
class gameData(object):
    def __init__(self):
        self.lives = 3
        self.highScore = 0
    def loseLife(self):
        self.lives-=1
        
            
    def scoreCount(self,score):
        if self.highScore<score:
            self.highScore = score
        else:
            pass
            
        
############################################################################     
class Enemy(Sprite):
    width = 40
    height = 40
    
    y = -40
    
    def __init__(self):
        self.x = randrange(0,scrWidth-self.width)
        Sprite.__init__(self)

        #Self.rect and self.image
        self.rect = Rect((self.x,self.y),(self.width,self.height))
        self.image = Surface(self.rect.size)
        self.image.fill((0,0,0))
        self.image.set_colorkey((0,0,0))

        #Draw stuff
        pygame.draw.ellipse(self.image,red,self.image.get_rect())
        pygame.draw.ellipse(self.image,blue2,self.image.get_rect(),15)

        #Randomly picking trajectory
        self.down = randrange(1,5)
        self.side = randrange(-6,6,4)
    def update(self):
        "Movement behavior"
        
        self.rect.y += self.down
        self.rect.x += self.side
        
        if self.rect.right > scrWidth or self.rect.left < 0:
            self.side *=-1
        if self.rect.top > scrHeight:
            self.kill()



class Enemy2(Sprite):
    y = -50
    health = 3
    width = height = 50
    def __init__(self):
        Sprite.__init__(self)
        self.x = randrange(0,scrWidth-self.width)

        self.rect = Rect((self.x,self.y),(self.width,self.height))
        self.image = Surface(self.rect.size)
        self.image.fill((0,0,0))
        self.image.set_colorkey((0,0,0))
        pygame.draw.ellipse(self.image,yellow,self.image.get_rect())
        
        self.down = 2
        self.side = randrange(-1,1,2)

        self.bombSplode = False
        
            
    def update(self):
        self.rect.x+=self.side
        self.rect.y+=self.down
        if self.rect.right > scrWidth or self.rect.left < 0:
            self.side *=-1
        if self.rect.top > scrHeight:
            self.kill
        if self.health<3:
            pygame.draw.ellipse(self.image,bOrange,self.image.get_rect(),15)
        if self.health<2:
            pygame.draw.ellipse(self.image,(0,0,0),self.image.get_rect(),15)
        if self.bombSplode:
            count = 3
            while count >0:
                pygame.draw.ellipse(self.image,(bORange),self.image.get_rect(),15)
            self.kill
        check = randrange(0,100)
        if check<3:
            eBulletGroup.add(bulletEnemy(self))
       
    def damage(self):
        self.health-=1
        if self.health == 0:
            check = randrange(0,100)
            pygame.draw.ellipse(self.image,bOrange,self.image.get_rect(),15)
            self.kill()
            if check <=10:
                bombGroup.add(Bomb(self))

class Enemy3(Sprite):
    width = 60
    height = 30
    y = -50
    health = 5
    def __init__(self):
        Sprite.__init__(self)
        self.x = randrange(0,scrWidth-self.width)
        self.rect = Rect((self.x,self.y),(self.width,self.height))
        self.image = Surface(self.rect.size)
        self.image.fill((0,0,0))
        self.image.set_colorkey((0,0,0))
        pygame.draw.ellipse(self.image,(liBlue),self.image.get_rect())
        self.down = 1
        self.side = 0
    def update(self,player):
        self.rect.y+=self.down
        if self.rect.x<player.rect.x-70:
            self.side = 2
        elif self.rect.x>player.rect.x+70:
            self.side = -2
        
        self.rect.x+=self.side
        if self.health == 5:
            pygame.draw.ellipse(self.image,green,self.image.get_rect(),15)
        if self.health<5:
            pygame.draw.ellipse(self.image,yellow2,self.image.get_rect(),15)
        if self.health<3:
            pygame.draw.ellipse(self.image,bOrange2,self.image.get_rect(),15)
        if self.health<2:
            pygame.draw.ellipse(self.image,red,self.image.get_rect(),15)
        if self.rect.top > scrHeight:
            self.kill
    def damage(self):
        self.health-=1
        if self.health <=0:
            self.kill()
       
            
        
############################################################################                        
def scoreStuff():
    "Refreshes and draws the scoreboard"
    if player.health>=0:
        scoreboard = "Score: %i|Health: %i|Shield: %i|Bombs: %i|Lives: %i|HighScore: %i"%(player.score,player.health,player.shield,player.bombs,gameData.lives,gameData.highScore)
    if player.health<=0 and gameData.lives>0:
        scoreboard = "Press ENTER for next life"
    elif gameData.lives<=0:
        scoreboard = "GAME OVER. Press ENTER for NEW GAME"
    text = scoreFont.render(scoreboard,True,(255,255,255),backg)
    textpos = text.get_rect()
    textpos.centerx = screen.get_rect().centerx
    return text,textpos




############################################################################
class Star(Sprite):
    y = -40
    def __init__(self):
        Sprite.__init__(self)
        self.size = randrange(5,10)
        self.x = randrange(0,scrWidth-self.size)
        
        self.rect = Rect((self.x,self.y),(self.size,self.size))
        self.image = Surface(self.rect.size)
        self.image.fill((0,0,0))
        self.image.set_colorkey((0,0,0))
        pygame.draw.ellipse(self.image,white,self.image.get_rect())
    def update(self):
        self.rect.y+= 5
        if self.rect.y> scrHeight:
            self.kill
############################################################################
class Shield(Sprite):
    def __init__(self,enemy):
        Sprite.__init__(self)
        self.size = 20
        self.rect = Rect((enemy.rect.x,enemy.rect.y),(self.size,self.size))
        self.image = Surface(self.rect.size)
        self.image.fill((0,0,0))
        self.image.set_colorkey((0,0,0))
        pygame.draw.rect(self.image,green,self.image.get_rect())
    def update(self):
        self.rect.y+=3    
        if self.rect.y>scrHeight:
            self.kill
class Bomb(Sprite):
    def __init__(self,enemy):
        Sprite.__init__(self)
        self.size = 20
        self.rect = Rect((enemy.rect.x,enemy.rect.y),(self.size,self.size))
        self.image = Surface(self.rect.size)
        self.image.fill((0,0,0))
        self.image.set_colorkey((0,0,0))
        pygame.draw.rect(self.image,(200,0,10),self.image.get_rect())
    def update(self):
        self.rect.y+=5    
        if self.rect.y>scrHeight:
            self.kill
    
############################################################################
##Pygame inits
pygame.init()
screen = pygame.display.set_mode((scrWidth,scrHeight))
clock = pygame.time.Clock()
pygame.key.set_repeat(100,100)

##Player
player = Player()
playerGroup = pygame.sprite.GroupSingle(player)
gameData = gameData()

##Stars and Shields and Bombs
starGroup = pygame.sprite.Group()
shieldGroup = pygame.sprite.Group()
bombGroup = pygame.sprite.Group()

##Bullets
bulletGroup = pygame.sprite.Group()
eBulletGroup = pygame.sprite.Group()

##Enemies
enemyGroup = pygame.sprite.Group()
enemyGroup2 = pygame.sprite.Group()
enemyGroup3 = pygame.sprite.Group()
############################################################################

while not done:
    ##Quit and Game Start/Restar controls
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type == QUIT:
            done = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            done = True
        ##Left/right controls
        if keys[K_LEFT]:
            player.dX = vLeft
        elif keys[K_RIGHT]:
            player.dX = vRight
        elif not keys[K_LEFT] and not keys[K_RIGHT]:
            player.dX = static
        ##Shooting controls
        if event.type == KEYDOWN and event.key == K_SPACE and player.health > 0:
            bulletGroup.add(Bullet(player))
        ##New Game controls
        if event.type == KEYDOWN and event.key == K_RETURN and gameData.lives>0 and player.health==0:
            player = Player()
            playerGroup = pygame.sprite.GroupSingle(player)
            eBulletGroup.empty()
            enemyGroup.empty()
            enemyGroup2.empty()
            enemyGroup3.empty()
        if event.type == KEYDOWN and event.key == K_RETURN and gameData.lives<=0:
            player = Player()
            playerGroup = pygame.sprite.GroupSingle(player)
            eBulletGroup.empty()
            enemyGroup.empty()
            enemyGroup2.empty()
            enemyGroup3.empty()
            gameData.highScore = 0
            gameData.lives = 3
        #Bomb controls (IN PROGRESS)
        if event.type == KEYDOWN and event.key == K_LSHIFT and player.health > 0 and player.bombs >0:
            bomb = True
            enemyGroup2.empty()
            enemyGroup3.empty()
            eBulletGroup.empty()
            enemyGroup.empty()
            
            player.bombs-=1
            
    
    # update
    check = randrange(0,200)
    if check <= 10:
        enemyGroup.add(Enemy())
    if check <=2:
        enemyGroup2.add(Enemy2())
    if check <=1:
        enemyGroup3.add(Enemy3())
    if check<=30:
        starGroup.add(Star())
    text,textpos = scoreStuff()

    ##updating groupS
    playerGroup.update()
    bulletGroup.update()
    enemyGroup.update()
    enemyGroup2.update()
    enemyGroup3.update(player)
    eBulletGroup.update()
    starGroup.update()
    bombGroup.update()
    shieldGroup.update()
    
    ##Checking collisions
    for enemy in pygame.sprite.groupcollide(bulletGroup,enemyGroup,True,True):
        pygame.draw.ellipse(enemy.image,bOrange,enemy.image.get_rect())
        if check <= 20:
            shieldGroup.add(Shield(enemy))
        player.score+=1
        
    if pygame.sprite.groupcollide(playerGroup,shieldGroup,False,True):
        player.shield+=1
        
    if pygame.sprite.groupcollide(playerGroup,bombGroup,False,True):
        if player.bombs <5:
            player.bombs+=1
    
    
    for enemyTwo in pygame.sprite.groupcollide(enemyGroup2,bulletGroup,False,True):
        enemyTwo.damage()
        player.score+=1

    for enemyThree in pygame.sprite.groupcollide(enemyGroup3,bulletGroup,False,True):
        
        enemyThree.damage()
        player.score+=1
    clock.tick(fps)
    # draw
    screen.fill((backg))
    starGroup.draw(screen)
    playerGroup.draw(screen)
    shieldGroup.draw(screen)
    if player.shield>0:
        pygame.draw.arc(player.image,green,player.image.get_rect(),0,6.28)
    else:
        pygame.draw.arc(player.image,(0,0,0),player.image.get_rect(),0,6.28)
    bulletGroup.draw(screen)
    enemyGroup.draw(screen)
    enemyGroup2.draw(screen)
    enemyGroup3.draw(screen)
    eBulletGroup.draw(screen)
    bombGroup.draw(screen)
    if bomb:
        pygame.draw.rect(screen,white,(0,0,scrWidth,scrHeight))
        bomb = False
    screen.blit(text,textpos)
    
    
    pygame.display.flip()
pygame.quit()
print "Program complete"
