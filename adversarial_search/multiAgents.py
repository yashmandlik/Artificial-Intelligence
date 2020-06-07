# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()
        #print (legalMoves)

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        #print (scores)
        bestScore = max(scores)
        #print (bestScore)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"
        #print (legalMoves[chosenIndex])
        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        #print(successorGameState)
        newPos = successorGameState.getPacmanPosition()
        #print(newPos)
        newFood = successorGameState.getFood()
        #print (newFood.asList())
        newGhostStates = successorGameState.getGhostStates()
        #print(newGhostStates)
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
        #print(newScaredTimes)

        "*** YOUR CODE HERE ***"
        
        food_distance = []
        for food in newFood.asList():
          dist = manhattanDistance(newPos, food)
          food_distance.append(dist)
               
        if len(food_distance) > 0:
          min_food_distance = float(min(food_distance))
          food_score = 1/min_food_distance
        else:
          food_score = 1

        ghost_positions = successorGameState.getGhostPositions()
        ghost_distance = []
        ghost_score = 0

        for position in ghost_positions:
          dist = manhattanDistance(newPos, position)
          ghost_distance.append(dist)

        min_ghost_distance = min(ghost_distance)
        if min_ghost_distance < 2:
          ghost_score = 1

        #print (min_food_distance, food_score, min_ghost_distance)

        return successorGameState.getScore() + food_score - ghost_score

def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """
        "*** YOUR CODE HERE ***"
        
        def minimax(gameState, agentIndex, depth):
          
          if depth == 0 or gameState.isWin() or gameState.isLose():
            return (self.evaluationFunction(gameState), "")

          if agentIndex == 0:

            v = float("-inf")
            best_action = ""
            actions = gameState.getLegalActions(agentIndex)
            
            for a in actions:
              new_state = gameState.generateSuccessor(agentIndex, a)
              temp_val = minimax(new_state, agentIndex+1, depth)
              if temp_val[0] > v:
                v = temp_val[0]
                best_action = a

            return (v, best_action)

          else:
            v = float("inf")
            best_action = ""
            actions = gameState.getLegalActions(agentIndex)

            for a in actions:
              new_state = gameState.generateSuccessor(agentIndex, a)
              if (agentIndex+1)%gameState.getNumAgents() == 0:
                d = depth-1
              else:
                d = depth
              temp_val = minimax(new_state, (agentIndex+1)%gameState.getNumAgents(), d)

              if temp_val[0] < v:
                v = temp_val[0]
                best_action = a
            
            return (v, best_action)

        return minimax(gameState, agentIndex=0, depth=self.depth)[1]   

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        def alpha_beta(gameState, agentIndex, depth, alpha, beta):
          
          if depth == 0 or gameState.isWin() or gameState.isLose():
            return (self.evaluationFunction(gameState), "")

          if agentIndex == 0:

            v = float("-inf")
            best_action = ""
            actions = gameState.getLegalActions(agentIndex)
            
            for a in actions:
              new_state = gameState.generateSuccessor(agentIndex, a)
              temp_val = alpha_beta(new_state, agentIndex+1, depth, alpha, beta)
              
              if temp_val[0] > v:
                v = temp_val[0]
                best_action = a
                
              if temp_val[0] > beta:
                return (temp_val[0],a)
              
              if v>alpha:
                alpha = v
              
            return (v, best_action)

          else:
            v = float("inf")
            best_action = ""
            actions = gameState.getLegalActions(agentIndex)

            for a in actions:
              new_state = gameState.generateSuccessor(agentIndex, a)
              if (agentIndex+1)%gameState.getNumAgents() == 0:
                d = depth-1
              else:
                d = depth
              temp_val = alpha_beta(new_state, (agentIndex+1)%gameState.getNumAgents(), d, alpha, beta)

              if temp_val[0] < v:
                v = temp_val[0]
                best_action = a
            
              if temp_val[0] < alpha:
                return(temp_val[0], a)

              if v<beta:
                beta = v
            return (v, best_action)

        return alpha_beta(gameState, agentIndex=0, depth=self.depth, alpha = float("-inf"), beta = float("inf"))[1]

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        def expectimax(gameState, agentIndex, depth):
          
          if depth == 0 or gameState.isWin() or gameState.isLose():
            return (self.evaluationFunction(gameState), "")

          if agentIndex == 0:

            v = float("-inf")
            best_action = ""
            actions = gameState.getLegalActions(agentIndex)
            
            for a in actions:
              new_state = gameState.generateSuccessor(agentIndex, a)
              temp_val = expectimax(new_state, agentIndex+1, depth)
              if temp_val[0] > v:
                v = temp_val[0]
                best_action = a

            return (v, best_action)

          else:
            v = 0
            
            best_action = ""
            actions = gameState.getLegalActions(agentIndex)
            p = 1.0/len(actions)
            
            for a in actions:
              new_state = gameState.generateSuccessor(agentIndex, a)
              if (agentIndex+1)%gameState.getNumAgents() == 0:
                d = depth-1
              else:
                d = depth
              temp_val = expectimax(new_state, (agentIndex+1)%gameState.getNumAgents(), d)
              v = v + p*temp_val[0]
            
            return (v, best_action)

        return expectimax(gameState, agentIndex=0, depth=self.depth)[1]  


def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
      Similar to the first question, I used the manhattan distance to the foods pellets
      and the ghosts. The nearer the food pellet, the higher the score, which is the inverse of the
      food distance and the opposite for the ghosts. I also used the scared timer in this case to check if 
      the ghosts where scared or not. I also wrote the case for when the length of the scared time is not zero but
      it made no difference to the overall score so I omitted it.
    """
    "*** YOUR CODE HERE ***"
    pacman_position = currentGameState.getPacmanPosition()
    food_position = currentGameState.getFood()
    
    food_distance = []
    for food in food_position.asList():
      dist = manhattanDistance(pacman_position, food)
      food_distance.append(dist)
            
    if len(food_distance) > 0:
      min_food_distance = float(min(food_distance))
      food_score = 1/min_food_distance
    else:
      food_score = 1

    ghost_positions = currentGameState.getGhostPositions()
    ghost_state = currentGameState.getGhostStates()
    ghost_distance = []
    ghost_score = 0
    scared_time = []
    for s in ghost_state:
      scared_time.append(s) 

    if len(scared_time) == 0: 
      for position in ghost_positions:
        dist = manhattanDistance(pacman_position, position)
        ghost_distance.append(dist)

      min_ghost_distance = min(ghost_distance)
      if min_ghost_distance < 2:
        ghost_score = 1

    return currentGameState.getScore() + food_score - ghost_score
    
    
# Abbreviation
better = betterEvaluationFunction