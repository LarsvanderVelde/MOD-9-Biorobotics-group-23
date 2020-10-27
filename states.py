class States(object):
    def __init__(self, bicep_left, bicep_right, calve):
        self.bicep_left = bicep_left
        self.bicep_right = bicep_right
        self.calve = calve
        return
    
    def move(self):
        position = [self.stationary(),self.moving_left(),self.moving_up(),self.moving_right(),self.moving_down()]
        change_position = [0, 0, 0, 0, 0]
        multiply = [0, -1, 2, 1, -2]
        for i in range(len(position)):
            change_position[i] += position[i] * multiply[i]
        for j in range(len(position)):
            if change_position[j] != 0:
                output = change_position[j]
        return change_position, output
    
    def stationary(self):
        if not any([self.bicep_left, self.bicep_right, self.calve]):
            stationary = True
        else:
            stationary = False
        return stationary

    def moving_up(self):
        if all([self.bicep_left, self.bicep_right]) and not (self.calve):
            move_up = True
        else:
            move_up = False
        return move_up 

    def moving_left(self):
        if self.bicep_left and not any([self.bicep_right, self.calve]):
            move_left = True
        else:
            move_left = False
        return move_left

    def moving_right(self):
        if self.bicep_right and not any([self.bicep_left, self.calve]):
            move_right = True
        else:
            move_right = False
        return move_right

    def moving_down(self):
        if self.calve and not any([self.bicep_left, self.bicep_right]):
            move_down = True
        else: 
            move_down = False
        return move_down