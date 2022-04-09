from gameboard import GameBoard
from solver import Solver
from prettytable import PrettyTable

algo = int(input('Please select an algorithm to solve the game\n(1 for BFS, 2 for DFS, 3 for IDS, 4 for A*, 5 for IDA*): '))

input_file = input('Please input the file name: ')

gameboard = GameBoard(6, 6)
gameboard.read_board('tests/' + input_file)

solver = Solver(gameboard)
if algo == 1:
    solution, node_num, memory_usage, execution_time, step_num = solver.BFS()
elif algo == 2:
    solution, node_num, memory_usage, execution_time, step_num = solver.DFS()
elif algo == 3:
    solution, node_num, memory_usage, execution_time, step_num = solver.IDS()
elif algo == 4:
    solution, node_num, memory_usage, execution_time, step_num = solver.A_star()
elif algo == 5:
    solution, node_num, memory_usage, execution_time, step_num = solver.IDA_star()

print('Problem: ' + input_file)
print(gameboard)
if algo == 1:
    print('Algorithm: BFS')
elif algo == 2:
    print('Algorithm: DFS')
elif algo == 3:
    print('Algorithm: IDS')
elif algo == 4:
    print('Algorithm: A*')
elif algo == 5:
    print('Algorithm: IDA*')

print(solution)
print('Number of steps: %d' % step_num)
print('Number of expanded nodes: %d' % node_num)
print('Peak memory usage: %.2f MB' % memory_usage)
print('Total execution time: %.2f sec' % execution_time)

