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

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

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
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        curFoodList = currentGameState.getFood().asList()
        newFoodList = newFood.asList()
        
        dist_list = []
        for food in newFoodList:
            dist_list.append(manhattanDistance(newPos, food))
        if len(dist_list) == 0:
            min_dist = 0
        else:
            min_dist = min(dist_list)
        
        ghost_list = []
        for ghost in newGhostStates:
            ghost_list.append(manhattanDistance(newPos, ghost.getPosition()))
            
        if len(ghost_list) == 0:
            min_ghost = 0
        else:
            min_ghost = min(ghost_list)
            
        score = - min_dist
        if newPos in curFoodList:
            score += min_dist
        
        scaredGhost = False 
        for scaredTime in newScaredTimes:
            if scaredTime != 0:
                scaredGhost = True
        if scaredGhost is False:
            if min_ghost < 2:
                score = - 999999
                
        return score        
        

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
        def miniMax (gameState, player, depth):
            if player >= gameState.getNumAgents():
                player = 0
                depth += 1
            best_move = None
            # terminal condition:
            # when the gameState is win or lose or it reached maximum depth
            if gameState.isWin() or gameState.isLose() or depth == self.depth:
                return (self.evaluationFunction(gameState), best_move)
            if player == 0:
                value = float("-inf")
            else:
                value = float("inf")
            
            for move in gameState.getLegalActions(player):
                nxt_pos = gameState.generateSuccessor(player, move)
                nxt_val, nxt_move = miniMax(nxt_pos, player +1, depth)
                if player == 0 and value < nxt_val:
                    value, best_move = nxt_val, move
                elif player != 0 and value > nxt_val:
                    value, best_move = nxt_val, move                
            return (value, best_move)
        
        return miniMax (gameState, 0, 0)[1]

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        def alphaBeta(gameState, player, alpha, beta, depth):
            if player >= gameState.getNumAgents():
                player = 0
                depth += 1           
            best_move = None
            if gameState.isWin() or gameState.isLose() or depth == self.depth:
                return (self.evaluationFunction(gameState), best_move)
            if player == 0:
                value = float("-inf")
            else:
                value = float("inf")
            
            for move in gameState.getLegalActions(player):
                nxt_pos = gameState.generateSuccessor(player, move)
                nxt_val, nxt_move = alphaBeta(nxt_pos, player + 1, alpha, beta, depth)
                if player == 0:
                    if value < nxt_val:
                        value, best_move = nxt_val, move
                    if value >= beta:
                        return (value, best_move)
                    alpha = max(alpha, value)
                elif player != 0:
                    if value > nxt_val:
                        value, best_move = nxt_val, move   
                    if value <= alpha:
                        return (value, best_move)
                    beta = min(beta, value)
            return (value, best_move)            
            
        return alphaBeta(gameState, 0, float("-inf"), float("inf"), 0)[1]

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
        def expectiMax(gameState, player, depth):
            if player >= gameState.getNumAgents():
                player = 0
                depth += 1
            best_move = None
            if gameState.isWin() or gameState.isLose() or depth == self.depth:
                return (self.evaluationFunction(gameState), best_move)
            if player == 0:
                value = float("-inf")
            else:
                value = 0
            for move in gameState.getLegalActions(player):
                nxt_pos = gameState.generateSuccessor(player, move)
                nxt_val, nxt_move = expectiMax(nxt_pos, player + 1, depth)
                if player == 0 and value < nxt_val:
                    value, best_move = nxt_val, move
                elif player != 0:
                    value = value + 1.0 /len(gameState.getLegalActions(player)) * nxt_val       
            return (value, best_move)
            
        return expectiMax(gameState, 0, 0)[1]

def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <I have made the pacman to go for food.>
    """
    "*** YOUR CODE HERE ***"

    pos = currentGameState.getPacmanPosition()
    foodList = currentGameState.getFood().asList()
    ghostStates = currentGameState.getGhostStates()
    capList = currentGameState.getCapsules()
    
    dist_list = []
    for food in foodList:
        dist_list.append(manhattanDistance(pos, food))
    if len(dist_list) == 0:
        min_dist = 0
    else:
        min_dist = min(dist_list)    
    
    ghost_list = []
    for ghost in ghostStates:
        ghost_list.append(manhattanDistance(pos, ghost.getPosition()))
        
    if len(ghost_list) == 0:
        min_ghost = 0
    else:
        min_ghost = min(ghost_list) 
    
    cap_list = []
    for cap in capList:
        cap_list.append(manhattanDistance(pos, cap))
        
    if len(cap_list) == 0:
        min_cap = 0
    else:
        min_cap = min(cap_list)     
    
    # I made the pacman to go for food. But I gave less score for closest food
    #because g
    score = currentGameState.getScore()
    score += min_ghost
    score -= (min_dist*2 + 5*len(cap_list) + 10* len(foodList))
    return score

# Abbreviation
better = betterEvaluationFunction

