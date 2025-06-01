#プレイヤーの状態・操作をまとめたクラス

import pygame

class Player:
    def __init__(self, maze, start_pos):
        self.maze = maze
        self.x, self.y = start_pos
        self.color = (0, 0, 255)

    def move(self, dx, dy):
        new_x = self.x + dx
        new_y = self.y + dy
        if self.maze.is_walkable(new_x, new_y):
            self.x = new_x
            self.y = new_y

    def handle_key(self, key):
        if key == pygame.K_UP:
            self.move(0, -1)
        elif key == pygame.K_DOWN:
            self.move(0, 1)
        elif key == pygame.K_LEFT:
            self.move(-1, 0)
        elif key == pygame.K_RIGHT:
            self.move(1, 0)

    def draw(self, screen):
        size = self.maze.tile_size
        rect = pygame.Rect(self.x * size, self.y * size, size, size)
        pygame.draw.rect(screen, self.color, rect)
