# --------------------- Modules ----->
import time
import board
import digitalio
from adafruit_motor import stepper

# --------------------- Setup ----->
DELAY = 0.001

# Motor 1
coilsA = (
    digitalio.DigitalInOut(board.D18),  # A1
    digitalio.DigitalInOut(board.D17),  # A2
    digitalio.DigitalInOut(board.D27),  # B1
    digitalio.DigitalInOut(board.D22),  # B2
)

for coilA in coilsA:
    coilA.direction = digitalio.Direction.OUTPUT

motorA = stepper.StepperMotor(coilsA[0], coilsA[1], coilsA[2], coilsA[3], microsteps=None)

# Motor 2
coilsB = (
    digitalio.DigitalInOut(board.D16),  # A1
    digitalio.DigitalInOut(board.D25),  # A2
    digitalio.DigitalInOut(board.D23),  # B1
    digitalio.DigitalInOut(board.D24),  # B2
)

for coilB in coilsB:
    coilB.direction = digitalio.Direction.OUTPUT

motorB = stepper.StepperMotor(coilsB[0], coilsB[1], coilsB[2], coilsB[3], microsteps=None)

# --------------------- Functions ----->
# Motor 1
def StepAFor(STEPS):
    for step in range(STEPS):
        motorA.onestep()
        time.sleep(DELAY)
        
    motorA.release()

def StepABack(STEPS):
    for step in range(STEPS):
        motorA.onestep(direction=stepper.BACKWARD)
        time.sleep(DELAY)
        
    motorA.release()
  # height 4, 1st triangle protrude out 1.5 cm 2nd is 1.6 cm. Width is 1.5
# Motor 2
def StepBFor(STEPS):
    for step in range(STEPS):
        motorB.onestep()
        time.sleep(DELAY)
        
    motorB.release()

def StepBBack(STEPS):
    for step in range(STEPS):
        motorB.onestep(direction=stepper.BACKWARD)
        time.sleep(DELAY)
        
    motorB.release()