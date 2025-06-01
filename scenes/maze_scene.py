#迷路をプレイする画面のクラス

import pygame

class MazeScene:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont(None, 36)

    def run(self):
        while True:
            self.screen.fill((10, 10, 60))
            text = self.font.render("Maze Playing... Press ESC to return", True, (255, 255, 255))
            self.screen.blit(text, (80, 250))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return None
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return None
