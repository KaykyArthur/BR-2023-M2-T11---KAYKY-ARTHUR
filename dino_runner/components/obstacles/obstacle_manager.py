import pygame
import random 

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.meteor import Meteor
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD, METEOR, SOUNDS


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            self.obstacle_type = random.choice([SMALL_CACTUS, LARGE_CACTUS, BIRD, METEOR])
            if self.obstacle_type == SMALL_CACTUS:
                self.obstacles.append(Cactus(self.obstacle_type, 325))
            elif self.obstacle_type == LARGE_CACTUS:
                self.obstacles.append(Cactus(self.obstacle_type, 300))
            elif self.obstacle_type == BIRD:
                self.obstacles.append(Bird(self.obstacle_type, random.choice([215, 300, 250])))
            elif self.obstacle_type == METEOR:
                self.obstacles.append(Meteor(self.obstacle_type))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if game.player.has_power_up and game.player.shield:
                    pass
                if game.player.has_power_up and game.player.hammer:
                    self.obstacles.remove(obstacle)
                    SOUNDS[1].play()
                elif game.player.has_power_up == False:
                    game.collide_count += 1
                    self.obstacles.remove(obstacle)
                    SOUNDS[0].play()
                    if game.lifes == 1:
                        pygame.time.delay(500)
                        game.death_count += 1
                        game.playing = False
                    break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []