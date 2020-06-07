# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import actions
    s = actions.SOUTH
    w = actions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    
      
    # print("Start:", problem.getStartState())
    # print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    # print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    #print(problem())
    
    
    agent_path = []
    explored_states = []                               

    start_state = (problem.getStartState(),[],0)
    stack = util.Stack()                        
    stack.push(start_state)
    
    while stack.isEmpty() is False:

        (state, action, cost) = stack.pop()       

        if problem.isGoalState(state):      
            agent_path = action
            break

        if state not in explored_states:
            explored_states.append(state)   
            
            for successor in problem.getSuccessors(state):
                next_action = action + [successor[1]]
                new_cost = cost + successor[2]
                new_state = (successor[0],next_action,new_cost)        
                stack.push(new_state)                                
    
    return agent_path
    # util.raiseNotDefined()
         
def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    agent_path = []
    explored_states = []

    start_state = (problem.getStartState(),[],0)
    queue = util.Queue()                        
    queue.push(start_state)

    while queue.isEmpty() is False:
        (state, action, cost) = queue.pop()

        if problem.isGoalState(state):
            agent_path = action
            break

        if state not in explored_states:
            explored_states.append(state)

            for successor in problem.getSuccessors(state):
                next_action = action + [successor[1]]
                new_cost = cost + successor[2]
                new_state = (successor[0], next_action, new_cost)
                queue.push(new_state)

    return agent_path
    # util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    agent_path = []
    explored_states = []

    start_state =  (problem.getStartState(),[],0)
    priority_queue = util.PriorityQueue()
    total_cost = 0
    priority_queue.push(start_state, total_cost)

    while priority_queue.isEmpty() is False:

        (state, action, cost) = priority_queue.pop()

        if problem.isGoalState(state):
            agent_path = action
            break

        if state not in explored_states:
            explored_states.append(state)

            for successor in problem.getSuccessors(state):

                next_action = action + [successor[1]]
                new_cost = cost + successor[2]
                total_cost = cost + successor[2]
                new_state = (successor[0], next_action, new_cost)
                priority_queue.update(new_state, total_cost)

    return agent_path
    # util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    
    agent_path = []
    explored_states = []

    priority_queue = util.PriorityQueue()
    start_state =  (problem.getStartState(),[],0)
    combined_cost = 0
    priority_queue.update(start_state, combined_cost)

    while priority_queue.isEmpty() is False:

        (state, action, cost) = priority_queue.pop()

        if problem.isGoalState(state):
            agent_path = action
            break

        if state not in explored_states:
            explored_states.append(state)

            for successor in problem.getSuccessors(state):

                next_action = action + [successor[1]]
                new_cost = cost + successor[2]
                combined_cost = new_cost + heuristic(successor[0], problem)
                new_state = (successor[0], next_action, new_cost)
                priority_queue.update(new_state,combined_cost)

    # print(agent_path)
    return agent_path
    # util.raiseNotDefined()

def bidirectionalSearch(problem, heuristic):
    
    # agent_path = []

    # list to see explored states
    explored_states = []

    # nodes visited in the forward direction
    fwd_vis = []
    # nodes visited in the backward direction
    bwd_vis =[]

    forward = util.PriorityQueue()
    backward = util.PriorityQueue()

    # state, actions and cost for the start state
    start_state = (problem.getStartState(), [], 0)
    
    # state, actions and cost for the goal state
    goal_state = (problem.goal, [], 0)

    combined_cost = 0

    # updating the forward and backward queues
    forward.update(start_state, combined_cost)
    backward.update(goal_state,combined_cost)

    # defining a list for the backward action from the goal node to the node where the paths meet
    rev_action = []

    # dictionary holding the reversed directions
    rev_dir = dict()
    rev_dir["North"] = "South"
    rev_dir["South"] = "North"
    rev_dir["West"] = "East"
    rev_dir["East"] = "West"

    while True:
        if forward.isEmpty():
            return []

        (state, action, cost) = forward.pop()

        if problem.isGoalState(state) or state in bwd_vis:
                while not backward.isEmpty():
                    (s,a,c) = backward.pop()
                    if s == state:
                        solution = action + a.reverse()
                        return solution

        if state not in explored_states:
            explored_states.append(state)

            for successor in problem.getSuccessors(state):
                next_action = action + [successor[1]]
                new_cost = cost + successor[2]
                combined_cost = new_cost + heuristic(successor[0], problem)
                new_state = (successor[0], next_action, new_cost)
                forward.update(new_state, combined_cost)
                fwd_vis.append(successor[0])

        if backward.isEmpty():
            return []

        (state, action, cost) = backward.pop()

        if state in fwd_vis:
            while not forward.isEmpty():
                (s,a,c) = forward.pop()
                if s == state:
                    
                    action.reverse()
                    
                    for i in action:
                        for key,value in rev_dir.items():
                            if i == key:
                                rev_action.append(value)

                    # solution = a + directions(action)
                    # print(len(explored_states))
                    # print(len(fwd_vis))
                    # print(len(bwd_vis))
                    # print(len(forward))
                    # print(len(backward))
                    solution = a + rev_action

                    # print(solution)

                    return solution

        if state not in explored_states:
            explored_states.append(state)

            for successor in problem.getSuccessors(state):
                next_action = action + [successor[1]]
                new_cost = cost + successor[2]
                combined_cost = new_cost + heuristic(successor[0], problem)
                new_state = (successor[0], next_action, new_cost)
                backward.update(new_state, combined_cost)
                bwd_vis.append(successor[0])
    
    return []

# def directions(action):
#     rev_action = []
#     rev_dir = dict()
#     rev_dir["North"] = "South"
#     rev_dir["South"] = "North"
#     rev_dir["West"] = "East"
#     rev_dir["East"] = "West"

#     for a in action:
#         for key,values in rev_dir.items():
#             if key == a:
#                 rev_action.append(values)

#     #print (rev_action)
#     return rev_action


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
bmm = bidirectionalSearch