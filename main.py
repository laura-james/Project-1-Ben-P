import pygame
from classes import Box, Player, Coin

BACKGROUND = (255, 0, 0)


def main():
    pygame.init()
    BACKGROUND = (255, 0, 0)
    GREEN = (0,255,0)
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((900, 900))


    Tilesize = 70
    width = 12
    height = 12
    Coinsize = 72
    DISPLAY = pygame.display.set_mode((width * Tilesize, height * Tilesize))
    boxes = []
    coins = []
    f = open("map.txt")
    mapgrid = f.readlines()
    f.close()

    for row in range(len(mapgrid)):  # loops through rows of map
        maprow = mapgrid[row].strip().split(",")  # splits the string of map.txt into just single 1's and 0's
        for col in range(len(maprow)):  # loops through columns of map
            # print(maprow[col])
            if maprow[col] == "1":  # there is a space before the 1
                boxes.append(Box(col * Tilesize,
                                 row * Tilesize))  # writes to the boxes array the boxes to then be drawn later on
            elif maprow[col] == "2":
                coins.append(Coin(col * Coinsize, row * Coinsize))
    player = Player(150, 600, 1)


    while True:
        pygame.event.pump()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        player.update(boxes,coins)
        # Drawing
        screen.fill(BACKGROUND)
                #elif map1[row][col] == 0:
                    #Tile = BACKGROUND
                #DISPLAY.blit(Tile[map1[row][col]],(col * Tilesize,row*Tilesize,Tilesize,Tilesize))

       #print(boxes)
        for coin in coins:
            coin.draw(screen)
        for box in boxes:
           box.draw(screen)
        player.draw(screen)

        pygame.display.update()
        pygame.display.flip()

        clock.tick(60)


main()
pygame.quit()
#for bx in range(0, 600, 70):
     #   boxes.append(Box(bx, 300))
    #boxes.append(Box(500, 200))
