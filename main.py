from states import States 
bicep_left = 0
bicep_right = 0
calve = 1

solver = States(bicep_left,bicep_right,calve)
print(solver.move())