from os import path
import os
import pygame as pg
import random

from globals import *
from sprites import *


class Game:
    def __init__(self):
        pg.init()
        pg.mixer.init()
        self.screen = pg.Surface((SCREENWIDTH, SCREENHEIGHT))
        self.displayScreen = pg.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
        pg.display.set_caption('x-01')
        self.clock = pg.time.Clock()
        self.isGameRunning = True
        self.isFullScreen = False
        self.fontName = pg.font.match_font(FONT_NAME)
        self.loadData()

    def loadData(self):
        self.dir = path.dirname(__file__)
        with open(path.join(self.dir, HS_FILE), 'w') as f:
            try:
                self.highscore = int(f.read())
            except:
                self.highscore = 0


    def new(self):
        self.score = 0
        self.allSprites = pg.sprite.Group()
        self.allPlatforms = pg.sprite.Group()
        self.player = Player(self)
        self.allSprites.add(self.player)
        for plat in PLATFORM_LIST:
            p = Platform(* plat)
            self.allSprites.add(p)
            self.allPlatforms.add(p)
        self.run()

    def run(self):
        self.isMainLoopRunning = True
        while self.isMainLoopRunning:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        self.allSprites.update()
        hits = pg.sprite.spritecollide(self.player, self.allPlatforms, False)
        if hits:
            if self.player.vel.y >= 0:
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = 0

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.IsGameRunning = False
                self.isMainLoopRunning = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.isGameRunning = False
                    self.isMainLoopRunning = False
                if event.key == pg.K_UP:
                    self.player.jump()
                    self.score += 1
                if event.key == pg.K_F1:
                    if not self.isFullScreen:
                        self.displayScreen = pg.display.set_mode((1920, 1080), pg.FULLSCREEN)
                    else:
                        self.displayScreen = pg.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
                        
                    self.isFullScreen = not self.isFullScreen
                    
    def draw(self):
        self.screen.fill(BLACK)
        self.allSprites.draw(self.screen)
        self.drawText(str(self.score), 22, WHITE, SCREENWIDTH // 2, 15)

        self.displayScreen.blit(pg.transform.scale(self.screen, self.displayScreen.get_rect().size), (0, 0))

        pg.display.flip()

    def showStartScreen(self):
        pass

    def showGOScreen(self):
        pass


    def drawText(self, text, size, color, x, y):
        font = pg.font.Font(self.fontName, size)
        textSurface = font.render(text, True, color)
        textRect = textSurface.get_rect()
        textRect.midtop = (x, y)
        self.screen.blit(textSurface, textRect)

# -----------------------------------------------------------------------------
# Start game
# -----------------------------------------------------------------------------
game = Game()
game.showStartScreen()

while game.isGameRunning:
    game.new()
    game.showGOScreen()

pg.quit()
