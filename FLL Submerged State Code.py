'''
This is our code for the Submerged Season. This is our code for the state competition (aka the thrid one). 
As of 2 - 1 - 2025, it is ready for comp.
'''
#Initialization
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

leftMotor = Motor(Port.E, Direction.COUNTERCLOCKWISE)
rightMotor = Motor(Port.F, Direction.CLOCKWISE)
topMotor = Motor(Port.D, Direction.CLOCKWISE)
backMotor = Motor(Port.C, Direction.CLOCKWISE)
rightColorSensor = ColorSensor(Port.B)
leftColorSensor = ColorSensor(Port.A)
driveBase = DriveBase(leftMotor, rightMotor, 56, 105)
driveBase.use_gyro(True)
driveBase.settings(turn_rate=550)
target_yaw = 0
init_yaw = 0
rate = 0
stopwatch = StopWatch()

if hub.battery.voltage()/90 < 81:
    hub.light.on(Color.RED)
print(hub.battery.voltage()/90)


#Missions
def unknownCreaturePt1():
    driveBase.settings(500, [500, 700], 120, [300, 300])
    backMotor.run_until_stalled(-180)
    backMotor.run_angle(180, 90, Stop.HOLD, False)
    driveBase.use_gyro(True)

    #Liftoff
    driveBase.curve(170, -45, Stop.COAST)

    #Align 
    driveBase.straight(380, Stop.NONE)
    leftMotor.run_time(275, 150, Stop.NONE)
    rightMotor.run_time(275, 150, Stop.NONE)
    driveBase.straight(35)
    driveBase.straight(-180)

    #To collection
    driveBase.turn(54)
    topMotor.run_time(-78, 2100, Stop.HOLD, False)
    driveBase.straight(320)
    driveBase.turn(20)
    driveBase.straight(30, Stop.HOLD, False)
    while not topMotor.done():
        pass
    topMotor.run_time(-78, 1000)

    #Garage closed
    driveBase.turn(-28)
    backMotor.run_until_stalled(-360, Stop.BRAKE)
    leftMotor.run_angle(300, -150)
    driveBase.straight(15)

    # CSL pos done :):):)
    driveBase.settings(200)
    backMotor.run_time(180, 1000, Stop.HOLD, False)
    driveBase.straight(-180)
    backMotor.run_time(-360, 250, Stop.COAST, False)
    driveBase.settings(800, 700, 850, 900)
    driveBase.straight(-120)
    backMotor.run_time(180, 400, Stop.HOLD, False)
    driveBase.curve(-120, 55, Stop.NONE)
    driveBase.curve(400, -20)

def collectShrimpPlankton():
    driveBase.settings(500, [500, 700], 120, [300, 300])
    backMotor.run_until_stalled(-180)
    backMotor.run_angle(180, 90, Stop.HOLD, False)
    driveBase.use_gyro(True)

    #Liftoff
    driveBase.curve(170, -45, Stop.COAST)

    #Align 
    driveBase.straight(380, Stop.NONE)
    leftMotor.run_time(275, 150, Stop.NONE)
    rightMotor.run_time(275, 150, Stop.NONE)
    driveBase.straight(35)
    driveBase.straight(-180)

    #To collection
    driveBase.turn(54)
    topMotor.run_time(-78, 2100, Stop.HOLD, False)
    driveBase.straight(320)
    driveBase.turn(20)
    driveBase.straight(30, Stop.HOLD, False)
    while not topMotor.done():
        pass
    topMotor.run_time(-78, 1000)

    #Garage closed
    driveBase.turn(-28)
    backMotor.run_until_stalled(-360, Stop.BRAKE)
    leftMotor.run_angle(300, -150)
    driveBase.straight(30)

    # CSL pos done
    driveBase.settings(200)
    backMotor.run_time(180, 1000, Stop.HOLD, False)
    driveBase.straight(-180)
    backMotor.run_time(-360, 250, Stop.COAST, False)
    driveBase.settings(800, 700, 850, 900)
    driveBase.straight(-120)
    backMotor.run_time(180, 400, Stop.HOLD, False)
    driveBase.curve(-120, 55, Stop.NONE)
    driveBase.curve(400, -20)

def artificialHabitat():
    driveBase.straight(-200)
    driveBase.turn(-27) 
    backMotor.run_angle(-360, 150)
    driveBase.turn(-85)
    driveBase.straight(-77)
    driveBase.turn(-60)

