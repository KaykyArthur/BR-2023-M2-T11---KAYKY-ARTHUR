from dino_runner.components.obstacles.obstacle import Obstacle


class Meteor(Obstacle):
    def __init__(self, image):
        self.type = 1
        self.fly_index = 0
        super().__init__(image, self.type)
        self.rect.y = 0

    def update(self, game_speed, obstacles):
        self.fly_index +=1
        if self.fly_index >= 10:
            self.type = 0
            if self.fly_index >= 20:
                self.type = 1
                self.fly_index = 0
        super().update(game_speed, obstacles)

        if self.rect.y < 350:
            self.rect.y += game_speed // 3
            if self.rect.y >= 350:
                self.rect.y = 350