import pygame, sys

RED = (255, 0, 0)

def main():
    pygame.init()
    size = 1000, 1000
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("2048")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = False
        rect = pygame.Rect(0, 0, 225, 225)
        pygame.draw.rect(screen, RED, rect)
        rect = pygame.Rect(0, 275, 225, 225)
        pygame.draw.rect(screen, RED, rect)
        rect = pygame.Rect(0, 550, 225, 225)
        pygame.draw.rect(screen, RED, rect)
        rect = pygame.Rect(0, 775, 225, 225)
        pygame.draw.rect(screen, RED, rect)
        pygame.display.flip()
    pygame.quit()
if __name__ == '__main__':
    main()

