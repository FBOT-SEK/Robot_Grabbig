#!/usr/bin/env python3

# Import the necessary libraries
import time
import math
from ev3dev2.motor import *
from ev3dev2.sound import Sound
from ev3dev2.button import Button
from ev3dev2.sensor import *
from ev3dev2.sensor.lego import *
from time import sleep

# Create the sensors and motors objects
medium_motor_ouC = MediumMotor(OUTPUT_C)
motorA = LargeMotor(OUTPUT_A)
motorB = LargeMotor(OUTPUT_B)
left_motor = motorB
right_motor = motorA
tank_drive = MoveTank(OUTPUT_B, OUTPUT_A)
steering_drive = MoveSteering(OUTPUT_B, OUTPUT_A)
color_sensor_in1 = ColorSensor(INPUT_1)
color_sensor_in2 = ColorSensor(INPUT_2)


#code
cano = 0
preso = 0

def detectarCano():
    if color_sensor_in1.color != 0:
        cano == 1
    else:
        cano == 0

def pegarCano():
    medium_motor_ouC.on_for_seconds(-20, 2)

def soltarCano():
    medium_motor_ouC.on_for_seconds(20, 2)

while True:
    detectarCano()
    if cano == 1 and color_sensor_in1.color != color_sensor_in2.color and preso == 0:
        pegarCano()
        preso == 1
    elif cano == 1 and color_sensor_in1.color == color_sensor_in2.color and preso == 1:
        soltarCano()
        preso == 0
