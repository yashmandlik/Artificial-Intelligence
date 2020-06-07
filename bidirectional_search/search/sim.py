"""
Pikachu Simulator made by Gautam Sharma
@2020
"""



import pygame
from util import PriorityQueue
import heapq
import matplotlib.pyplot as plt
pygame.init()
import math
import time
import argparse

parser = argparse.ArgumentParser(description = 'Pikachu Simulator for CSE 571 Final Project.')
parser.add_argument('-a','--algorithm', type=str, metavar='',help = 'astar or bidirec')
parser.add_argument('-x','--xposition', type=int, metavar='',help = ' Starting x position of Pikachu')
parser.add_argument('-y','--yposition', type=int, metavar='',help = 'Starting y position of Pikachu')
parser.add_argument('-gx','--xgoalpos', type=int, metavar='',help = 'X Position of Pokeball')
parser.add_argument('-gy','--ygoalpos', type=int, metavar='',help = 'Y Position of Pokeball')
group = parser.add_mutually_exclusive_group()
group.add_argument('-q', '--quiet', action='store_true', help='print quiet')
group.add_argument('-v', '--verbose', action='store_true', help='print verbose')
args = parser.parse_args()

win = pygame.display.set_mode((500, 500))
char = pygame.image.load('Images/pikacu-2.png')
char = pygame.transform.scale(char, (80, 80))

ball = pygame.image.load('Images/balls.png')
ball = pygame.transform.scale(ball, (25, 25))

light = pygame.image.load('Images/light.png')
light = pygame.transform.scale(light, (100, 100))

pygame.display.set_caption("Search Simulator for CSE 571 Final Project")
clock = pygame.time.Clock()

