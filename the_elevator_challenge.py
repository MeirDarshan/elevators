import queue
import pygame
pygame.init()


# variables
window_width, window_heigh = 750, 650
elevator_width, elevator_heigh = 64, 64
floor_width, floor_heigh = 64, 128
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
GREY = (200, 200, 200)


size = (window_width, window_heigh)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("elevator")
screen.fill(WHITE)
pygame.display.flip()

IMG_BRICK = "d71f94_ae34abde0e1f460693df63e483c70091~mv2.png"
img_brick = pygame.image.load(IMG_BRICK)
screen.blit(img_brick, (70, 586))
pygame.display.flip()

IMG_ELEVATOR = "elv.png"
img_elevator = pygame.image.load(IMG_ELEVATOR)
screen.blit(img_elevator, (190, 586))
pygame.display.flip()







class Elevator:
    def __init__(self):
        self.__curent_floor = 0
        self.__still_available = 0
        
class Floor:
    def __init__(self, floor_num):   
       self.__floor_num = floor_num
        
    def control(self, floor_num): 
       self.__request.append(self.__floor_num)
      
class Building:
    def __init__(self, floors: int, elevators: int):
        self.__floors = []
        for i in range(floors):
            self.__floors.append(Floor(i))
        self.__elevators = []
        for i in range(elevators):
            self.__floors.append(Elevator(i)) 
        
    def constractot(self):
        for i in range(len(self.__floors)):
            y = window_heigh - i * floor_width
            screen.blit(img_brick, (70, y))







    # def control (self, floor_num):
    #     self.__request.append(floor_num)





 
finish = False
while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
pygame.quit()
       