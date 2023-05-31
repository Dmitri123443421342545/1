class Settings:
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует статические настройки игры."""
        # Параметры экрана
        self.difficulty_level = None
        self.screen_width = 1200
        self.screen_height = 800
        # Назначение цвета фона
        self.bg_color = (0, 0, 255)
        # Настройки корабля
        self.ship_speed = 15
        self.ship_limit = 3
        # Параметры снаряда
        self.bullet_speed = 20
        self.bullet_width = 40
        self.bullet_height = 40
        # self.bullet_color = (255, 0, 0)
        self.bullets_allowed = 100
        # Настройки инопланетян
        self.alien_speed = 10
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
        # Темп ускорения игры
        self.speedup_scale = 2
        # Как быстро увеличиваются значения очков пришельцев
        self.score_scale = 1.5

    def initialize_dynamic_settings(self):
        """Инициализирует настройки, изменяющихся в ходе игры."""
        if self.difficulty_level == "Легкий":
            self.ship_limit = 5
            self.bullets_allowed = 100
            self.ship_speed = 15
            self.bullet_speed = 20
            self.alien_speed = 10
        elif self.difficulty_level == "Средний":
            self.ship_limit = 3
            self.bullets_allowed = 5
            self.ship_speed = 10
            self.bullet_speed = 15
            self.alien_speed = 5
        elif self.difficulty_level == "Сложный":
            self.ship_limit = 1
            self.bullets_allowed = 3
            self.ship_speed = 3.0
            self.bullet_speed = 6.0
            self.alien_speed = 2.0

        self.fleet_direction = 1

        self.alien_points = 100

    def increase_speed(self):
        """Увеличение настройки скорости и стоимости пришельцев."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)

    def set_difficulty(self, diff_setting):  # Установка уровня сложности
        if diff_setting == "Легкий":
            print("Легкий")
        elif diff_setting == "Средний":
            pass
        elif diff_setting == "Сложный":
            pass
