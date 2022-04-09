import copy
import tracemalloc
import time

class Solver():
    def __init__(self, board):
        self.game_board = board
        self.solotion = ''

    def BFS(self):
        tracemalloc.start()
        start_time = time.time()
        self.solotion = 'Solution <car_index, new_row, new_column>: \n'
        grid = self.game_board.get_grid()
        explored = set()
        frontier = [[[], grid, 0]]
        explored.add(hash(str(grid)))
        while len(frontier)>0:
            moves, grid, step_num = frontier.pop(0)
            if self.is_solved(grid):
                for step in moves:
                    self.solotion += '< '
                    self.solotion += str(step[0])
                    self.solotion += ', '
                    self.solotion += str(step[1][0])
                    self.solotion += ', '
                    self.solotion += str(step[1][1])
                    self.solotion += ' >'
                    self.solotion += '\n'
                current, peak = tracemalloc.get_traced_memory()
                tracemalloc.stop()
                return [self.solotion, len(explored), peak/10**6, time.time()-start_time, step_num]
            for new_moves, new_grid in self.get_states(grid):
                if hash(str(new_grid)) not in explored:
                    frontier.append([moves + new_moves, new_grid, step_num + 1])
                    explored.add(hash(str(new_grid)))
        return 'No Solution'

    def DFS(self):
        tracemalloc.start()
        start_time = time.time()
        self.solotion = 'Solution <car_index, new_row, new_column>: \n'
        grid = self.game_board.get_grid()
        explored = set()
        frontier = [[[], grid, 0]]
        explored.add(hash(str(grid)))
        while len(frontier)>0:
            moves, grid, step_num = frontier[-1]
            if self.is_solved(grid):
                for step in moves:
                    self.solotion += '< '
                    self.solotion += str(step[0])
                    self.solotion += ', '
                    self.solotion += str(step[1][0])
                    self.solotion += ', '
                    self.solotion += str(step[1][1])
                    self.solotion += ' >'
                    self.solotion += '\n'
                current, peak = tracemalloc.get_traced_memory()
                tracemalloc.stop()
                return [self.solotion, len(explored), peak/10**6, time.time()-start_time, step_num]
            states = self.get_states(grid)
            flag = True
            for new_moves, new_grid in states:
                if hash(str(new_grid)) not in explored:
                    frontier.append([moves + new_moves, new_grid, step_num + 1])
                    explored.add(hash(str(new_grid)))
                    flag = False
            if flag:
                del frontier[-1]

        return 'No Solution'

    def IDS(self):
        tracemalloc.start()
        start_time = time.time()
        max_depth = 0 
        while True:
            self.solotion = 'Solution <car_index, new_row, new_column>: \n'
            grid = self.game_board.get_grid()
            explored = {}
            frontier = [[[], grid, 0, 0]]
            explored[hash(str(grid))] = 0
            while len(frontier) > 0:
                moves, grid , depth, step_num = frontier[-1]
                if self.is_solved(grid):
                    for step in moves:
                        self.solotion += '< '
                        self.solotion += str(step[0])
                        self.solotion += ', '
                        self.solotion += str(step[1][0])
                        self.solotion += ', '
                        self.solotion += str(step[1][1])
                        self.solotion += ' >'
                        self.solotion += '\n'
                    current, peak = tracemalloc.get_traced_memory()
                    tracemalloc.stop()
                    return [self.solotion, len(explored), peak/10**6, time.time()-start_time, step_num]
                if depth > max_depth:
                    del frontier[-1]
                    continue
                states = self.get_states(grid)
                flag = True
                for new_moves, new_grid in states:
                    if hash(str(new_grid)) not in explored:
                        frontier.append([moves + new_moves, new_grid, (depth + 1), step_num + 1])
                        explored[hash(str(new_grid))] = depth+1
                        flag = False
                    elif depth+1 < explored[hash(str(new_grid))]:
                        frontier.append([moves + new_moves, new_grid, (depth + 1), step_num + 1])
                        explored[hash(str(new_grid))] = depth+1
                        flag = False
                if flag:
                    del frontier[-1]
            max_depth += 1
        return 'No Solution'

    def A_star(self):
        tracemalloc.start()
        start_time = time.time()
        self.solotion = 'Solution <car_index, new_row, new_column>: \n'
        grid = self.game_board.get_grid()
        h_score = self.hybrid_heuristic_score(grid)
        f_score = 0 + h_score
        explored = set()
        frontier = [[[], grid, f_score, 0]]
        explored.add(hash(str(grid)))
        while len(frontier) > 0:
            index = self.min_score_index(frontier)
            moves, grid, f_score, step_num = frontier[index]
            if self.is_solved(grid):
                for step in moves:
                    self.solotion += '< '
                    self.solotion += str(step[0])
                    self.solotion += ', '
                    self.solotion += str(step[1][0])
                    self.solotion += ', '
                    self.solotion += str(step[1][1])
                    self.solotion += ' >'
                    self.solotion += '\n'
                current, peak = tracemalloc.get_traced_memory()
                tracemalloc.stop()
                return [self.solotion, len(explored), peak/10**6, time.time()-start_time, step_num]
            states = self.get_states(grid)
            flag = True
            for new_moves, new_grid in states:
                new_h_score = self.hybrid_heuristic_score(new_grid)
                new_g_score = step_num + 1
                new_f_score = new_g_score + new_h_score
                if hash(str(new_grid)) not in explored:
                    frontier.append([moves + new_moves, new_grid, new_f_score, step_num + 1])
                    explored.add(hash(str(new_grid)))
                    flag = False
            if flag:
                del frontier[index]
        return "No Solution"

    def IDA_star(self):
        tracemalloc.start()
        start_time = time.time()
        max_score = 0 
        while True:
            self.solotion = 'Solution <car_index, new_row, new_column>: \n'
            grid = self.game_board.get_grid()
            h_score = self.hybrid_heuristic_score(grid)
            f_score = 0 + h_score
            explored = {}
            frontier = [[[], grid, f_score, 0]]
            explored[hash(str(grid))] = f_score
            while len(frontier) > 0:
                index = self.min_score_index(frontier)
                moves, grid, f_score, step_num = frontier[index]
                if self.is_solved(grid):
                    for step in moves:
                        self.solotion += '< '
                        self.solotion += str(step[0])
                        self.solotion += ', '
                        self.solotion += str(step[1][0])
                        self.solotion += ', '
                        self.solotion += str(step[1][1])
                        self.solotion += ' >'
                        self.solotion += '\n'
                    current, peak = tracemalloc.get_traced_memory()
                    tracemalloc.stop()
                    return [self.solotion, len(explored), peak/10**6, time.time()-start_time, step_num]
                if f_score > max_score:
                    del frontier[index]
                    continue
                states = self.get_states(grid)
                flag = True
                for new_moves, new_grid in states:
                    new_h_score = self.hybrid_heuristic_score(new_grid)
                    new_g_score = step_num + 1
                    new_f_score = new_g_score + new_h_score
                    if hash(str(new_grid)) not in explored:
                        frontier.append([moves + new_moves, new_grid, new_f_score, step_num + 1])
                        explored[hash(str(new_grid))] = new_f_score
                        flag = False
                    elif new_f_score < explored[hash(str(new_grid))]:
                        frontier.append([moves + new_moves, new_grid, new_f_score, step_num + 1])
                        explored[hash(str(new_grid))] = new_f_score
                        flag = False
                if flag:
                    del frontier[index]
            max_score += 1
        return 'No Solution'

    def get_states(self, grid):
        states = []
        for i in range(self.game_board.get_height()):
            for j in range(self.game_board.get_width()):
                car = grid[i][j]
                if car != '.':
                    for direction in ['Forward', 'Backward']:
                        if self.is_movable(car, direction, grid):
                            new_grid = copy.deepcopy(grid)
                            new_car = copy.deepcopy(grid[i][j])
                            if direction == 'Forward':
                                new_car.move_forward()
                            if direction == 'Backward':
                                new_car.move_backward()
                            old_locations = car.get_ocuupied_locations()
                            new_locations = new_car.get_ocuupied_locations()
                            new_grid = self.update_grid(new_grid, new_car, old_locations, new_locations)
                            states.append([[[car, new_car.get_start_location()]], new_grid])
        return states

    def is_movable(self, car, direction, grid):
        if car.get_orientation() == 'horizontal':
            if direction == 'Forward':
                end = car.get_end_location()
                x = end[1] + 1
                y = end[0]
                if x < self.game_board.get_width() and grid[y][x] == '.':
                    return True
                else:
                    return False
            if direction == 'Backward':
                start = car.get_start_location()
                x = start[1] - 1
                y = start[0]
                if x > -1 and grid[y][x] == '.':
                    return True
                else:
                    return False
        if car.get_orientation() == 'vertical':
            if direction == 'Forward':
                end = car.get_end_location()
                x = end[1] 
                y = end[0] + 1
                if y < self.game_board.get_height() and grid[y][x] == '.':
                    return True
                else:
                    return False
            if direction == 'Backward':
                start = car.get_start_location()
                x = start[1] 
                y = start[0] - 1
                if y > -1 and grid[y][x] == '.':
                    return True
                else:
                    return False

    def update_grid(self, grid, car, old_locations, new_locations):
        for i in old_locations:
            grid[i[0]][i[1]] = '.'
        for i in new_locations:
            grid[i[0]][i[1]] = car
        return grid

    def is_solved(self, grid):
        if grid[2][4] != '.' and grid[2][5] != '.':
            if grid[2][4].id == '0' and grid[2][5].id == '0':
                return True
        else:
            return False

    def blocking_heuristic_score(self, grid):
        i = 0
        counter = 0
        while i < len(grid):
            if grid[2][i] != '.' and grid[2][i].get_id() == '0':
                i += 1
                break
            i += 1
        while i < len(grid):
            if grid[2][i] != '.':
                counter += 1
            i += 1 
        return counter

    def distance_heuristic_score(self, grid):
        i = 0
        for i in range(len(grid)):
            if grid[2][i] != '.' and grid[2][i].get_id() == '0':
                break
        return len(grid) - i - 2

    def hybrid_heuristic_score(self, grid):
        return self.blocking_heuristic_score(grid) + self.distance_heuristic_score(grid)
 
    def min_score_index(self, frontier):
        min = 100
        index = -1
        for i in range(len(frontier)):
            if frontier[i][2] < min:
                min = frontier[i][2]
                index = i
        return index