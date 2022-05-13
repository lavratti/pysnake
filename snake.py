from random import randint
import pygame
from pygame.locals import *
from time import sleep

board_l = 20
res = 600

class Snake:
    def __init__(self):
        self.segments = [[], [], [], [], [], ]
        self.segments[0] = [board_l/2 + 2, board_l/2]
        self.segments[1] = [board_l/2 + 1, board_l/2]
        self.segments[2] = [board_l/2, board_l/2]
        self.segments[3] = [board_l/2 - 1, board_l/2]
        self.segments[4] = [board_l/2 - 2, board_l/2]
        self.should_grow = False

    @property
    def head(self):
        return self.segments[0]

    def grow(self):
        self.should_grow = True

    def move_right(self):
        if self.should_grow:
            self.should_grow = False
            self.segments.append(self.segments[-1])
            for i in range(2, len(self.segments)):
                self.segments[len(self.segments)-i] = self.segments[len(self.segments)-i-1]
        else:
            for i in range(1, len(self.segments)):
                self.segments[len(self.segments)-i] = self.segments[len(self.segments)-i-1]
        self.segments[0] = [self.segments[0][0] + 1, self.segments[0][1]]
        
    def move_left(self):
        if self.should_grow:
            self.should_grow = False
            self.segments.append(self.segments[-1])
            for i in range(2, len(self.segments)):
                self.segments[len(self.segments)-i] = self.segments[len(self.segments)-i-1]
        else:
            for i in range(1, len(self.segments)):
                self.segments[len(self.segments)-i] = self.segments[len(self.segments)-i-1]
        self.segments[0] = [self.segments[0][0] - 1, self.segments[0][1]]
        
    def move_up(self):
        if self.should_grow:
            self.should_grow = False
            self.segments.append(self.segments[-1])
            for i in range(2, len(self.segments)):
                self.segments[len(self.segments)-i] = self.segments[len(self.segments)-i-1]
        else:
            for i in range(1, len(self.segments)):
                self.segments[len(self.segments)-i] = self.segments[len(self.segments)-i-1]
        self.segments[0] = [self.segments[0][0], self.segments[0][1] + 1]
        

    def move_down(self):
        if self.should_grow:
            self.should_grow = False
            self.segments.append(self.segments[-1])
            for i in range(2, len(self.segments)):
                self.segments[len(self.segments)-i] = self.segments[len(self.segments)-i-1]
        else:
            for i in range(1, len(self.segments)):
                self.segments[len(self.segments)-i] = self.segments[len(self.segments)-i-1]
        self.segments[0] = [self.segments[0][0], self.segments[0][1] - 1]
        
    def shoud_be_dead(self):
        if (self.segments[0][0] == 0 or 
            self.segments[0][0] == board_l or 
            self.segments[0][1] == 0 or 
            self.segments[0][1] == board_l):
                return True

        for segment in self.segments[1:]:
            if self.segments[0] == segment:
                return True
        return False


pygame.init()
screen = pygame.display.set_mode( (res, res) )
scaling = res/board_l
pygame.display.set_caption('Python Snake')
screen.fill((0, 0, 0))

snake = Snake()
apple_coord = [randint(1, board_l-1), randint(1, board_l-1)]
highscore = 0
done = False
next_move = snake.move_right

while not done:
                
    sleep(0.1)

    pygame.event.pump()
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        done = True
    elif keys[K_UP] or keys[K_w]:
        next_move = snake.move_up
    elif keys[K_LEFT] or keys[K_a]:
        next_move = snake.move_left
    elif keys[K_DOWN] or keys[K_s]:
        next_move = snake.move_down
    elif keys[K_RIGHT] or keys[K_d]:
        next_move = snake.move_right

    next_move()
    
    if snake.head == apple_coord:
        snake.grow()
        apple_coord = [randint(1, board_l-1), randint(1, board_l-1)]


    if snake.shoud_be_dead():
        highscore = max(highscore, len(snake.segments))
        print(highscore)
        snake = Snake()

    screen.fill((0, 0, 0))
    for segment in snake.segments:
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect((segment[0]-0.5) * scaling, res - ((segment[1]-0.5) * scaling), 1*scaling, 1*scaling))
    
    pygame.draw.circle(screen, (255, 0, 0), [(apple_coord[0]-0.5) * scaling, res - (apple_coord[1]-0.5) * scaling], 0.5 * scaling)

    pygame.display.update()

