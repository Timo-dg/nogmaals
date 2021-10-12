from RobotArm import RobotArm
# Let op: hier start het anders voor een random level:
robotArm = RobotArm()
robotArm.randomLevel(1,7)
robotArm.speed = 3
# Jouw python instructies zet je vanaf hier:
for x in range(0, 8):
    robotArm.grab()
    color = robotArm.scan()
    if color != '':
        for y in range(x):
            robotArm.moveRight()
        robotArm.drop()
        for z in range(x):
            robotArm.moveLeft()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
