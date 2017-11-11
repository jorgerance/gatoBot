from flask import Flask, render_template, request, redirect, url_for, make_response
import motors
import RPi.GPIO as GPIO
import socket

# Get server ip
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
server_ip = s.getsockname()[0]
s.close()

GPIO.setmode(GPIO.BOARD) 

app = Flask(__name__) 

@app.route('/')
def index():

	return render_template('index.html', server_ip=server_ip)

@app.route('/<changepin>', methods=['POST'])
def reroute(changepin):

	changePin = int(changepin) 

	if changePin == 1:
		motors.turnLeft()
	elif changePin == 2:
		motors.forward()
	elif changePin == 3:
		motors.turnRight()
	elif changePin == 4:
		motors.backward()
	elif changepin == 6:
		top()
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
		  while GPIO.input(ECHO)==0:              #Check whether the ECHO is LOW        
		  pulse_start = time.time()
		  while GPIO.input(ECHO)==1:              #Check whether the ECHO is HIGH
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
	else:
		motors.stop()

	response = make_response(redirect(url_for('index')))
	return(response)

app.run(debug=True, host='0.0.0.0', port=8000) 