def seabedSample():
    driveBase.settings(500, [500, 700], 120, [300, 300])
    leftMotor.run_angle(230, 20)
    topMotor.run_time(-360, 270, Stop.HOLD, False)
    backMotor.run_until_stalled(-180)
    topMotor.run_angle(180, -90, Stop.HOLD, False)
    driveBase.use_gyro(True)

    # Liftoff
    driveBase.straight(-50)
    driveBase.turn(-59)
    driveBase.straight(-700)
    backMotor.run_angle(180, 64, Stop.HOLD, False)
    driveBase.turn(30)
    driveBase.straight(-245)
    topMotor.run(1000)
    topMotor.run_angle(1000, 180, Stop.HOLD, True) #Drop Octopus
    driveBase.turn(-19)
    driveBase.straight(-247)
    driveBase.turn(48)
    driveBase.use_gyro(False)
    driveBase.straight(-150, Stop.HOLD, False)
    while not (driveBase.done() or driveBase.stalled()):
        pass
    driveBase.use_gyro(True)
    topMotor.run_angle(360, 110, Stop.COAST, False)
    backMotor.run_until_stalled(-50, Stop.HOLD) #Pick up Seabed sample and Submersible
    driveBase.reset()
    driveBase.use_gyro(True)
    driveBase.settings(500, [500, 700], 120, [300, 300])
    leftMotor.run_time(360, 150)
    driveBase.straight(150)
    topMotor.run_time(-90, 1280, Stop.HOLD, False)
    wait(500)
    driveBase.straight(-90)
    driveBase.settings(800, [800, 800], 500, [800, 800])
    driveBase.turn(-94)
    print(driveBase.angle())
    driveBase.straight(-350)
    driveBase.curve(-105, 43, Stop.NONE)
    driveBase.straight(-700)

def anglerFish():
    # do anglerfish
    driveBase.straight(100)
    driveBase.straight(-100)
    driveBase.turn(20)

def shark(): 
    #go to shark
    driveBase.turn(10)
    driveBase.straight(300)
    driveBase.turn(-30)
    driveBase.straight(200)
    driveBase.turn(18)
    #shark
    driveBase.straight(400)
    driveBase.straight(-40)
    #go back
    driveBase.turn(40)
    driveBase.straight(-200)

def collectResearchVessel():
    driveBase.straight(300)
    driveBase.straight(-400)

def sonarDiscovery():
    driveBase.use_gyro(True)
    driveBase.settings(300)
    driveBase.straight(750)
    topMotor.run_time(-100, 2500)

def shippingLanes():
    driveBase.straight(-150)
    driveBase.curve(-50,35)
    backMotor.run_time(-100, 700)
    driveBase.turn(10)
    driveBase.straight(-200)
    backMotor.run_time(100, 800)
    wait(500)
    driveBase.turn(50)
    driveBase.straight(-500)

def raiseMastKrakensTresure():
    driveBase.reset()
    driveBase.settings(straight_speed=800,straight_acceleration = 733, turn_rate = 1000, turn_acceleration = 200)
    driveBase.use_gyro(True)
    driveBase.straight(100)
    driveBase.turn(-47)
    driveBase.straight(105)
    driveBase.curve(305, 88)
    wait(250)
    driveBase.settings(straight_speed=100,straight_acceleration = 733, turn_rate = 177, turn_acceleration = 800)
    driveBase.straight(110)
    topMotor.run_angle(500, 45)
    driveBase.settings(straight_speed=800,straight_acceleration = 733, turn_rate = 100, turn_acceleration = 800)
    driveBase.straight(30)
    driveBase.straight(-275)
    driveBase.turn(-55)
    driveBase.straight(-650)

def collectTrident():
    driveBase.use_gyro(False)
    driveBase.turn(-85) # Turn to P2
    driveBase.use_gyro(True)
    driveBase.straight(85)
    driveBase.settings(turn_rate=1000)
    topMotor.run_angle(90, 60)# Drop shark
    driveBase.turn(15)
    driveBase.straight(100)
    topMotor.run_angle(90, 60)
    topMotor.run_angle(10, -60,) # trident🔱🔱🔱🔱🔱
    driveBase.straight(-150)
    driveBase.straight(150)
    driveBase.curve(-400, -45)
    driveBase.straight(-900)

def deliverResearchVesselCoral():
    driveBase.use_gyro(True)
    driveBase.settings(500)
    driveBase.use_gyro(True)
    driveBase.straight(175)
    driveBase.turn(90)
    driveBase.straight(300)
    topMotor.run_time(-500, 655)
    driveBase.settings(195)
    driveBase.turn(-5)
    driveBase.straight(785)
    driveBase.turn(5)
    topMotor.run_time(300,655) # Lift the Research vessel arm
    backMotor.run_angle(800, 150) # Lift artificial habitat
    driveBase.straight(-170)
    backMotor.run_angle(500, -360)
    driveBase.settings(900)
    driveBase.straight(-200)
    driveBase.turn(-40)
    driveBase.curve(340, 60, Stop.COAST)
    driveBase.straight(700)

def feedWhale():
    driveBase.use_gyro(True)
    driveBase.settings(500, turn_rate=70)
    driveBase.turn(-40)
    driveBase.straight(585)
    driveBase.turn(79)
    driveBase.settings(800, turn_rate=100)
    driveBase.straight(520, Stop.COAST)
    driveBase.settings(80)
    wait(100)
    driveBase.straight(100)
    driveBase.settings(200)
    driveBase.straight(245, Stop.NONE, False)
    wait(100)
    driveBase.settings(500)
    driveBase.straight(-220)
    driveBase.turn(90)

    #go alignish to Sonar
    driveBase.use_gyro(False)
    driveBase.straight(-79)
    driveBase.turn(-7)
    backMotor.run_angle(300,-400, Stop.HOLD, False)
    wait(2000)
    driveBase.settings(100)
    driveBase.straight(30)

