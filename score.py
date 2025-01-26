import pygame.font

class Score:

    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.text_color = (30, 30 ,30)
        self.font = pygame.font.SysFont(None, 48)
        self.prep_score()
        self.prep_cps()

    def prep_score(self):
        score_str = f'${self.game.money:.{2}f}'
        self.score_image = self.font.render(score_str, True, self.text_color, "white")
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    
    def prep_cps(self):
        cps_str = f'{self.game.cps:.{2}f} Dollars per second'
        self.cps_image = self.font.render(cps_str, True, self.text_color, "white")
        self.cps_rect = self.cps_image.get_rect()
        self.cps_rect.right = self.score_rect.left - 20
        self.cps_rect.top = 20

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.cps_image, self.cps_rect)
