import pygame,sys
from settings import Settings
from ship import Ship
def run_game():
    #Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #Make a ship
    ship = Ship(screen)
    # Start the main loop for the game.
    count = 0
    while True:
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()
        if count > 5:
            if(ship.rect.x < ship.screen_rect.right):
                ship.rect.x += 1
            else:
                ship.rect.x = ship.screen_rect.left
            count = -1
        count += 1
run_game()