class Pikachu():

    def __init__(self,x,y,goal_x,goal_y):
        self.x = x
        self.y = y
        self.goal_x = goal_x
        self.goal_y = goal_y
        self.lim_x = 500
        self.lim_y = 500
        self.width = 15
        self.height = 17
        self.vel = 25

    def heuristic(self,state):
        return math.sqrt(abs(state[0] - self.goal_x) + abs(state[1] - self.goal_y)) + (
            ((state[0] - self.x) ** 2 + (state[1] - self.y) ** 2))

    def heuristic_b(self,state):
        return math.sqrt(abs(state[0] - self.x) + abs(state[1] - self.y)) + (
        ((state[0] - self.goal_x) ** 2 + (state[1] - self.goal_y) ** 2))

    def astar(self,path, explored, fringe, bwd_path=None, fringe_bwd=None):

        while fringe:

            clock.tick(400)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            fringe.sort(reverse=True)

            state = fringe.pop()[1]
            plt.scatter(state[0], state[1])

            pygame.draw.rect(win, (255, 100, 100), (state[0], state[1], self.width, self.height))
            clock.tick(400)
            win.blit(char, (self.x, self.y))
            pygame.display.update()
            win.blit(ball, (self.goal_x, self.goal_y))
            pygame.display.update()

            if state == (self.goal_x, self.goal_y):
                for p in path[(state)]:
                    clock.tick(30)
                    pygame.draw.rect(win, (0, 255, 0), (p[0], p[1], self.width, self.height))
                    pygame.display.update()
                time.sleep(3)
                pygame.time.wait(1500)
                break
            if state not in explored:
                explored.append(state)

                for next_states in self.action(state):
                    if next_states not in explored:
                        prev = path[(state)]
                        path[(next_states)] = [next_states] + prev
                        fringe.append([self.heuristic(next_states), next_states])

    def action(self,state):
        a = []
        if state[0] > self.vel:
            a.append((state[0] - self.vel, state[1]))

        if state[0] < 1000 - self.width - self.vel:
            a.append((state[0] + self.vel, state[1]))

        if state[1] > self.vel:
            a.append((state[0], state[1] - self.vel))

        if state[1] < 1000 - self.height - self.vel:
            a.append((state[0], state[1] + self.vel))

        if state[0] > self.vel and state[1] > self.vel:
            a.append((state[0] - self.vel, state[1] - self.vel))

        if state[0] > self.vel and state[1] < 1000 - self.height - self.vel:
            a.append((state[0] - self.vel, state[1] + self.vel))

        if state[0] < 1000 - self.width - self.vel and state[1] < 1000 - self.height - self.vel:
            a.append((state[0] + self.vel, state[1] + self.vel))

        if state[0] < 1000 - self.width - self.vel and state[1] > self.vel:
            a.append((state[0] + self.vel, state[1] - self.vel))

        return a

    def bidirec(self,fwd_path, explored, fringe_fwd, bwd_path, fringe_bwd):
        fwd_vis = []
        bwd_vis = []
        while True:
            if not fringe_fwd:
                return []

            clock.tick(400)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            fringe_fwd.sort(reverse=True)

            state = fringe_fwd.pop()[1]
            plt.scatter(state[0], state[1])

            pygame.draw.rect(win, (255, 100, 100), (state[0], state[1], self.width, self.height))
            clock.tick(400)
            win.blit(char, (self.x, self.y))
            pygame.display.update()
            win.blit(ball, (self.goal_x, self.goal_y))
            pygame.display.update()

            if state == (self.goal_x, self.goal_y) or state in bwd_vis:
                while fringe_bwd:
                    fringe_bwd.sort(reverse=True)
                    s = fringe_bwd.pop()[1]
                    if s == state or state == (self.goal_x, self.goal_y):
                        for p in fwd_path[(state)]:
                            clock.tick(30)
                            pygame.draw.rect(win, (0, 255, 0), (p[0], p[1], self.width, self.height))
                            # pygame.display.update()
                        win.blit(light, (250, 250))
                        pygame.display.update()
                        break

            if state not in explored:
                explored.append(state)

                for next_states in self.action(state):
                    if next_states not in explored:
                        prev = fwd_path[(state)]
                        fwd_path[(next_states)] = [next_states] + prev
                        fringe_fwd.append([self.heuristic(next_states), next_states])
                        fwd_vis.append(next_states)

            if not fringe_bwd:
                return []

            clock.tick(400)

            fringe_bwd.sort(reverse=True)

            state = fringe_bwd.pop()[1]
            # plt.scatter(state[0], state[1])

            clock.tick(400)
            # win.blit(char, (x, y))
            pygame.draw.rect(win, (0, 100, 250), (state[0], state[1], self.width, self.height))
            pygame.display.update()
            # win.blit(ball, (goal_x, goal_y))
            if state in fwd_vis:
                while fringe_fwd:
                    fringe_fwd.sort(reverse=True)
                    s = fringe_fwd.pop()[1]
                    if s == state:
                        for p in bwd_path[(state)]:
                            clock.tick(30)
                            pygame.draw.rect(win, (0, 255, 0), (p[0], p[1], self.width, self.height))
                            # pygame.display.update()
                        win.blit(light, (250, 250))
                        pygame.display.update()
                        break

            if state not in explored:
                explored.append(state)

                for next_states in self.action(state):
                    if next_states not in explored:
                        prev = bwd_path[(state)]
                        bwd_path[(next_states)] = [next_states] + prev
                        fringe_bwd.append([self.heuristic_b(next_states), next_states])
                        bwd_vis.append(next_states)

    def implementation(self,search):

        fringe = []
        fringe_fwd = []
        fringe_bwd = []
        explored = []
        path = dict()
        fwd_path = dict()
        bwd_path = dict()

        path[(self.x, self.y)] = [(self.x, self.y)]
        fwd_path[(self.x, self.y)] = [(self.x, self.y)]
        bwd_path[(self.goal_x, self.goal_y)] = [(self.goal_x, self.goal_y)]

        fringe.append([0, (self.x, self.y)])
        fringe_fwd.append([0, (self.x, self.y)])
        fringe_bwd.append([0, (self.goal_x, self.goal_y)])

        """
        ###########################################################
        Change the search argument with different functions to test
        ##########################################################
        """
        search(fwd_path, explored, fringe_fwd, bwd_path, fringe_bwd)
        # pygame.time.delay(100)

        pygame.quit()


if __name__ == '__main__':
    program_starts = time.time()
    Pika = Pikachu(args.xposition,args.yposition,args.xgoalpos,args.ygoalpos)
    if args.algorithm == 'astar':
        Pika.implementation(search = Pika.astar)
    else:
        Pika.implementation(search = Pika.bidirec)
    now = time.time()
    print("It has been {0} seconds since the loop started".format(now - program_starts))
    plt.savefig("Hello.jpg")
