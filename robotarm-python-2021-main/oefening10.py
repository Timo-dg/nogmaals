from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')
robotArm.speed = 3
# Jouw python instructies zet je vanaf hier:

for x in range(9, 0, -2):
    robotArm.grab()
    for y in range(0, x):
        robotArm.moveRight()   
    robotArm.drop()
    for zet in range(0, x - 1): 
        robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
