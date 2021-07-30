#!/usr/bin/python3

import RPi.GPIO as GPIO
import time
import bme280
import smbus2

port = 1
address = 0x77 # Default Slave Adress! Adress when HIGH: 0x77, Adress when LOW: 0x76
bus = smbus2.SMBus(port)

bme280.load_calibration_params(bus,address)

green = 11 #Pin Number RPi Board
red = 16 #Pin Number RPi Board

GPIO.setmode(GPIO.BOARD)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(red, GPIO.OUT)

n = 0
nmax = 30

while n != nmax:
  GPIO.output(green,GPIO.HIGH) #turn on green LED
  GPIO.output(red, GPIO.LOW) #turn off green LED
  bme280_data = bme280.sample(bus,address)
  humidity  = bme280_data.humidity
  pressure  = bme280_data.pressure
  ambient_temperature = bme280_data.temperature
  print(humidity, pressure, ambient_temperature)
  time.sleep(1.5)
  GPIO.output(green,GPIO.LOW) #turn on red LED
  GPIO.output(red, GPIO.HIGH) #turn off red LED
  time.sleep(0.5)
  n += 1
  
GPIO.cleanup()
