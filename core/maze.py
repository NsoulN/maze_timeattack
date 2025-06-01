#迷路生成・表示用クラス

import random
import pygame

class Maze:
    def __init__(self, width, height, tile_size=40):
        self.width = width
        self.height = height
        self.tile_size = tile_size
        self.maze_data = self.generate_maze()

    def generate_maze(self):
        # 仮の迷路：ランダムに壁（1）と通路（0）を生成
        return [[random.choice([0, 0, 1]) for _ in range(self.width)] for _ in range(self.height)]

    def is_walkable(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.maze_data[y][x] == 0
        return False

    def get_start_position(self):
        # スタートは左上固定
        return (0, 0)

    def get_goal_position(self):
        # ゴールは右下固定
        return (self.width - 1, self.height - 1)

    def draw(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                color = (50, 50, 50) if self.maze_data[y][x] == 1 else (200, 200, 200)
                rect = pygame.Rect(x * self.tile_size, y * self.tile_size,self.tile_size, self.tile_size)
                pygame.draw.rect(screen, color, rect)
