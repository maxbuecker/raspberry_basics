#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

green = 11 #Pin Number RPi Board
red = 18 #Pin Number RPi Board

GPIO.setmode(GPIO.BOARD)
GPIO.setup(green, GPIO.OUT, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(red, GPIO.OUT, pull_up_down=GPIO.PUD_DOWN)

n = 0
nmax = 30

while n != nmax:
  GPIO.output(green,GPIO.HIGH) #turn on green LED
  GPIO.output(red, GPIO.LOW) #turn off red LED
  time.sleep(500)
  GPIO.output(green,GPIO.LOW) #turn off green LED
  GPIO.output(red, GPIO.HIGH) #turn on red LED
  time.sleep(500)
  n += 1
  
GPIO.cleanup()
