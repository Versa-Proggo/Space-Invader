import pygame,math, random
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYER_START_X = 370
PLAYER_START_Y = 380
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 4
BULLET_SPEED_Y = 10
COLLISION_DISTANCE = 27
pygame.init()
screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
background = pygame.image.load("assets\bg.png")
pygame.set_display.set_caption("Space Inavader")
icon = pygame.image.load("assets/ufo.png")
pygame.display.set_icon(icon)
playerImg = pygame.image.load('assets/player.png')
playerx = PLAYER_START_X
playery = PLAYER_START_Y
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []