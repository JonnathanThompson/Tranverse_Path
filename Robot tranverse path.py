import time #imports time libary that are needed to run this code
import board #imports board libary that are needed to run this code
import digitalio #imports digitalio libary that are needed to run this code
import pwmio #imports libaries that are needed to run this code

from adafruit_motor import motor #imports a small section of adafruit_motor libary

left_motor_forward = board.GP12 #Initilizes the varibale left_motor_forward and attaches it to GP12
left_motor_backwards = board.GP13 #Initilizes the varibale left_motor_backwards and attaches it to GP13

pwm_La = pwmio.PWMOut(left_motor_forward, frequency=10000) #Tells the pico that this component is an output (and some other configuration)
pwm_Lb = pwmio.PWMOut(left_motor_backwards, frequency=10000) #Tells the pico that this component is an output (and some other configuration)

Left_Motor = motor.DCMotor(pwm_La, pwm_Lb) #Intilaizes Left_Motor and configuration line and it is required
Left_Motor_speed = 0 #Intilaizes the variable Left_Motor_speed to 0


right_motor_forward = board.GP14 #Initilizes the varibale right_motor_forward and attaches it to GP14
right_motor_backwards = board.GP15 #Initilizes the varibale right_motor_backwards and attaches it to GP15


pwm_La = pwmio.PWMOut(right_motor_forward, frequency=10000) #Tells the pico that this component is an output (and some other configuration)
pwm_Lb = pwmio.PWMOut(right_motor_backwards, frequency=10000) #Tells the pico that this component is an output (and some other configuration)

Right_Motor = motor.DCMotor(pwm_La, pwm_Lb) #Intilaizes Right_Motor and configuration line and it is required
Right_Motor_speed = 0 #Intilaizes the variable Right_Motor_speed to 0

def Robot_forward():
    Left_Motor_speed = -1
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = -1
    Right_Motor.throttle = Right_Motor_speed

def Robot_backwards():
    Left_Motor_speed = 1
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = 1
    Right_Motor.throttle = Right_Motor_speed


def Robot_right():
    Left_Motor_speed = 1
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = -1
    Right_Motor.throttle = Right_Motor_speed


def Robot_left():
    Left_Motor_speed = -1
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = 1
    Right_Motor.throttle = Right_Motor_speed

def Robot_stop():
    Left_Motor_speed = 0
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = 0
    Right_Motor.throttle = Right_Motor_speed

while True:

    Robot_backwards()
'''time.sleep(1.7)
Robot_right()
time.sleep(.3)
Robot_forward
time.sleep(2)
Robot_right
time.sleep(.5)
Robot_forward
time.sleep(.7)
Robot_left
time.sleep(.5)
Robot_forward
time.sleep(.5)
Robot_left
time.sleep(.5)
Robot_forward
time.sleep(.7)
Robot_right
time.sleep(.5)
Robot_forward
time.sleep(.5)
Robot_right
time.sleep(.5)
Robot_forward
time.sleep(.8)'''
# Write your code here :-)
