#タイトル画面用のクラス

import pygame
from scenes.maze_scene import MazeScene

class TitleScene:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont(None, 48)

    def run(self):
        while True:
            self.screen.fill((30, 30, 30))
            text = self.font.render("Maze Time Attack - Press any key", True, (255, 255, 255))
            self.screen.blit(text, (100, 250))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return None
                elif event.type == pygame.KEYDOWN:
                    return MazeScene(self.screen,10,10)
