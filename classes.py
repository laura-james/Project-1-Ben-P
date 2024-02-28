import pygame

# size    = [400,400]
# screen  = pygame.display.set_mode(size)
ground = False


class Sprite(pygame.sprite.Sprite):
    def __init__(self, images, startx, starty):  # constructor method
        super().__init__()

        self.images = [pygame.image.load(image) for image in images]
        self.rect = self.images[0].get_rect()

        self.rect.center = [startx, starty]

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.images[0], self.rect)
        # function to create the player model


class Player(Sprite):

    def __init__(self, startx, starty, direction):
        super().__init__(["sprites/p1_front.png"], startx, starty)
        self.stand_image = self.images

        self.facing_left = False

        self.speed = 4
        self.jumpspeed = 10
        self.vsp = 0  # vertical speed
        self._hsp = 0  # horizontal speed
        self.gravity = 0.8
        self.ground = False
        #self.collide = True
        self.friction = 0.1
        self.hitwallR = False
        self.hitwallL = False
        self.score = 0

    def checkcollision(self, Box, Coin):
        if self.rect.colliderect(Box.rect) and self.vsp > 0 and self.rect.bottom < Box.rect.centery: #check that the bottom of the player is less than the centre of the box (as y is inverse)
            self.ground = True
            self.rect.bottom = Box.rect.top


        if self.rect.colliderect(Coin.rect):
            self.score +=1



        if self.rect.colliderect(Box.rect)   and self.rect.left < Box.rect.right and self.vsp > 0 and self._hsp < 0:
            self.rect.left = Box.rect.right
            self.hitwallL = True
            print("hitwalll")
        else:
            self.hitwallL = False


        if self.rect.colliderect(Box.rect)   and self.rect.right > Box.rect.left and self.vsp > 0 and self._hsp > 0:
            self.rect.right = Box.rect.left
            self.hitwallR = True
            print("hitwallr")
        else:
            self.hitwallR = False


        #if self.rect.colliderect(Coin.rect):
            #self.score += 1
            #so far 


        if self.ground == True:
            #self.rect.y += 1 #moving the player down 1 pixel to ensure that they are still on the ground
            #if self.rect.colliderect(Box.rect):
                self.ground = True


             #   self.rect.y -=1




    def update(self, list):

        key = pygame.key.get_pressed()  # detects if a key is pressed

        if key[pygame.K_LEFT]:

            self._hsp = -self.speed
            self.facing_left = True





        elif key[pygame.K_RIGHT]:

            self._hsp = self.speed - self.friction
            self.facing_left = False

        else:
            self.image = self.stand_image

        if key[pygame.K_UP]:
            if self.ground:
                self.vsp = -self.jumpspeed
                self.ground = False

        if self.ground == False:
            if self.vsp < 10:  # if the player is travelling at less than gravity then gravity will drag the player down
                self.vsp += self.gravity  # adds gravity to the vertical speed to move downwards
        self.move(self._hsp, self.vsp, )

        if self._hsp > 0 and self.facing_left == False:
            self._hsp -= self.friction
        elif self._hsp < 0 and self.facing_left == True:
            self._hsp +=self.friction
        if self.hitwallR == True:
            self._hsp = -self.speed
        else:
            self.hitwallR == False

        if self.hitwallL == True:
            self._hsp = self.speed

        else:
            self.hitwallL == False
#add friction after bouncing off of wall
        self.ground = False
        for Box in list:
            self.checkcollision(Box,Coin)  # loops through the box list checking for collisions

        if self.ground == True:  # while player is on the ground it is set to true
            self.vsp = 0  # when the player is on the ground the vertical speed is set to 0

    def move(self, x, y):
            self.rect.move_ip([x, y])




        # function to move the player
class Coin(Sprite):
    def __init__(self, startx, starty):
        super().__init__(["sprites/coins2.png"], startx, starty)



class Box(Sprite):
    def __init__(self, startx, starty):
        super().__init__(["sprites/boxAlt.png"], startx, starty)




