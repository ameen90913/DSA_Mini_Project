import pygame , os , sys 
import cmn_func as func
from pathlib import Path 
from pygame import mixer
from hanoi import *

pygame.display.set_caption("Data Dash")
class Button:
    def __init__(self, x, y, width, height, text, action=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.action = action

    def draw(self):
        # pygame.draw.rect(screen, BLACK, self.rect)
        func.custom_text(self.text, self.rect.x + self.rect.width // 2, self.rect.y + self.rect.height // 2)
        
# Splash Screen
splash_screen = True
while splash_screen:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    func.screen.fill(func.BLACK)
    func.draw_text("AMEEN MJ ", func.WHITE, func.SCREEN_WIDTH // 2, func.SCREEN_HEIGHT // 4)
    func.draw_text("MANO ", func.WHITE, func.SCREEN_WIDTH // 2, func.SCREEN_HEIGHT // 3)
    func.draw_text("KEVIN ANSLOM", func.WHITE, func.SCREEN_WIDTH // 2, func.SCREEN_HEIGHT // 2)
    pygame.display.flip()
    pygame.time.delay(3000)  # Display splash screen for 2 seconds
    splash_screen = False

# Start Screen
mixer.init()
mixer.music.load(func.file_loc("bg.mp3"))
mixer.music.set_volume(0.7)

start_screen = True
while start_screen:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                start_screen = False
    func.screen.fill(func.BLACK)
    func.screen.blit(func.background_image, (0, 0))
    
    func.custom_text("Data Dash: Adventures in Data Structures", func.SCREEN_WIDTH // 2, func.SCREEN_HEIGHT // 3)
    font = pygame.font.Font(func.file_loc("VerminVibes1989Regular-m77m.ttf"), func.FONT_SIZE)
    func.custom_text("Press Enter to Start",(func.SCREEN_WIDTH // 2), (func.SCREEN_HEIGHT // 2))
    mixer.music.play()
    pygame.display.flip()
    func.clock.tick(func.FPS)

# Menu Screen
menu_screen = True
game_buttons = [
    Button(func.SCREEN_WIDTH // 3, 170, 250, 50, "Ahoy Hanoi!", action=lambda: exec(open(Path(__file__).parent / "hanoi.py").read())),
    Button(func.SCREEN_WIDTH // 3, 270, 250, 50, "Queue Quest", action=lambda: print("Clicked Game 2")),
    Button(func.SCREEN_WIDTH // 3, 370, 250, 50, "Tree Trek", action=lambda: print("Clicked Game 3"))
]

selected_button_index = 0
game_buttons[selected_button_index].hovered = True

while menu_screen:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                selected_button_index = (selected_button_index - 1) % len(game_buttons)
            elif event.key == pygame.K_DOWN:
                selected_button_index = (selected_button_index + 1) % len(game_buttons)
            elif event.key == pygame.K_RETURN:
                # Execute the action of the selected button
                button = game_buttons[selected_button_index]
                if button.action:
                    button.action()
    func.screen.fill(func.BLACK)
    func.screen.blit(func.background_image, (0, 0))
    # draw_text("Game Menu", WHITE, SCREEN_WIDTH // 3, SCREEN_HEIGHT // 4)
    mixer.unpause
    pygame.draw.rect(func.screen, func.PURPLE, game_buttons[selected_button_index].rect, 2)

    # Display game buttons
    for index, button in enumerate(game_buttons):
        button.draw()
        # Draw border around the selected button
        if index == selected_button_index:
            pygame.draw.rect(func.screen, func.YELLOW, button.rect, 3)

    pygame.display.flip()
    func.clock.tick(func.FPS)
