# BI-DIRECTIONAL SEARCH

Team Name: Agents

Team Members:
----------------------------------
- Gautam Sharma	
- Hoda Nasser	
- Yash Mandlik	
- Yashaswy Govada	

Topic Chosen: 
----------------------------------
Topic 1 - BI-DIRECTIONAL SEARCH

Prerequisites : Python 2.7
----------------------------------

PACMAN Bidirectional Search  
----------------------------------

Important Files
----------------------------------
- search.py        - This file contains all the algorithms for the search problems.
- searchAgents.py  - This file contains the problems and the respective Heuristic Functions.
- pacman.py        - Main file that initiates the Pacman game.
- game.py          - The logic that runs the Pacman game.
- layouts          - This folder contains the various different layouts for the mazes. The existing ones can be edited or new Mazes can be created here.
- layout.py        - The file that processes the manually designed layouts.
- utils.py         - The utilities file that contains useful Data Sructures to implement this project. 
- ghostAgents.py   - This code helps us to control the Ghost Agents.

Implementation
----------------------------------
`python pacman.py -l [Maze] -p SearchAgent -a fn=[search_algorithm],heuristic=[heuristic_used]`

[Maze] can be one of the following:

1.  tinyMaze
2.  smallMaze
3.  mediumMaze
4.  bigMaze
5.  openMaze
6.  contoursMaze
7.  trialMaze1
8.  trialMaze2
9.  trialMaze3
10. trialMaze4
11. trialMaze5
12. trialMaze6
13. trialMaze7
14. trialMaze8
15. trialMaze9

fn can be one of the following [search_algorithm]:

1. bfs     = Breadth First Search
2. dfs     = Depth First Search
3. astar   = A* Search
4. ucs     = Uniform Cost Search
5. bmm   = Bidirectional Search MM

[heuristics_used] can be one of the following; 

1. manhattanHeuristic - To use manhattan Distance, which is the distance calculated along the axes at right angles   
2. euclideanHeuristic - To use Euclidean Distance, which is the distance between the two nodes in cartesian space.
3. mazeDistance       - To use Maze Distance, which is the distance between current state and goal state considering all the obstacles in the Pacman's path.
4. nullHeuristic      - This is the default when heuristic is not mentioned


Example Usage:
--------------------------------------------
- In Terminal / Command Prompt:

`cd [folder where you extracted the Pacman Game package]/search`

`python pacman.py -l bigMaze -p SearchAgent -a fn=bmm,heuristic=mazeDistance`

`python pacman.py -l openMaze -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic`

`python pacman.py -l trialMaze3 -p SearchAgent -a fn=bfs`

Note: This command will show you the optimized path to the goal using the search algorithm and the heuristic specified by you given 
      the Maze. It also gives information regarding, Total Cost, Computation Time, Number of nodes expanded and the Score
      after Pacman emerges victorious. 

##########################################################################################

Testing A star vs Bidirectional Search-
---------------------------------------------
A custom simulator was built using pygame and programmed using python to simulate A star search vs Bidirectional Search.
We have named it as the Pikachu Simulator. Clone and extract Pikachu_Simulator.zip in a folder of your choice. 
To run it first install pygame:

- Note : It works with python 3.7

- In Terminal / Command Prompt:

`python3 -m pip install -U pygame --user`

`cd [folder where you extracted Pikachu simulator]/search`

`python sim.py -a [astar or bidirec] -x [staring x position] -y [starting y position] -gx [goal x position] -gy [goal y position]`

Note : Only put coordinates that are multiple of 25 and <=500.

Eg : 

`python sim.py -a astar -x 0 -y 0 -gx 100 -gy 100`

`python sim.py -a bidirec -x 0 -y 0 -gx 100 -gy 100`

The program execution time will be printed out to the terminal after the program terminates.
Observe the difference in time between A star and Bidirectional.
