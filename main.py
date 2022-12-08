import pygame as pg
from menu.background import bg
pg.init()

import screen
from button import buttons, funcs_button
from paths import get_path


def run_game():
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        
        screen.win.blit(bg, (0, 0))
        funcs_button.update(screen=screen.win,
                            funcs_dict=funcs_button.funcs_dict
                            )
        
        pg.display.flip()
        screen.clock.tick(screen.fps)
        

run_game()