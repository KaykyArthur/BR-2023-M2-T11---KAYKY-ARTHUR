import pygame
import os
pygame.mixer.init()

# Global Constants
TITLE = "Jala Dino Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")
FONT_DIR = os.path.join(os.path.dirname(__file__), "..", "assets", "Fonts")
SOUNDS_DIR = os.path.join(os.path.dirname(__file__), "..", "assets", "Sounds")

# Assets Constants
FONT_STYLE = os.path.join(FONT_DIR, "PressStart2P-Regular.ttf")

ICON = pygame.image.load(os.path.join(IMG_DIR, "DinoWallpaper.png"))

GAME_OVER = pygame.image.load(os.path.join(IMG_DIR, "Other/GameOver.png"))

SOUNDS = [
    pygame.mixer.Sound(os.path.join(SOUNDS_DIR, "collide.wav")),
    pygame.mixer.Sound(os.path.join(SOUNDS_DIR, "smash.wav")),
    pygame.mixer.Sound(os.path.join(SOUNDS_DIR, "power_up.wav")),
]

RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2Hammer1.png")),
]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJump.png"))
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpShield.png"))
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpHammer.png"))

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2Hammer.png")),
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus3.png")),
]

LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3.png")),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird2.png")),
]

METEOR = [
    pygame.image.load(os.path.join(IMG_DIR, 'Meteor/spr_meteor_small.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Meteor/spr_meteor_small2.png')),
]

CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))

HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

EMPTY_HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallEmptyHeart.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"
HAMMER_TYPE = "hammer"
HEART_TYPE = "heart"
METEOR_TYPE = "meteor"