import pygame
from classes import Box, Player

BACKGROUND = (255, 0, 0)


def main():
    pygame.init()
    BACKGROUND = (255, 0, 0)
    GREEN = (0,255,0)
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((900, 900))


    Tilesize = 40
    width = 12
    height = 12
    DISPLAY = pygame.display.set_mode((width * Tilesize, height * Tilesize))
    Tile = pygame.surface.Surface((Tilesize,Tilesize))
    map1 = [[1,0,0,0,0,0,1,0,0,0,0,0,1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    ]
    player = Player(100, 200, 1)
    boxes = []
    #for bx in range(0, 600, 70):
        #boxes.append(Box(bx, 300))
        #boxes.append(Box(500, 200))
    Tile = []
    while True:
        pygame.event.pump()

        player.update(boxes)

        # Drawing
        screen.fill(BACKGROUND)
        for row in range(height):
            for col in range(width):
                if map1[row][col] == 1:
                    boxes.append(Box(row,col))
                #elif map1[row][col] == 0:
                    #Tile = BACKGROUND
                #DISPLAY.blit(Tile[map1[row][col]],(col * Tilesize,row*Tilesize,Tilesize,Tilesize))




        for box in boxes:
           box.draw(screen)
        player.draw(screen)

        pygame.display.update()
        pygame.display.flip()

        clock.tick(60)


main()
#for bx in range(0, 600, 70):
     #   boxes.append(Box(bx, 300))
    #boxes.append(Box(500, 200))