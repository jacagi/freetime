import pygame, sys, random

WHITE = (255, 255, 255)
v = [20, 140, 260, 380]
col = 4
fil = 4

def tovectorindex(i, j):
    return i * fil + j

def generatenumber(gamematrix):
    gamematrix[random.choice([i for i in range(0, col * fil) if gamematrix[i] == 0])] = 2

def movedownaux(gamematrix, i, j):
    if gamematrix[tovectorindex(i, j+1)] == 0:
        gamematrix[tovectorindex(i, j+1)] = gamematrix[tovectorindex(i, j)]
        gamematrix[tovectorindex(i, j)] = 0
        if j < fil-2:
            movedownaux(gamematrix, i, j+1)
    elif gamematrix[tovectorindex(i, j+1)] == gamematrix[tovectorindex(i, j)]:
        gamematrix[tovectorindex(i, j+1)] = gamematrix[tovectorindex(i, j+1)] * 2
        gamematrix[tovectorindex(i, j)] = 0

def movedown(gamematrix):
    for i in range(0,col):
        for j in range(fil-2,-1,-1):
            if gamematrix[tovectorindex(i, j)] != 0:
                movedownaux(gamematrix, i, j)

def moveupaux(gamematrix, i, j):
    if gamematrix[tovectorindex(i, j-1)] == 0:
        gamematrix[tovectorindex(i, j-1)] = gamematrix[tovectorindex(i, j)]
        gamematrix[tovectorindex(i, j)] = 0
        if j > 1:
            moveupaux(gamematrix, i, j-1)
    elif gamematrix[tovectorindex(i, j-1)] == gamematrix[tovectorindex(i, j)]:
        gamematrix[tovectorindex(i, j-1)] = gamematrix[tovectorindex(i, j-1)] * 2
        gamematrix[tovectorindex(i, j)] = 0

def moveup(gamematrix):
    for i in range(0,col):
        for j in range(1,fil):
            if gamematrix[tovectorindex(i, j)] != 0:
                moveupaux(gamematrix, i, j)

def moverightaux(gamematrix, i, j):
    if gamematrix[tovectorindex(i+1, j)] == 0:
        gamematrix[tovectorindex(i+1, j)] = gamematrix[tovectorindex(i, j)]
        gamematrix[tovectorindex(i, j)] = 0
        if i < fil-2:
            moverightaux(gamematrix, i+1, j)
    elif gamematrix[tovectorindex(i+1, j)] == gamematrix[tovectorindex(i, j)]:
        gamematrix[tovectorindex(i+1, j)] = gamematrix[tovectorindex(i+1, j)] * 2
        gamematrix[tovectorindex(i, j)] = 0

def moveright(gamematrix):
    for j in range(0,col):
        for i in range(fil-2,-1,-1):
            if gamematrix[tovectorindex(i, j)] != 0:
                moverightaux(gamematrix, i, j)

def moveleftaux(gamematrix, i, j):
    if gamematrix[tovectorindex(i-1, j)] == 0:
        gamematrix[tovectorindex(i-1, j)] = gamematrix[tovectorindex(i, j)]
        gamematrix[tovectorindex(i, j)] = 0
        if i > 1:
            moveleftaux(gamematrix, i-1, j)
    elif gamematrix[tovectorindex(i-1, j)] == gamematrix[tovectorindex(i, j)]:
        gamematrix[tovectorindex(i-1, j)] = gamematrix[tovectorindex(i-1, j)] * 2
        gamematrix[tovectorindex(i, j)] = 0

def moveleft(gamematrix):
    for j in range(0,col):
        for i in range(1,fil):
            if gamematrix[tovectorindex(i, j)] != 0:
                moveleftaux(gamematrix, i, j)

def main():
    gamematrix = [0 for i in range(0, col*fil)]
    pygame.init()
    size = 500, 500
    screen = pygame.display.set_mode(size)
    font = pygame.font.SysFont('Arial', 25)
    pygame.display.set_caption("2048")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    moveup(gamematrix)
                elif event.key == pygame.K_DOWN:
                    movedown(gamematrix)
                elif event.key == pygame.K_LEFT:
                    moveleft(gamematrix)
                elif event.key == pygame.K_RIGHT:
                    moveright(gamematrix)
                generatenumber(gamematrix)
        for i in range(0, fil):
            for j in range(0, col):
                rect = pygame.Rect(v[i], v[j], 100, 100)
                pygame.draw.rect(screen, WHITE, rect)
                vectorindex = tovectorindex(i, j)
                screen.blit(font.render(str(gamematrix[vectorindex]), True, (0, 0, 0)), (v[i] + 40, v[j] + 40))
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()

