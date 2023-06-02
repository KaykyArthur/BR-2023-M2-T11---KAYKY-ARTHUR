import random
import pygame

from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.hammer import Hammer
from dino_runner.components.power_ups.heart import Heart
from dino_runner.utils.constants import SOUNDS


class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = 0

    def generate_power_up(self, score):
        if len(self.power_ups) == 0 and self.when_appears == score:
            self.when_appears += random.randint(200, 300)
            self.power_up_type = random.choice([0, 1, 2])
            if self.power_up_type == 0:
                self.power_ups.append(Shield())
            elif self.power_up_type == 1:
                self.power_ups.append(Hammer())
            elif self.power_up_type == 2:
                self.power_ups.append(Heart())

    def update(self, game):
        self.generate_power_up(game.score)
        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if game.player.dino_rect.colliderect(power_up.rect):
                power_up.start_time = pygame.time.get_ticks()
                game.player.type = power_up.type
                SOUNDS[2].play()
                if game.player.type == "shield":
                    game.player.shield = True
                    game.player.hammer = False
                    game.player.has_power_up = True
                    game.player.power_up_time = power_up.start_time + (power_up.duration * 1000)
                    self.power_ups.remove(power_up)
                if game.player.type == "hammer":
                    game.player.shield = False
                    game.player.hammer = True
                    game.player.has_power_up = True
                    game.player.power_up_time = power_up.start_time + (power_up.duration * 1000)
                    self.power_ups.remove(power_up)
                if game.player.type == "heart":
                    if game.lifes < 3:
                        game.lifes += 1
                    game.player.type = "default"
                    self.power_ups.remove(power_up)

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset_power_ups(self):
        self.power_ups = []
        self.when_appears = random.randint(200, 300)