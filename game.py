import pygame
from gameObject import GameObject


class Game:
    #add self. if you want the variables in many different location in other function, and still belong to the Game class
    def __init__(self):
        self.width = 800
        self.height = 800   
        self.white_colour =(255,255,255)
        self.game_window=pygame.display.set_mode((self.width,self.height))
        #rgb: 0-255 color (red blue green)
        self.clock=pygame.time.Clock()
        #Gane loop wo keep the window open. 
        # tasks: handling input, updating game state, and rendering graphics (the 4th task is checking for endgame conditions
       
        self.background =GameObject(0,0,self.width, self.height,'assets/background.png')
        
        self.item = GameObject(375,50,50,50, 'assets/treasure.png')
        
  
    def draw_objects(self):
        self.game_window.fill(self.white_colour)
            
        self.game_window.blit (self.background.image, (self.background.x, self.background.y))
        self.game_window.blit (self.item.image, (self.item.x, self.item.y))
   
        pygame.display.update()
        
  
  
        
    def run_game_loop(self):
        while True:
            #Handle events
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    return
            #Execute logic
            #Update display
            self.draw_objects()
            #clockrate will update how many time per second (handle events,update screen) 
            self.clock.tick(60)