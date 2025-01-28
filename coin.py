import pygame

class Coin:
    def __init__(self, game):
        pygame.init()
        self.game = game
        self.choose_image()
        self.rect = self.image.get_rect()
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.place()
    
    def choose_image(self):
        self.upgradeNum = self.game.upgradeNum
        if self.upgradeNum == 0:
            self.image = pygame.image.load(r'Coin Clicker\images\oneCent.bmp')
            self.amt_gained = 0.01
        elif self.upgradeNum == 1:
            self.image = pygame.image.load(r'Coin Clicker\images\twenfiveCent.bmp')
            self.amt_gained = 0.25
        elif self.upgradeNum == 2:
            self.image = pygame.image.load(r'Coin Clicker\images\dollar.bmp')
            self.amt_gained = 1.00
    
    def update(self):
        self.choose_image()

    def place(self):
        self.rect.x = 7
        self.rect.y = 250
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)
