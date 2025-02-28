import pygame
import sys
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Pocket Dungeon")
    clock = pygame.time.Clock()
    
    player = Player(name="Hero")
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    targx, targy = event.pos
                    player.move_order(targx, targy)
        
        screen.fill((0, 0, 0))
        pygame.draw.circle(screen, (255, 0, 0), (int(player.x), int(player.y)), 10)
        pygame.display.flip()
        clock.tick(60)

    sys.exit()

if __name__ == "__main__":
    main()
