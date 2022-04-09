class Car():
    def __init__(self, id, y, x, length, orientataion):
        self.id = id
        self.start_location = [y, x]
        self.length = length
        self.orientataion = orientataion

    def move_forward(self):
        if self.orientataion == 'horizontal':
            self.start_location[1] += 1
        else:
            self.start_location[0] += 1

    def move_backward(self):
        if self.orientataion == 'horizontal':
            self.start_location[1] -= 1
        else:
            self.start_location[0] -= 1

    def get_id(self):
        return self.id 
        
    def get_start_location(self):
        return self.start_location

    def get_end_location(self):
        if self.orientataion == 'horizontal':
            return [self.start_location[0], self.start_location[1] + self.length - 1]
        else:
            return [self.start_location[0] + self.length - 1, self.start_location[1]]

    def get_ocuupied_locations(self):
        self.occupied_location = []
        if self.orientataion == 'horizontal':
            y = self.start_location[0]
            for x in range(self.start_location[1], self.start_location[1] + self.length):
                self.occupied_location.append([y, x])
        else:
            x = self.start_location[1]
            for y in range(self.start_location[0], self.start_location[0] + self.length):
                self.occupied_location.append([y, x])
        return self.occupied_location

    def get_orientation(self):
        return self.orientataion

    def __repr__(self):
        return self.id