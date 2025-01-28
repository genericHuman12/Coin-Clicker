import pygame
import sys
from coin import Coin
from score import Score
from upgrade import Upgrade
from time import time, sleep # type: ignore

class Clicker:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_rect = self.screen.get_rect()
        self.screen_width = self.screen_rect.width
        self.screen_hieght = self.screen_rect.height
        self.money = 0.00
        self.upgradeNum = 0
        self.cps = 0.00
        self.coin = Coin(self)
        self.money_board = Score(self)
        self.bank = Upgrade(self, 100)
        self.coin_ugrade = Upgrade(self, self.coin.rect.bottom)
        self.coin_ugrade.rect.height -= 50
        self.coin_ugrade.rect.midtop = self.coin.rect.midbottom
        self.printer = Upgrade(self, self.bank.rect.bottom+20)
        pygame.display.set_caption("COIN CLICKER")


    def run_game(self):
        self.tar = time()
        while True:
            self.check_time()
            self.check_events()
            self.coin.update()
            self.money_board.prep_score()
            self.money_board.prep_cps()
            self._update_screen()

    def check_time(self):
        self.tn = time()
        elapsed = round((self.tn-self.tar),2)
        if (elapsed*2)%2 == 0:
            self._update_money()
        sleep(0.005)

    def _update_screen(self):
        self.screen.fill("white")
        self.coin.blitme()
        self.money_board.show_score()
        self.bank.draw()
        self.bank.draw_bank_text()
        self.printer.draw()
        self.printer.draw_printer_text()
        self.coin_ugrade.draw()
        self.coin_ugrade.draw_coin_text()
        pygame.display.flip()

    def _update_money(self):
        self.money += self.cps

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self.check_mouse_events(mouse_pos)

    def check_mouse_events(self, mouse_pos):
        coin_clicked = self.coin.rect.collidepoint(mouse_pos)
        if coin_clicked:
            self.money += self.coin.amt_gained
        bank_clicked = self.bank.rect.collidepoint(mouse_pos)
        if bank_clicked:
            if self.money >= self.bank.bank_price:
                self.cps += 0.01
                self.money -= self.bank.bank_price
                self.bank.bank_price *= 1.05
        coin_ugrade_clicked = self.coin_ugrade.rect.collidepoint(mouse_pos)
        if coin_ugrade_clicked:
            if self.money >= self.coin_ugrade.coin_upgrade_price:
                self.money -= self.coin_ugrade.coin_upgrade_price
                self.upgradeNum += 1
                self.coin.update()
        printer_clicked = self.printer.rect.collidepoint(mouse_pos)
        if printer_clicked:
            if self.money >= self.printer.printer_price:
                self.money -= self.printer.printer_price
                self.cps += 1
                self.printer.printer_price *= 1.05
        

    
click = Clicker()
click.run_game()
