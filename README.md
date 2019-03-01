# Introduction to Artificial Intelligence
### 토론토 대학교 CSC384 Introduction to Artificial Intelligence 수업에서 진행한 프로젝트들을 올렸습니다.
### Projects from University of Toronto CSC384 Introduction to Artificial Intelligence
1. *Search*
>UC Berkeley CSC188 프로젝트를 수정한 코드를 기반으로 진행하였습니다.
> 이 프로젝트에서 저는 다양한 검색 알고리즘을 적용하여 팩맨이 미로에서 길을 찾고 음식을 효율적인 방법으로 찾을 수 있게 하였습니다.
> 이 프로젝트를 통해 저는 다양한 검색 알고리즘을 실제 프로젝트에 적용해보는 경험을 하였습니다. DFS나 BFS, Uniform-cost Search는 비교적 적용하기 쉬웠지만, A* Search에서 얼마나 좋은 heuristic을 찾는냐가 중요하다는 것을 깨달았습니다.
> 제가 작성한 코드는 search.py와 searchAgents.py에 있습니다.
> 다음은 제가 팩맨에 적용시킨 검색 알고리즘들입니다.
- Depth-First Search
- Breadth-First Search
- Uniform-cost Search
- A* Search with different heuristics

2. *Multi-Agent Pacman*
>  UC Berkeley CSC188 프로젝트를 수정한 코드를 기반으로 진행하였습니다.
> 이 프로젝트에서 저는 유령을 포함한 클래식 버전의 팩맨을 구현하려고 다양한 게임 트리 검색 알고리즘을 적용하였습니다. 
> 제가 작성한 알고리즘들은 multiAgents.py안에 있습니다.
> 다음은 제가 작성한 게임 트리 검색 알고리즘들입니다.
- Minimax
- Alpha-Beta Pruning
- Expectimax
- Evaluation Function

3. *Constraint Satisfaction Problems*
>  이 프로젝트에서 저는 제약 만족 문제와 백트래킹 검색 알고리즘을 구현하였습니다.. 
> 제가 작성한 알고리즘들은 backtracking.py, csp_problems.py, constraints.py 안에 있습니다.
> 특히 비행기 스케쥴 문제를 제약 만족 문제로 푸는 과정은 어렵지만 흥미로웠습니다.
> 다음은 제가 작성한 알고리즘들입니다.
- Forward Checking
- Generalized	Arc	Consistency
- Various constraints
- Plane Scheduling as Constraint Satisfaction Problem
---------------------------------------------------------------------------

1. *Search*
> Modified version of UC Berkeley CSC188 Project 1 
> In this project, I have implemented various search algorithms to make the pacman agent to efficiently find paths and collect food in the maze world.
> I have experienced applying various search algorithms to the real project. It was easier to implement DFS, BFS or Uniform-cost Search, but I realized how important it is to find a good heiristic for A* Search.
> The lines of code that I have written are in search.py and searchAgents.py
> Followings are the search algorithms that I have applied to the pacman agent.
- Depth-First Search
- Breadth-First Search
- Uniform-cost Search
- A* Search with different heuristics

2. *Multi-Agent Pacman*
> Modified version of UC Berkeley CSC188 Project 2
> In this project, I have designed agents for the classic version of Pacman, including ghosts. I have implemented the various game tree search algorithms.
> The lines of code that I have written are in multiAgents.py
> Followings are the game tree search algorithms that I have applied to the pacman agent.
- Minimax
- Alpha-Beta Pruning
- Expectimax
- Evaluation Function

3. *Constraint Satisfaction Problems*
>  In this project, I have implemented Constraint Satisfaction Problems and backtracking search algorithm
> Representing Plane Scheduling as Constraint Satisfaction Problem was hard but interesting.
> My written codes are in backtracking.py, csp_problems.py, constraints.py.
> Followings are the implemented algorithms.
- Forward Checking
- Generalized	Arc	Consistency
- Various constraints
- Plane Scheduling as Constraint Satisfaction Problem
