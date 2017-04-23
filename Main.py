#!/usr/bin/env python
"""
fuck you
"""

# Import Modules
import os, pygame, time, random
from pygame.locals import *

if not pygame.font: print ('Warning, fonts disabled')

main_dir = os.path.split(os.path.abspath(__file__))[0]


def main():
    """this function is called when the program starts.
       it initializes everything it needs, then runs in
       a loop until the function returns."""

    # Initialize Everything
    pygame.init()
    screen = pygame.display.set_mode((468, 60))
    pygame.display.set_caption('ReadMe')
    # pygame.mouse.set_visible(0)

    # create the bg
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    # Put Text On The Background, Centered
    if pygame.font:
        font = pygame.font.Font(None, 36)
    text = font.render("Starting...", 1, (10, 10, 10))
    textpos = text.get_rect(centerx=background.get_width() / 2)
    background.blit(text, textpos)

    # Display The Background
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Prepare Game Objects
    clock = pygame.time.Clock()
    phase = 0
    daze = 100

    #Main Loop
    going = True
    while going:
        clock.tick(10)

        # Handle Input Events
        for event in pygame.event.get():
            if event.type == QUIT:
                going = False
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
               going = False

        # Draw Everything
        if daze != 0:
            background.fill((phase * 250, phase * 250, phase * 250))
            text = font.render("НОЧЬ ПОТЕРЯНА!!!", 1, ((1 - phase) * 250, (1 - phase) * 250, (1 - phase) * 250))
            textpos = text.get_rect(centerx=background.get_width() / 2, centery=background.get_height() / 2)
            background.blit(text, textpos)
            screen.blit(background, (0, 0))
            pygame.display.flip()
        else:
            background.fill((random.randrange(250), random.randrange(250), random.randrange(250)))
            text = font.render("УИИИИИИИИ!", 1, (random.randrange(250), random.randrange(250), random.randrange(250)))
            textpos = text.get_rect(centerx=background.get_width() / 2, centery=background.get_height() / 2)
            background.blit(text, textpos)
            screen.blit(background, (0, 0))
            pygame.display.flip()

        if daze != 0:
            daze = daze - 1

        if phase == 1:
            phase = 0
        else:
            phase = 1

    pygame.quit()

# Game Over

#this calls the 'main' function when this script is executed
if __name__ == '__main__':
    main()