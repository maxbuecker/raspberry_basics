#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

green = 18 #Pin Number RPi Board
red = 20 #Pin Number RPi Board

GPIO.setmode(GPIO.BOARD)
GPIO.setup(green, GPIO.OUT, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(red, GPIO.OUT, pull_up_down=GPIO.PUD_DOWN)

n = 10

for i in range(n):
  if (i==0) & (i==2) & (i==4) & (i==6) & (i==8):
    GPIO.output(green,GPIO.HIGH) #turn on green LED
    GPIO.output(red, GPIO.LOW) #turn off red LED
  else:
    GPIO.output(green,GPIO.LOW) #turn off green LED
    GPIO.output(red, GPIO.HIGH) #turn on red LED
  print('Iteration ' + str(i) + '/' + str(n))
  time.sleep(1000)

GPIO.cleanup()
