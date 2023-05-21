import os, time, pygame
from states.state import State, Button, Dectect
from states.denied_page import Denied
from states.approved_page import Approved

class Vote_team(State):
    def __init__(self, game):
        State.__init__(self, game)
        
        self.Dectect = Dectect(Dectect)
        self.ori_time = 5 # 10
        self.time = 5 # 10
        self.start_count = True
        self.circle = 270
        self.num_team = (self.game.quest_track, self.game.num_player)
        self.dic_track_round = {1 : (46, 820), 2 : (135, 820), 3 : (224, 820), 4 : (313, 820), 5 : (402, 820)}
        
        self.Dectect = Dectect(Dectect)
        self.Bg = Button("", "Lexend-VariableFont_wght.ttf", 20, (255, 255, 255), (255, 255, 255), (1600, 900), (0, 0))
        self.Table = Button("", "Lexend-VariableFont_wght.ttf", 20, (255, 255, 255), (255, 255, 255), (748, 561), (426, 170))
        self.Text_time = Button("Team approval!", "Amita-Regular.ttf", 64, (238, 215, 10), (255, 255, 255), (450, 124), (575, 290))
        self.Describe = Button("raise a hand to approve the team", "Amita-Regular.ttf", 36, (255, 255, 255), (255, 255, 255), (541, 70), (530, 424))
        self.Phase = Button("Team Building Phase", "Amita-Regular.ttf", 36, (255, 255, 255), (255, 255, 255), (341, 70), (79, 26))

        
        self.Player_leader = Button(f"Leader : player {self.game.team_leader}", "Amita-Regular.ttf", 40, (255, 255, 255), (255, 255, 255), (291, 78), (673, 792))
        self.Track_round = Button("", "Amita-Regular.ttf", 40, (255, 255, 255), (255, 255, 255), (63, 63), self.dic_track_round[self.game.vote_track])
        
        self.arc = Button("", "Amita-Regular.ttf", 64, (255, 255, 255), (0, 0, 0), (112, 112), (744, 555))
        self.Text_time1 = Button(f"{self.time}", "Amita-Regular.ttf", 48, (255, 255, 255), (0, 0, 0), (49, 93), (800, 611))
        
        self.Quest_result1 = Button("", "Amita-Regular.ttf", 40, (255, 255, 255), (255, 255, 255), (63, 63), (1131, 819))
        self.Quest_result2 = Button("", "Amita-Regular.ttf", 40, (255, 255, 255), (255, 255, 255), (63, 63), (1221, 819))
        self.Quest_result3 = Button("", "Amita-Regular.ttf", 40, (255, 255, 255), (255, 255, 255), (63, 63), (1310, 819))
        self.Quest_result4 = Button("", "Amita-Regular.ttf", 40, (255, 255, 255), (255, 255, 255), (63, 63), (1399, 819))
        self.Quest_result5 = Button("", "Amita-Regular.ttf", 40, (255, 255, 255), (255, 255, 255), (63, 63), (1487, 819))
        
    def update(self, delta_time, action):
        self.game.reset_keys()
        self.Track_round = Button("", "Amita-Regular.ttf", 40, (255, 255, 255), (255, 255, 255), (63, 63), self.dic_track_round[self.game.vote_track])
            
        if self.time > 0 and self.start_count == True:
            if (self.time) % 3 == 1:
                self.Text_time = Button("Team approval ...", "Amita-Regular.ttf", 64, (238, 215, 10), (255, 255, 255), (450, 124), (575, 290))
                
            elif (self.time) % 3 == 2:
                self.Text_time = Button("Team approval ..", "Amita-Regular.ttf", 64, (238, 215, 10), (255, 255, 255), (450, 124), (575, 290))
                
            elif (self.time) % 3 == 0:
                self.Text_time = Button("Team approval .", "Amita-Regular.ttf", 64, (238, 215, 10), (255, 255, 255), (450, 124), (575, 290))
                
            self.time -= 1
            self.circle = self.circle - (360/self.ori_time)
            self.Text_time1 = Button(f"{self.time}", "Amita-Regular.ttf", 48, (255, 255, 255), (0, 0, 0), (49, 93), (800, 611))
            time.sleep(1)
            
        elif self.time == 0 and self.start_count == True:
            self.start_count = False
            self.circle = 270
            self.time = self.ori_time
            self.Text_time1 = Button(f"0", "Amita-Regular.ttf", 48, (255, 255, 255), (0, 0, 0), (49, 93), (800, 611))
            
            
        elif self.start_count == False:
            self.Text_time1 = Button(f"{self.time}", "Amita-Regular.ttf", 48, (255, 255, 255), (0, 0, 0), (49, 93), (800, 611))
            self.start_count = True
            hand_count = self.Dectect.count_hand()
            # print(hand_count)
            if hand_count >= self.game.num_player/2:
                print("Approved!")
                new_state = Approved(self.game)
                new_state.enter_state()
                
            else:
                print("Denied!")
                new_state = Denied(self.game)
                new_state.enter_state()
            
        
    def render(self, display):
        display.fill((0, 0, 0))
        self.Bg.draw_image(display, 'Gameplay_background.png')
        self.Table.draw_image(display, 'Table.png')
        
        self.Player_leader.draw_text(display)
        self.Describe.draw_text(display)
        self.Phase.draw_text(display)
        
        self.Text_time.draw_text(display)
        self.Text_time1.draw_text_center(display)
        self.arc.draw_arc(display, -90, self.circle, 50, 4)
        
        self.Track_round.draw_image(display, "Track_round.png")
        for i in range(1, 5, 1):
            if self.game.dic_result[i] != None:
                if i == 1:
                    if self.game.dic_result[1] == "success":
                         self.Quest_result1.draw_image(display, "Quest_successed.png")
                         
                    elif self.game.dic_result[1] == "fail":
                        self.Quest_result1.draw_image(display, "Quest_failed.png")
                        
                elif i == 2:
                    if self.game.dic_result[2] == "success":
                         self.Quest_result2.draw_image(display, "Quest_successed.png")
                         
                    elif self.game.dic_result[2] == "fail":
                        self.Quest_result2.draw_image(display, "Quest_failed.png")
                        
                elif i == 3:
                    if self.game.dic_result[3] == "success":
                         self.Quest_result3.draw_image(display, "Quest_successed.png")
                         
                    elif self.game.dic_result[3] == "fail":
                        self.Quest_result3.draw_image(display, "Quest_failed.png")
                        
                elif i == 4:
                    if self.game.dic_result[4] == "success":
                         self.Quest_result4.draw_image(display, "Quest_successed.png")
                         
                    elif self.game.dic_result[4] == "fail":
                        self.Quest_result4.draw_image(display, "Quest_failed.png")
                        
                elif i == 5:
                    if self.game.dic_result[5] == "success":
                         self.Quest_result5.draw_image(display, "Quest_successed.png")
                         
                    elif self.game.dic_result[5] == "fail":
                        self.Quest_result5.draw_image(display, "Quest_failed.png")
        
        