def sendOverSubmersible():
    driveBase.straight(-150)
    driveBase.turn(47)
    driveBase.straight(-235)
    driveBase.turn(-16)
    backMotor.run_angle(475, -1250, Stop.HOLD, False)
    driveBase.settings(35)
    driveBase.straight(-50)
    driveBase.settings(600)
    wait(2000)
    driveBase.straight(100) 

def unknownCreaturePt2():
    driveBase.straight(-210)
    driveBase.turn(50)
    driveBase.straight(-125)
    backMotor.run_angle(800, 750)

def coralNurseryPickUp():
    driveBase.use_gyro(True)
    driveBase.settings(500, [500, 500], 120, [300, 300])
    backMotor.run_time(-250, 100)
    topMotor.run_until_stalled(-500)
    print(driveBase.angle())
    driveBase.turn(29, Stop.BRAKE)
    print(driveBase.angle())
    driveBase.straight(520, Stop.BRAKE)
    driveBase.turn(-36)
    topMotor.run_angle(100, 160)
    driveBase.use_gyro(False)
    driveBase.straight(330, Stop.BRAKE)
    driveBase.turn(10)
    driveBase.straight(55)
    wait(250)
    driveBase.settings(500, [300, 300], 120, [300, 300])
    driveBase.reset()
    driveBase.straight(-27, Stop.BRAKE)
    topMotor.run_time(300, 500)
    wait(500)
    topMotor.run_angle(-500, 130)
    driveBase.reset()

    #Done with Reef
    driveBase.straight(-310, Stop.BRAKE)
    topMotor.run_until_stalled(-500)
    driveBase.turn(112)
    backMotor.run_time(500, 1000)
    driveBase.straight(-100)
    backMotor.run_time(-250, 700)
    driveBase.straight(100)
    driveBase.turn(25)
    driveBase.straight(-200, Stop.BRAKE)
    driveBase.turn(-10)
    driveBase.straight(-100)
    driveBase.curve(450, 180)

def collectDiver():
    #get diver
    topMotor.run_time(150, 1300)
    driveBase.turn(-10)
    topMotor.run_time(180,1300)
    driveBase.turn(10)
    #go back
    driveBase.settings(100)
    driveBase.turn(20)
    driveBase.turn(-20)
    driveBase.straight(-500)
    driveBase.turn(90)
    driveBase.straight(-50)

def deliverDiverCoralReef():
    #quickly pull back
    driveBase.use_gyro(False)
    wait(9000)
    driveBase.settings(500)
    driveBase.use_gyro(True)
    driveBase.straight(-650)

def coralNurseryFlipPlants():
    #do coral farm
    driveBase.turn(-45)
    driveBase.straight(20)
    driveBase.turn(-30)
    driveBase.straight(-45)
    driveBase.turn(80)
    driveBase.straight(600)

#Runs
def run1():
    collectShrimpPlankton()
    driveBase.use_gyro(False)

def run2():
    seabedSample()
    driveBase.use_gyro(False)

def run3():    
    coralNurseryPickUp()
    driveBase.use_gyro(False)

def run4():
    raiseMastKrakensTresure()
    driveBase.use_gyro(False)

def run5():
    deliverResearchVesselCoral()
    driveBase.use_gyro(False)

def run6():
    feedWhale() 
    driveBase.use_gyro(False)

#Menu System Setup
runDefined = [run1, run2, run3, run4, run5, run6]   

global runNum
runNum = 1
hub.system.set_stop_button({Button.LEFT, Button.RIGHT})

#Menu System Funcs.
def changeRun(buttonPressed = "LEFT"):
    global runNum
    if buttonPressed == "RIGHT":
        if runNum == 6:
                runNum = 1
        else:
                runNum += 1
    else:
        if runNum == 1:
                runNum = 6
        else:
            runNum -= 1
    wait(300)

#Menu System
while True:
    #Always running code (displaying stats)
    if hub.battery.voltage() <= 3.9:
        hub.light.on(Color.ORANGE)
    else:
        hub.light.on(Color.GREEN)
    hub.display.number(runNum)
    
    #Changing runs
    if hub.buttons.pressed() == {Button.RIGHT}:
        changeRun("RIGHT")
    elif hub.buttons.pressed() == {Button.LEFT}:
        changeRun()
    
    #Execute Runs
    if hub.buttons.pressed() == {Button.CENTER}:
        stopwatch.reset()
        runDefined[runNum - 1]()            
        totalTime = stopwatch.time()
        wait(300)
        print(f"Run {runNum} Time = {totalTime}")
        changeRun("RIGHT")