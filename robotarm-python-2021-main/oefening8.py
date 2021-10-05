from RobotArm import RobotArm

robotArm = RobotArm('exercise 8')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 3  
robotArm.moveRight()
for x in range(0, 7):
    for x in range(8):
            robotArm.grab()
            robotArm.moveRight()
    robotArm.drop()
    for x in range(8):
        robotArm.moveLeft()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
