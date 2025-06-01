#迷路をプレイする画面のクラス

import pygame
import time
from core.maze import Maze
from core.player import Player

class MazeScene:
    def __init__(self, screen, width, height, tile_size=40):
        self.screen = screen
        self.maze = Maze(width, height, tile_size)
        self.player = Player(self.maze, self.maze.get_start_position())
        self.goal = self.maze.get_goal_position()
        self.font = pygame.font.SysFont(None, 24)
        self.start_time = time.time()
        self.is_cleared = False
        self.running = True
        self.clock = pygame.time.Clock()

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False
        elif event.type == pygame.KEYDOWN and not self.is_cleared:
            self.player.handle_key(event.key)

    def update(self):
        if (self.player.x, self.player.y) == self.goal:
            self.is_cleared = True

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.maze.draw(self.screen)
        self.player.draw(self.screen)

        # タイマー表示
        elapsed = int(time.time() - self.start_time)
        text = self.font.render(f"Time: {elapsed}s", True, (255, 255, 255))
        self.screen.blit(text, (10, 10))

        # ゴール表示
        if self.is_cleared:
            goal_text = self.font.render("Goal!!", True, (255, 0, 0))
            self.screen.blit(goal_text, (150, 10))

        pygame.display.flip()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                self.handle_event(event)

            self.update()
            self.draw()
            self.clock.tick(60)  # フレームレートを60FPSに設定
