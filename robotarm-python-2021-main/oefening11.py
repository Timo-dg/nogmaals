from RobotArm import RobotArm

robotArm = RobotArm('exercise 11')
robotArm.speed = 3
# Jouw python instructies zet je vanaf hier:
for x in range(8):
    robotArm.moveRight()
robotArm.grab()
color = robotArm.scan()
for x in range(9):  
    if color == 'white':
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()
        robotArm.moveLeft()
    else:
        robotArm.drop()
        robotArm.moveLeft()
    robotArm.grab()
    color = robotArm.scan()
robotArm.drop()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
