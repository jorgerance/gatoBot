import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
import time

Motor1A = 16 
Motor1B = 18
Motor2A = 11
Motor2B = 15

sleep_t = 0.2

sr04_trig = 36
sr04_echo = 35

GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(sr04_trig,GPIO.OUT)
GPIO.setup(sr04_echo,GPIO.IN)
GPIO.output(sr04_trig, False)


def backward():
	GPIO.output(Motor1A,GPIO.HIGH)
	GPIO.output(Motor1B,GPIO.LOW)
	GPIO.output(Motor2A,GPIO.HIGH)
	GPIO.output(Motor2B,GPIO.LOW)

def forward():
	GPIO.output(Motor1A,GPIO.LOW)
	GPIO.output(Motor1B,GPIO.HIGH)
	GPIO.output(Motor2A,GPIO.LOW)
	GPIO.output(Motor2B,GPIO.HIGH)

def turnLeft():
	print("Going Left")
	GPIO.output(Motor1A,GPIO.HIGH)
	GPIO.output(Motor1B,GPIO.LOW)
	GPIO.output(Motor2A,GPIO.LOW)
	GPIO.output(Motor2B,GPIO.HIGH)

def turnRight():
	print("Going Right")
	GPIO.output(Motor1A,GPIO.LOW)
	GPIO.output(Motor1B,GPIO.HIGH)
	GPIO.output(Motor2A,GPIO.HIGH)
	GPIO.output(Motor2B,GPIO.LOW)

def stop():
	print("Stopping")
	GPIO.output(Motor1A,GPIO.LOW)
	GPIO.output(Motor1B,GPIO.LOW)
	GPIO.output(Motor2A,GPIO.LOW)
	GPIO.output(Motor2B,GPIO.LOW)

def objectavoidance():
  print "Ultrasonic Measurement"

  GPIO.output(sr04_trig, False)

  def measure():
    time.sleep(0.333)
    GPIO.output(sr04_trig, True)
    time.sleep(0.00001)
    GPIO.output(sr04_trig, False)
    start = time.time()
    
    while GPIO.input(sr04_echo)==0:
      start = time.time()

    while GPIO.input(sr04_echo)==1:
      stop = time.time()

    elapsed = stop-start
    distance = (elapsed * 34300)/2

    return distance

    while True:

      distance = measure()
      print "Distance : %.1f" % distance
      time.sleep(.5)


      if distance >= 10:
       forward()
      else:
       turnRight()
