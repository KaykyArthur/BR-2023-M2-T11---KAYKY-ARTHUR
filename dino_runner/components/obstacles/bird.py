from dino_runner.components.obstacles.obstacle import Obstacle


class Bird(Obstacle):
    def __init__(self, image, bird_postion):
        self.type = 1
        self.fly_index = 0
        super().__init__(image, self.type)
        self.rect.y = bird_postion

    def update(self, game_speed, obstacles):
        self.fly_index +=1
        if self.fly_index >= 10:
            self.type = 0
            if self.fly_index >= 20:
                self.type = 1
                self.fly_index = 0
        super().update(game_speed, obstacles)

    def draw(self, screen):
        screen.blit(self.image[self.type], (self.rect.x, self.rect.y))