from car import Car

class GameBoard():
    def __init__(self, height, width):
        self.grid = []
        self.height = height
        self.width = width
        self.generate_grid()
        self.cars = {}

    def generate_grid(self):
        for i in range(self.height):
            self.grid.append([])
            for j in range(self.width):
                self.grid[i].append('.')

    def read_board(self, filename):
        f = open(filename, 'r')
        content = f.readlines()
        f.close()
        data = []
        for line in content:
            data.append(line.split())
        for i in range(len(data)):
            orientataion = ''
            if data[i][4] == '1':
                orientataion = 'horizontal'
            else:
                orientataion = 'vertical'
            car = Car(data[i][0], int(data[i][1]), int(data[i][2]), int(data[i][3]), orientataion)
            self.add_car(car)

    def add_car(self, car):
        if car.orientataion == 'horizontal':
            y = car.start_location[0]
            for x in range(car.start_location[1], car.start_location[1] + car.length):
                self.grid[y][x] = car
        else:
            x = car.start_location[1]
            for y in range(car.start_location[0], car.start_location[0] + car.length):
                self.grid[y][x] = car

    def get_height(self):
        return self.height

    def get_width(self):
        return self.width

    def get_grid(self):
        return self.grid
        
    def __str__(self):
        string = 'Game Board:\n'
        for i in range(self.height):
            for j in range(self.width):
                string += '{:^3s}'.format((str(self.grid[i][j])))
            string += '\n'
        return string