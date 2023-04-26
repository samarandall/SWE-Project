"""
this is our main file for our game

this file contains our main game loop, game class, and the 
main function which will run our game
"""

import pygame, sys
from settings import *
from level import Level


class Game:
    """
    this is our initial class which will run the game
    """

    def __init__(self):
        """
        this is initial setup for our game
        """

        pygame.init()
        self.screen_width, self.screen_height = WIDTH, HEIGHT
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), pygame.RESIZABLE)
        pygame.display.set_caption("SWE PROJECT - The Battle for Sugar Rush : Dallas Gere, Sam Randall, Victor Ekpenyong")
        self.clock = pygame.time.Clock()

        # setting the title of our game

        # if we want then we can set an icon as well
        # Icon = pygame.image.laod("some icon file")
        # pygame.display.set_icon(Icon)

        # making the level
        self.level_one = Level()

        #OST
        main_sound  = pygame.mixer.Sound('../audio/main_ost.ogg')
        main_sound.set_volume(0.7)
        main_sound.play(loops=-1)

    def draw_start_menu(self):
        self.screen.fill((43, 26, 7))
        title_font = pygame.font.Font('../graphics/font/joystix.ttf', 60)
        start_font = pygame.font.Font('../graphics/font/joystix.ttf', 40)
        enter_font = pygame.font.Font('../graphics/font/joystix.ttf', 15)
        controls_font = pygame.font.Font('../graphics/font/joystix.ttf', 40)
        c_font = pygame.font.Font('../graphics/font/joystix.ttf', 15)
        title = title_font.render('The Battle for Sugar Rush', True, (205, 86, 156))
        title_rect = title.get_rect()
        title_rect.center = (self.screen_width // 2, (self.screen_height // 2) - (self.screen_height // 8))
        start_button = start_font.render('Start', True, (255, 255, 255))
        start_button_rect = start_button.get_rect()
        start_button_rect.center = ((self.screen_width // 2) - (self.screen_width // 4), (self.screen_height // 2) + (self.screen_height // 4))
        enter = enter_font.render('(Enter)', True, (205, 86, 156))
        enter_rect = enter.get_rect()
        enter_rect.center = ((self.screen_width // 2) - (self.screen_width // 4), (self.screen_height // 2) + (self.screen_height // 3))
        controls_button = controls_font.render('Controls', True, (255, 255, 255))
        controls_button_rect = controls_button.get_rect()
        controls_button_rect.center = ((self.screen_width // 2) + (self.screen_width // 4), (self.screen_height // 2) + (self.screen_height // 4))
        c = c_font.render('(c)', True, (205, 86, 156))
        c_rect = c.get_rect()
        c_rect.center = ((self.screen_width // 2) + (self.screen_width // 4), (self.screen_height // 2) + (self.screen_height // 3))
        self.screen.blit(title, title_rect)
        self.screen.blit(start_button, start_button_rect)
        self.screen.blit(enter, enter_rect)
        self.screen.blit(controls_button, controls_button_rect)
        self.screen.blit(c, c_rect)
        pygame.display.update()
    
    def draw_pause_menu(self):
        self.screen.fill((43, 26, 7))
        title_font = pygame.font.Font('../graphics/font/joystix.ttf', 80)
        button_font = pygame.font.Font('../graphics/font/joystix.ttf', 60)
        r_font = pygame.font.Font('../graphics/font/joystix.ttf', 25)
        controls_font = pygame.font.Font('../graphics/font/joystix.ttf', 60)
        c_font = pygame.font.Font('../graphics/font/joystix.ttf', 25)
        title = title_font.render('PAUSED', True, (205, 86, 156))
        title_rect = title.get_rect()
        title_rect.center = (self.screen_width // 2, (self.screen_height // 2) - (self.screen_height // 8))
        resume_button = button_font.render('Resume', True, (255, 255, 255))
        resume_button_rect = resume_button.get_rect()
        resume_button_rect.center = ((self.screen_width // 2) + (self.screen_width // 4), (self.screen_height // 2) + (self.screen_height // 4))
        r = r_font.render('(r)', True, (205, 86, 156))
        r_rect = r.get_rect()
        r_rect.center = ((self.screen_width // 2) + (self.screen_width // 4), (self.screen_height // 2) + (self.screen_height // 3))
        controls_button = controls_font.render('Quit', True, (255, 255, 255))
        controls_button_rect = controls_button.get_rect()
        controls_button_rect.center = ((self.screen_width // 2) - (self.screen_width // 4), (self.screen_height // 2) + (self.screen_height // 4))
        c = c_font.render('(Esc)', True, (205, 86, 156))
        c_rect = c.get_rect()
        c_rect.center = ((self.screen_width // 2) - (self.screen_width // 4), (self.screen_height // 2) + (self.screen_height // 3))
        self.screen.blit(title, title_rect)
        self.screen.blit(resume_button, resume_button_rect)
        self.screen.blit(r, r_rect)
        self.screen.blit(controls_button, controls_button_rect)
        self.screen.blit(c, c_rect)
        pygame.display.update()
    
    def draw_game_over(self):
        self.screen.fill((43, 26, 7))
        title_font = pygame.font.Font('../graphics/font/joystix.ttf', 80)
        button_font = pygame.font.Font('../graphics/font/joystix.ttf', 50)
        enter_font = pygame.font.Font('../graphics/font/joystix.ttf', 25)
        title = title_font.render('GAME OVER', True, (159, 0, 24))
        title_rect = title.get_rect()
        title_rect.center = (self.screen_width // 2, (self.screen_height // 2) - (self.screen_height // 8))
        start_menu = button_font.render('Start Menu', True, (255, 255, 255))
        start_menu_rect = start_menu.get_rect()
        start_menu_rect.center = (self.screen_width // 2, (self.screen_height // 2) + (self.screen_height // 4))
        enter = enter_font.render('(Space)', True, (205, 86, 156))
        enter_rect = enter.get_rect()
        enter_rect.center = (self.screen_width // 2, (self.screen_height // 2) + (self.screen_height // 3))
        self.screen.blit(title, title_rect)
        self.screen.blit(start_menu, start_menu_rect)
        self.screen.blit(enter, enter_rect)
        pygame.display.update()
    
    def draw_controls(self):
        self.screen.fill((43, 26, 7))
        title_font = pygame.font.Font('../graphics/font/joystix.ttf', 60)
        text_font = pygame.font.Font('../graphics/font/joystix.ttf', 15)
        button_font = pygame.font.Font('../graphics/font/joystix.ttf', 40)
        enter_font = pygame.font.Font('../graphics/font/joystix.ttf', 15)
        title = title_font.render('Controls', True, (205, 86, 156))
        title_rect = title.get_rect()
        title_rect.center = (self.screen_width // 2, (self.screen_height // 2) - (self.screen_height // 3))
        use_weapon = text_font.render('(Space)', True, (205, 86, 156))
        weapon = text_font.render('Use Weapon', True, (255, 255, 255))
        use_weapon_rect = use_weapon.get_rect()
        use_weapon_rect.center = ((self.screen_width // 2) - (self.screen_width // 16), (self.screen_height // 2) - (self.screen_height // 5))
        weapon_rect = weapon.get_rect()
        weapon_rect.center = ((self.screen_width // 2) + (self.screen_width // 16), (self.screen_height // 2) - (self.screen_height // 5))

        use_spell = text_font.render('(Ctrl)', True, (205, 86, 156))
        spell = text_font.render('Cast Spell', True, (255, 255, 255))
        use_spell_rect = use_spell.get_rect()
        use_spell_rect.center = ((self.screen_width // 2) - (self.screen_width // 16), (self.screen_height // 2) - (self.screen_height // 8))
        spell_rect = spell.get_rect()
        spell_rect.center = ((self.screen_width // 2) + (self.screen_width // 16), (self.screen_height // 2) - (self.screen_height // 8))

        switch_weapon = text_font.render('(q)', True, (205, 86, 156))
        switchW = text_font.render('Switch Weapon', True, (255, 255, 255))
        switch_weapon_rect = switch_weapon.get_rect()
        switch_weapon_rect.center = ((self.screen_width // 2) - (self.screen_width // 16), (self.screen_height // 4) + (self.screen_height // 5))
        switchW_rect = switchW.get_rect()
        switchW_rect.center = ((self.screen_width // 2) + (self.screen_width // 16), (self.screen_height // 4) + (self.screen_height // 5))

        switch_spell = text_font.render('(e)', True, (205, 86, 156))
        switchS = text_font.render('Switch Spell', True, (255, 255, 255))
        switch_spell_rect = switch_spell.get_rect()
        switch_spell_rect.center = ((self.screen_width // 2) - (self.screen_width // 16), (self.screen_height // 4) + (self.screen_height // 3.25))
        switchS_rect = switchS.get_rect()
        switchS_rect.center = ((self.screen_width // 2) + (self.screen_width // 16), (self.screen_height // 4) + (self.screen_height // 3.25))

        pause_control = text_font.render('(p)', True, (205, 86, 156))
        pause = text_font.render('Pause', True, (255, 255, 255))
        pause_control_rect = pause_control.get_rect()
        pause_control_rect.center = ((self.screen_width // 2) - (self.screen_width // 16), (self.screen_height // 4) + (self.screen_height // 2.5))
        pause_rect = pause.get_rect()
        pause_rect.center = ((self.screen_width // 2) + (self.screen_width // 16), (self.screen_height // 4) + (self.screen_height // 2.5))

        move_control = text_font.render('(arrow-keys)', True, (205, 86, 156))
        move = text_font.render('Move Player', True, (255, 255, 255))
        move_control_rect = move_control.get_rect()
        move_control_rect.center = ((self.screen_width // 2) - (self.screen_width // 16), (self.screen_height // 4) + (self.screen_height // 2))
        move_rect = move.get_rect()
        move_rect.center = ((self.screen_width // 2) + (self.screen_width // 16), (self.screen_height // 4) + (self.screen_height // 2))

        start_menu = button_font.render('Start Menu', True, (255, 255, 255))
        start_menu_rect = start_menu.get_rect()
        start_menu_rect.center = (self.screen_width // 2, (self.screen_height // 2) + (self.screen_height // 3))
        enter = enter_font.render('(Esc)', True, (205, 86, 156))
        enter_rect = enter.get_rect()
        enter_rect.center = (self.screen_width // 2, (self.screen_height // 2) + (self.screen_height // 2.5))
        self.screen.blit(title, title_rect)
        self.screen.blit(start_menu, start_menu_rect)
        self.screen.blit(enter, enter_rect)
        self.screen.blit(weapon, weapon_rect)
        self.screen.blit(use_weapon, use_weapon_rect)
        self.screen.blit(spell, spell_rect)
        self.screen.blit(use_spell, use_spell_rect)
        self.screen.blit(switchW, switchW_rect)
        self.screen.blit(switch_weapon, switch_weapon_rect)
        self.screen.blit(switchS, switchS_rect)
        self.screen.blit(switch_spell, switch_spell_rect)
        self.screen.blit(pause, pause_rect)
        self.screen.blit(pause_control, pause_control_rect)
        self.screen.blit(move, move_rect)
        self.screen.blit(move_control, move_control_rect)
        pygame.display.update()
        

    def run(self):
        """
        this is the initial running of the game
        """

        while True:
            keys = pygame.key.get_pressed()
            self.game_state = self.level_one.get_game_state()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.VIDEORESIZE:
                    # Update the screen size
                    self.screen_width, self.screen_height = event.size
                    self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), pygame.RESIZABLE)
            if self.game_state == 'start_menu':
                self.draw_start_menu()
                if keys[pygame.K_RETURN]:
                    self.level_one = Level()
                    self.level_one.update_game_state('game')
                elif keys[pygame.K_c]:
                    self.level_one.update_game_state('controls')
            elif self.game_state == 'pause':
                self.draw_pause_menu()
                self.level_one.pause_the_level()
                if keys[pygame.K_r]:
                    self.level_one.unpause_the_level()
                    self.level_one.update_game_state('game')
                if keys[pygame.K_ESCAPE]:
                    self.level_one.update_game_state('start_menu')
            elif self.game_state == 'game_over':
                self.draw_game_over()
                if keys[pygame.K_SPACE]:
                    self.level_one.update_game_state('start_menu')
            elif self.game_state == 'controls':
                self.draw_controls()
                if keys[pygame.K_ESCAPE]:
                    self.level_one.update_game_state('start_menu')
            else:
                self.screen.fill(WATER_COLOR)
                self.level_one.run()
                pygame.display.update()
                self.clock.tick(FPS)


if __name__ == "__main__":
    game = Game()
    game.run()
