#ゲーム起動用のクラス

import pygame
import sys
from scenes.title_scene import TitleScene

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Maze Time Attack")
    clock = pygame.time.Clock()

    # 最初のシーンはタイトル画面
    current_scene = TitleScene(screen)

    while True:
        next_scene = current_scene.run()
        if next_scene is None:
            break  # None が返ってきたら終了
        current_scene = next_scene
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
