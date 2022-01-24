import pygame

#This class intends to hold game objects with same properties: x, y, width, height, and image. 
class GameObject:
    
    def __init__(self, x, y, width, height, image_path):
        image = pygame.image.load(image_path)
        #scale up image
        self.image=pygame.transform.scale(image, (width,height))
        
        self.x=x
        self.y=y
        self.width=width
        self.height=height