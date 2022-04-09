## Abstract
This is a report of my rush hour puzzle AI solver, where I implement five searching algorithms: BFS, DFS, IDS, A*, IDA* to solve the game.

## Introduction
Rush Hour is a sliding block puzzle invented by Nob Yoshigahara in the 1970s. The game board is a 6x6 grid with cars on it. Each car has its own postion, length, orientation. The final goal of the game is to move the red car out the grid(to the right). Each problem will have different initial grid which comes with different difficulties.
<img align = 'right' src=report/rush_hour.png>

## Goal
In this project my goal is to solve the rush hour puzzle with serveral searching algorithms, including some uninformed search such like Breadth First Search, Depth First Search, Iterative Deepening Search, and some informed search such like A* Search, Iterative Deepening A* Search. For uninformed search, I will simply solve the puzzle, while in informed search, I will test some heuristic to find the best one.  Last but not least, I will compare these algorithms in different metrics and analyze their pros and cons.

## Approach
I finished all the coding with python. All of my code is in the **Appendix** section of this report and also available on my [github](https://github.com/ben0919/Rush_Hour_GAME_Solver). 
I simply implement the rush hour puzzle with two classes. Car, where I store some basic information of a car such like id, position, length, orientation, and define some method such like how to move them and how to get their occupied area. Gameboard, where I read the input and put all the cars on. For each car, I don't put only one car on the board but several same cars on its occupied area, which can make the search easier.
```python
def add_car(self, car):
    if car.orientataion == 'horizontal':
        y = car.start_location[0]
        for x in range(car.start_location[1], car.start_location[1] + car.length):
            self.grid[y][x] = car
    else:
        x = car.start_location[1]
        for y in range(car.start_location[0], car.start_location[0] + car.length):
            self.grid[y][x] = car
``` 
For all the searching algorithms, I implement them in an another class, solver. I simply implement the frontier as a _list_, and the explored set as a _set_ for doing graph search. For IDS and IDA*, the explored set is implement by a _dictionary_, where I can keep track of the minimum depth and score.
#### Heuristics
For A* and IDA*, heuristics is needed. In addition of the heuristic function which the teacher offered, I also design two more heuristic functions.
##### Blocking Heuristic
The number of cars directly blocking the way of the red car to the exit.
##### Distance Heuristic
The distance of the red car from the exit.
##### Hybrid Heuristic 
Its a hybrid version of the above two heuristcs, that is, the number of cars directly blocking the way of the red car to the exit plus the distance of the red car from the exit.
## Results
#### Heuristics
As I mentioned above, in addition of blocking heuristics, I design two more heuristic functions. To tell which heuristic fuction is the best, I tested them on A* and sum up the number of expanded nodes after running several input files: 
<img src =report/heuristics.png> 
It shows that the **hybrid heuristic** is the best since it has the least number of expand nodes. So I choose **hybrid heuristic** for A* and IDA*.

#### Searching
To compare the five searching algorithms, I used four metrics: number of steps to solution, number of expanded nodes, peak memory usage and total execution time. For number of steps, it's the depth of the search. For number of expanded nodes, it's simply the length of the explored set. As for tracing mememory usage and execution time, I used python standard library _tracemalloc_ and _time_. I found that using _tracemalloc_ will slow down the program. However, I'm only comparing the relative speed of the five algorithm, so it's fine to put them all in the program.
These are the results running on different input files:
<img src=report/L02.png>
<img src=report/L10.png>
<img src=report/L20.png>
<img src=report/L31.png>
The comparision between each algorithm is mentioned in the **Observation and Conclusion** section.

## Observation and Conclusion
1. DFS is the fastest algorithm (O(b^m)), but the solution isn't optimal.
2. BFS has the optimal solution but it use a lot of memory (O(b^d)).
3. IDS surely can use less memory (O(bd)) while getting the optimal solution, but it costs a huge amount of time (O(b^d)).
4. IDA* costs more time to run but only has a similar performance compared to A*, which is a little bit weird. 
5. With appropriate heuristics, searching can become easier since the number of expanded nodes is less while also getting the optimal solution.

## Discussion
1. How to implement the explored set if you want to do graph search? Is the extra time and space worth it?
Ans: I only did graph search in this project, and the approach is simply having a explored set to get track of the same states. 
2. Can you improve on the provided heuristic function, or devise new ones? If you do, be sure to make comparisons of how they affect the evaluation metrics.
Ans: I design two more heuristic function, distance heuristic and hybrid heuristic, and it comes out that hybrid heuristc has the best performance since it have the least number of expanded nodes(see **Results-Heuristics** section).

## What I Learned
1. How to implement several searching algorithms in games like rush hour puzzle.   
2. How to analyze these algorithms with different metrics.

## Future Works
1. Implement GUI interface.
2. Implement automatic puzzle generator with different difficulties.
3. Improve IDS and IDA* speed.
4. Find out why IDA* costs more time than A* but only has a similar preformance with A*.
## Reference
[1] https://en.wikipedia.org/wiki/Rush_Hour_(puzzle)
[2] https://github.com/CirXe0N/RushHourSolver

<div style="page-break-after: always;"></div>
