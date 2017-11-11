import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

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
	print("Avoiding obstacles")
		count=0
		while True:
		 i=0
		 avgDistance=0
		 for i in range(5):
		  GPIO.output(TRIG, False)                 #Set TRIG as LOW
		  time.sleep(0.1)                                   #Delay
		  GPIO.output(TRIG, True)                  #Set TRIG as HIGH
		  time.sleep(0.00001)                           #Delay of 0.00001 seconds
		  GPIO.output(TRIG, False)                 #Set TRIG as LOW
		  pulse_start = time.time()
		  pulse_end = time.time()
		  pulse_duration = pulse_end - pulse_start #time to get back the pulse to sensor
		  distance = pulse_duration * 17150        #Multiply pulse duration by 17150 (34300/2) to get distance
		  distance = round(distance,2)                 #Round to two decimal points
		  avgDistance=avgDistance+distance
		 avgDistance=avgDistance/5
		 print avgDistance
		 flag=0
		 if avgDistance < 15:      #Check whether the distance is within 15 cm range
		    count=count+1
		    motors.stop()
		    time.sleep(1)
		    motors.backward()
		    time.sleep(1.5)
		    if (count%3 ==1) & (flag==0):
		     motors.turnRight()
		     flag=1
		    else:
		     motors.turnLeft()
		     flag=0
		    time.sleep(1.5)
		    motors.stop()
		    time.sleep(1)
		 else:
		    motors.forward()
		    flag=0