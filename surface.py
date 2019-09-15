import sys
import pygame as pg

# The Surface is the screen itself, pygame.display.set_mode() creates the main surface.
# Other ways to create surfaces are: image.load() for images, font.render() for just text or Surface() for nothing at all.
# Surface functions are not really relevant, just know:
# blit(surface, coordinates) : Situates a new surface into the main surface
# fill()    : Fill a surface with a solid color
# set_at()  :
# get_at()  :
# IMPORTANT: Use surface.convert(), easy to use and increases blit rate drastically. EX: surface = pygame.image.load('example.png').convert()

def main():

    # Control variables:
    
    game_finished = False

    #####################

    pg.init()

    print 'Creating Surface for the game: '

    screen_size = (1000, 700)                        # Pre-defined static size for the canvas

    screen        = pg.display.set_mode(screen_size) # Creating the main-surface
    back_image    = pg.Surface(screen_size)          # Creating a new surface that will work as the background
    char_standing = pg.image.load('IMG/standing.jpg').convert()

    back_image.fill((255, 255, 255))
    screen.blit(back_image, (0, 0))                  # Disposing our background in the canvas
    screen.blit(char_standing, (260, 350))           # Disposing the main character


    ##### ACTUAL GAME LOOP AND GAME_QUIT #####

    pg.display.flip()                                # Loop for updating the game 
                                                     # Repeats untill the game is finished
    while game_finished == False:

        for event in pg.event.get():

            if event.type == pg.QUIT:               # Event almost mandatory for quiting the game

                game_finished = True

            elif event.type == pg.KEYDOWN:           # Event for realising when a key is getting pressed

                if event.key == pg.K_ESCAPE:

                    game_finished = True

    pg.quit()                                       # Exit pyGame

if __name__ == '__main__':
    main()


# Main tutorial this come from: https://www.pygame.org/docs/tut/newbieguide.html