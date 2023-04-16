import os, time, pygame
from states.state import State
from states.game_rule_2 import Game_rule_2

class Game_rule_1(State):
    def __init__(self, game):
        State.__init__(self, game)
        
        self.Home_button = Button("HOME", 20, (255, 255, 255), (0, 0, 0), (85, 33), (829, 79))
        self.Categgory_button = Button("CATEGORY", 20, (255, 255, 255), (0, 0, 0), (154, 33), (933, 79))
        self.Mylist_button = Button("MY LIST", 20, (255, 255, 255), (0, 0, 0), (123, 33), (1097, 79))
        self.Back = Button("BACK", 20, (255, 255, 255), (0, 0, 0), (85, 33), (153, 79))
        self.Bg = Button("", 20, (255, 255, 255), (255, 255, 255), (986, 670), (307, 180))
        
        
        self.Good = Button("", 20, (255, 255, 255), (255, 255, 255), (237, 176), (510, 362))
        self.Bad = Button("", 20, (255, 255, 255), (255, 255, 255), (237, 180), (510, 565))
        
        
        self.Next_page = Button("Next page >>", 28, (255, 255, 255), (219, 160, 90, 0), (181, 25), (1088, 785))
        
        
    def update(self, delta_time, action):
        # self.buttons['Home_button'] = Button(self.display, "HOME", 20, (255, 255, 255), (255, 0, 0), (85, 33), (749, 49))
        # self.buttons['Categgory_button'] = Button(self.display, "CATEGORY", 20, (255, 255, 255), (0, 255, 0), (154, 33), (854, 49))
        # self.buttons['Mylist_button'] = Button(self.display, "MY LIST", 20, (255, 255, 255), (0, 0, 255), (123, 33), (1018, 49))
        
        self.game.reset_keys()
        self.Home_button.check_click()
        self.Categgory_button.check_click()
        self.Mylist_button.check_click()
        self.Back.check_click()
        self.Next_page.check_click()
        if self.Home_button.pressed == True:
            print('Home_button click')
            self.exit_state()
            self.Home_button.pressed = False
            
        elif self.Categgory_button.pressed == True:
            print('Categgory_button click')
            
        elif self.Mylist_button.pressed == True:
            print('Mylist_button click')
            
        elif self.Next_page.pressed == True:
            print('Next_page click')
            self.Next_page.pressed = False
            new_state = Game_rule_2(self.game)
            new_state.enter_state()
        
            
        elif self.Back.pressed == True:
            self.exit_state()
            self.Back.pressed = False
            
        
    def render(self, display):
        display.fill((0, 0, 0))
        # draw_button(self, surface, text, Text_size, Text_color, button_color, width_height, pos)
        # Button1 = self.Button(display, "HOME", 20, (255, 255, 255), (255, 0, 0), (85, 33), (749, 49))
        
        # self.Home_button = self.game.draw_button(display, "HOME", 20, (255, 255, 255), (255, 0, 0), (85, 33), (749, 49))
        # self.Categgory_button = self.game.draw_button(display, "CATEGORY", 20, (255, 255, 255), (0, 255, 0), (154, 33), (854, 49))
        # self.Mylist_button = self.game.draw_button(display, "MY LIST", 20, (255, 255, 255), (0, 0, 255), (123, 33), (1018, 49))
        
        
        self.Home_button.draw(display)
        self.Categgory_button.draw(display)
        self.Mylist_button.draw(display)
        self.Back.draw(display)
        self.Bg.draw_image(display, 'BG.png')
        
        
        self.game.draw_text(display, 'Avalon Rule', 64, (255, 255, 255), (631, 212))
        self.game.draw_text(display, 'Roles', 28, (255, 255, 255), (445, 300))
        
        
        self.Good.draw_image(display, 'Good.png')
        self.game.draw_text(display, 'Good team', 20, (255, 255, 255), (819, 362))
        self.game.draw_text(display, ' - Merlin - knows the identity of all Evil players', 16, (255, 255, 255), (828, 406))
        self.game.draw_text(display, ' - Loyal Servants of Arthur - do not know who is who', 16, (255, 255, 255), (828, 436))
        self.game.draw_text(display, ' - Percival - knows who Merlin is', 16, (255, 255, 255), (828, 466))

        
        self.Bad.draw_image(display, 'Bad.png')
        self.game.draw_text(display, 'Evil team', 20, (255, 255, 255), (819, 565))
        self.game.draw_text(display, ' - Assassin - knows who Merlin is', 16, (255, 255, 255), (828, 609))
        self.game.draw_text(display, ' - Mordred - unknown to Merlin', 16, (255, 255, 255), (828, 639))
        self.game.draw_text(display, ' - Morgana - appears as Merlin to Percival', 16, (255, 255, 255), (828, 669))
        self.game.draw_text(display, ' - The Minions of Mordred - do not know who is who', 16, (255, 255, 255), (828, 699))
        
        
        self.Next_page.draw_with_border(display, 1, (255, 255, 255))
        
class Button:
    def __init__(self, text, Text_size, Text_color, button_color, width_height, pos ):
        gui_font = pygame.font.Font(os.path.join("assets", "font", "Lexend-VariableFont_wght.ttf"), Text_size)
        self.pos = pos
        # self.surface = surface
        
        # Core attributes
        self.pressed = False
        
        # Top rectangle
        self.width_height = width_height
        self.top_rect = pygame.Rect(pos, width_height)
        self.top_color = button_color
        
        # text
        self.text_surf = gui_font.render(text, True, Text_color)
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)
        
    def draw(self, surface):
        pygame.draw.rect(surface, self.top_color, self.top_rect)
        # text_rect.center = (pos[0] + width_height[0]/2, pos[1] + width_height[1]/2)
        surface.blit(self.text_surf, self.text_rect)
        # self.check_click()
        
    def draw_image(self, surface, image):
        image = pygame.image.load(os.path.join("assets", "Game_rule", image))
        image = pygame.transform.scale(image, self.width_height)
        # pygame.draw.rect(surface, self.top_color, self.top_rect)
        # text_rect.center = (pos[0] + width_height[0]/2, pos[1] + width_height[1]/2)
        surface.blit(image, self.pos)
        # self.check_click()
        
    def draw_with_border(self, surface, border, border_color):
        surf = pygame.Surface((self.width_height[0]+border*2, self.width_height[1]+border*2), pygame.SRCALPHA)
        pygame.draw.rect(surf, self.top_color, (border, border, self.width_height[0], self.width_height[1]), 0)
        # pygame.draw.rect(surf, self.top_color, self.top_rect, 0)
        for i in range(1, border):
            pygame.draw.rect(surf, border_color, (border-i, border-i, self.width_height[0], self.width_height[1]), 1)
        surface.blit(surf, self.top_rect)
        surface.blit(self.text_surf, self.text_rect)
        
        
    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()        
        if self.top_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.pressed = True

            else:
                if self.pressed == True:
                    print('click')
                    self.pressed = False