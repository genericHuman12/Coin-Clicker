import pygame

class Upgrade:
    def __init__(self, game, y_pos):
        pygame.init()
        self.rect = pygame.Rect(0,0,200,100)
        self.screen = game.screen
        self.game = game
        self.screen_rect = self.screen.get_rect()
        self.color = (90,90,90)
        self.text_color = (0,0,0)
        self.rect.right = self.screen_rect.right - 20
        self.rect.y = y_pos
        self.title_font = pygame.font.SysFont(None, 48)
        self.descrip_font = pygame.font.SysFont(None, 30)
        self.bank_price = 0.20
        self.printer_price = 15.00

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def bank_text(self):
        title = "Bank"
        price = f"Price: ${self.bank_price:.{2}f}"
        descrip1 = "Gives:"
        descrip2 = "+1 cent per second"
        self.bank_title_image = self.title_font.render(title, True, self.text_color, self.color)
        self.bank_descrip1_image = self.descrip_font.render(descrip1, True, self.text_color, self.color)
        self.bank_descrip2_image = self.descrip_font.render(descrip2, True, self.text_color, self.color)
        self.bank_price_image = self.descrip_font.render(price, True, self.text_color, self.color)
        self.bank_title_image_rect = self.bank_title_image.get_rect()
        self.bank_descrip1_image_rect = self.bank_descrip1_image.get_rect()
        self.bank_descrip2_image_rect = self.bank_descrip2_image.get_rect()
        self.bank_price_image_rect = self.bank_price_image.get_rect()
        self.bank_title_image_rect.midtop = self.rect.midtop
        self.bank_descrip1_image_rect.midtop = self.bank_title_image_rect.midbottom
        self.bank_descrip2_image_rect.midtop = self.bank_descrip1_image_rect.midbottom
        self.bank_price_image_rect.midtop = self.bank_descrip2_image_rect.midbottom
    
    def draw_bank_text(self):
        self.bank_text()
        self.screen.blit(self.bank_title_image, self.bank_title_image_rect)
        self.screen.blit(self.bank_descrip1_image, self.bank_descrip1_image_rect)
        self.screen.blit(self.bank_descrip2_image, self.bank_descrip2_image_rect)
        self.screen.blit(self.bank_price_image, self.bank_price_image_rect)

    def coin_upgrade_text(self):
        if self.game.upgradeNum == 0:
            text = "Upgrade to quarter"
            self.coin_upgrade_price = 0.20
            price = f"Price: ${self.coin_upgrade_price:.{2}f}"
            attribute = "Gives +1 cent/click"
        elif self.game.upgradeNum == 1:
            text = "MAX"
            price = ""
            attribute = "Gives +25 cents/click"
            self.coin_upgrade_price = 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999.00
        self.coin_titl_img = self.title_font.render(text, True, self.text_color, self.color)
        self.coin_price_img  = self.descrip_font.render(price, True, self.text_color, self.color)
        self.coin_attribute_img  = self.title_font.render(attribute, True, self.text_color, self.color)
        self.coin_titl_rect = self.coin_titl_img.get_rect()
        self.coin_titl_rect.midtop = self.rect.midtop
        self.coin_price_rect = self.coin_price_img.get_rect()
        self.coin_price_rect.midtop = self.coin_titl_rect.midbottom
        self.coin_attribute_rect = self.coin_attribute_img.get_rect()
        self.coin_attribute_rect.midbottom = self.game.coin.rect.midtop

    def draw_coin_text(self):
        self.coin_upgrade_text()
        self.screen.blit(self.coin_titl_img, self.coin_titl_rect)
        self.screen.blit(self.coin_price_img, self.coin_price_rect)
        self.screen.blit(self.coin_attribute_img, self.coin_attribute_rect)