# Informed and Uninformed Search

Prerequisites : Python 2.7
----------------------------------

Important Files
----------------------------------
- search.py        - This file contains all the algorithms for the search problems.
- searchAgents.py  - This file contains the problems and the respective heuristic Functions.
- pacman.py        - Main file that initiates the Pacman game.
- game.py          - The logic that runs the Pacman game.
- layouts          - This folder contains the various different layouts for the mazes. The existing ones can be edited or new mazes can be created here.
- layout.py        - The file that processes the manually designed layouts.
- utils.py         - The utilities file that contains useful data structures to implement this project. 
- ghostAgents.py   - This code helps us to control the ghost agents.

Implementation
----------------------------------
`python pacman.py -l [Maze] -p SearchAgent -a fn=[search_algorithm],heuristic=[heuristic_used]`
`python pacman.py -l [Maze] -p SearchAgent -a fn=[search_algorithm],prob=[problem]`

[problem] can be:
1. cornersProblem
2. PositionSearchProblem
3. FoodSearchProblem

[Maze] can be one of the following:

1.  tinyMaze
2.  smallMaze
3.  mediumMaze
4.  bigMaze
5.  openMaze
6.  contoursMaze ...

fn can be one of the following [search_algorithm]:

1. bfs     = Breadth First Search
2. dfs     = Depth First Search
3. astar   = A* Search
4. ucs     = Uniform Cost Search


[heuristics_used] can be one of the following; 

1. manhattanHeuristic - To use manhattan distance, which is the distance calculated along the axes at right angles   
2. euclideanHeuristic - To use euclidean distance, which is the distance between the two nodes in cartesian space.
3. mazeDistance       - To use maze distance, which is the distance between current state and goal state considering all the obstacles in the Pacman's path.
4. nullHeuristic      - This is the default when heuristic is not mentioned


Example Usage:
--------------------------------------------
- In Terminal / Command Prompt:

`cd [folder where you extracted the Pacman Game package]/search`

`python pacman.py -l bigMaze -p SearchAgent -a fn=bmm,heuristic=mazeDistance`

`python pacman.py -l openMaze -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic`

`python pacman.py -l trialMaze3 -p SearchAgent -a fn=bfs`
