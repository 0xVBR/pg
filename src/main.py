"""Main loop"""
import pygame
from background import Background
from player import Player

def main():
    """Main loop"""

    pygame.init()
    window = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("app")
    clock = pygame.time.Clock()

    background = Background()
    player = Player("Elsa")

    background.draw(window)
    player.draw(window)
    pygame.display.update()

    running = True
    while running:
        clock.tick(120)
        frame_time = clock.get_time()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player.move_up()
                if event.key == pygame.K_DOWN:
                    player.move_down()
                if event.key == pygame.K_LEFT:
                    player.move_left()
                if event.key == pygame.K_RIGHT:
                    player.move_right()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    player.stop_up()
                if event.key == pygame.K_DOWN:
                    player.stop_down()
                if event.key == pygame.K_LEFT:
                    player.stop_left()
                if event.key == pygame.K_RIGHT:
                    player.stop_right()

        player.clear(window, background)
        player.update(frame_time)
        player.draw(window)

        pygame.display.update()
    pygame.quit()
    quit()

if __name__ == "__main__":
    main()
