from display import Display
from synthetic_data import SyntheticData
from algorithm import *

import pygame
import random

def main():
    num_people = 300
    num_ads = 9
    num_billboards = 9
    matrix_size = 40
    categories = ['technology', 'fashion', 'food']
    colors = {'technology': (155, 0, 0),\
                'fashion': (0, 155, 0),\
                'food': (0, 0, 155)
                }
    # (num_people, num_ads, num_billboards, matrix_size)
    data = SyntheticData(num_people, num_ads, num_billboards, matrix_size, categories, colors)
    display = Display(20, matrix_size)

    data.draw_people(display)
    data.draw_billboards(display)

    # display.draw_big_circle(10, 10, 5, (0, 0, 0))
    # display.draw_big_circle(10, 30, 5, (0, 0, 0))
    # display.draw_big_circle(30, 10, 5, (0, 0, 0))
    # display.draw_big_circle(30, 30, 5, (0, 0, 0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                display.end()
                break

        p_id = random.randint(0, data.num_people - 1)
        dire = random.choice([(1,0), (-1,0), (0,1), (0,-1)])

        display.draw_circle(data.people[p_id][1], data.people[p_id][2], (255, 255, 255))
        data.update_person(p_id, dire)
        display.draw_circle(data.people[p_id][1], data.people[p_id][2], data.colors[data.people[p_id][3]])
        
        # algorithm1(data.people, data.billboards, data.ads)
        algorithm2(data.people, data.billboards, data.ads)
        data.draw_billboards(display)

        # pygame.time.wait(2)
        display.display()

if __name__ == "__main__":
    main()