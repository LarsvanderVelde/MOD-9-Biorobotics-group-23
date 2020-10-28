from states import States 
from Current_position import Angles

bicep_left = 0
bicep_right = 0
calve = 1

solver = States(bicep_left,bicep_right,calve)
print(solver.move())

robot = Angles()
robot.go_moving(solver.move())
