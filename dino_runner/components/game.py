import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, FONT_STYLE, HEART, DEFAULT_TYPE
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.score = 0
        self.lifes = 3
        self.collide_count = 0
        self.death_count = 0
        self.high_score = []

        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()    
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()   

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()

        pygame.display.quit()
        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        self.reset_data()
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.update_score()
        self.update_high_score()
        self.update_lifes()
        self.power_up_manager.update(self)

    def update_score(self):
        self.score += 0.5
        if self.score % 100 == 0:
            self.game_speed += 5

    def update_high_score(self):
        self.high_score.append(self.score)

    def update_lifes(self):
        self.lifes -= self.collide_count
        self.collide_count = 0

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255)) # "#FFFFFF"
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.draw_score()
        self.draw_high_score()
        self.draw_lifes()
        self.draw_power_up_time()
        self.power_up_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def draw_text(self, text, size, position):
        font = pygame.font.Font(FONT_STYLE, size)
        text_render = font.render(text, False, (83, 83, 83)) 
        text_rect = text_render.get_rect() 
        text_rect.center = position 
        self.screen.blit(text_render, text_rect)

    def draw_score(self):
        self.draw_text(f"{str(int(self.score)).zfill(5)}", 14, (1000, 50))
    
    def draw_high_score(self):
        self.draw_text(f"HI {str(int(max(self.high_score))).zfill(5)}", 14, (895, 50))

    def draw_lifes(self):
        heart_x = 50

        for i in range(self.lifes):
            self.screen.blit(HEART, (heart_x, 50))
            heart_x += HEART.get_width() + 20
            
    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_up_time - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show >= 0:
                self.draw_text(f"{self.player.type.capitalize()} enabled for {time_to_show} seconds", 18, (500, 40))
            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE


    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.run()

    def show_menu(self):
        self.screen.fill((255, 255, 255))
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2

        if self.death_count == 0:
            self.draw_text("Press any key to start", 18, (half_screen_width, half_screen_height))
        else:
            self.screen.blit(ICON, (half_screen_width - 40, half_screen_height - 200))
            self.draw_text("Press any key to restart", 18, (half_screen_width, half_screen_height))
            self.draw_text(f"HIGH SCORE: {str(int(max(self.high_score))).zfill(5)}", 14, (half_screen_width, half_screen_height + 100))
            self.draw_text(f"DEATHS: {self.death_count}", 14, (half_screen_width, half_screen_height + 200))

            # MOSTRAR MENSAGEM "Press any key to restart"
            # MOSTRAR score ATINGIDO
            # MOSTRAR death_count

            ## Resetar score e game_speed quando uma partida for recomeçada
            ## Criar método para remover repetição de código do texto

        pygame.display.update()  # ou .flip()
        self.handle_events_on_menu()

    def reset_data(self):
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups()
        self.game_speed = 20
        self.score = 0
        self.lifes = 3
        self.player.dino_jump = False