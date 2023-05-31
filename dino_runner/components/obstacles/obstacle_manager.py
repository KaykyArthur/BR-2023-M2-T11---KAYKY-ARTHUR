import pygame
import random 

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            self.obstacle_type = random.choice([SMALL_CACTUS, LARGE_CACTUS, BIRD])
            if self.obstacle_type == SMALL_CACTUS:
                self.obstacles.append(Cactus(self.obstacle_type, 325))
            elif self.obstacle_type == LARGE_CACTUS:
                self.obstacles.append(Cactus(self.obstacle_type, 300))
            elif self.obstacle_type == BIRD:
                self.obstacles.append(Bird(self.obstacle_type, random.choice([215, 300, 250])))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)