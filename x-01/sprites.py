import pygame as pg
from globals import *

vec = pg.math.Vector2

class SpriteSheet:
    def __init__(self, filename):
        self.spritesheet = pg.image.load(filename).convert()

    def getImage(self, x, y, width, height):
        image = pg.Surface((width, height))
        image.blit(self.spritesheet, (0,0), (x, y, width, height))
        return image


class Player(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((20, 30))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREENWIDTH // 2
        self.rect.centery = SCREENHEIGHT // 2
        self.pos = vec(SCREENWIDTH // 2, SCREENHEIGHT // 2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def jump(self):
        self.rect.y += 1
        hits = pg.sprite.spritecollide(self, self.game.allPlatforms, False)
        self.rect.y -= 1
        if hits:
            self.vel.y = -PLAYER_JUMP


    def update(self):
        self.acc = vec(0, PLAYER_GRAVITY)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC
        
        self.acc.x += self.vel.x * PLAYER_FRICTION
        self.vel += self.acc
        self.pos += self.vel + 0.5*self.acc

        self.rect.midbottom = self.pos


class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
