from flask import Flask, render_template, request, redirect, url_for, make_response
import motors
import RPi.GPIO as GPIO
import socket

# Get server ip
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
server_ip = s.getsockname()[0]
s.close()

GPIO.setmode(GPIO.BOARD) #set up GPIO

app = Flask(__name__) #set up flask server

@app.route('/')
def index():

	return render_template('index.html', server_ip=server_ip)

@app.route('/<changepin>', methods=['POST'])
def reroute(changepin):

	changePin = int(changepin) #cast changepin to an int

	if changePin == 1:
		motors.turnLeft()
	elif changePin == 2:
		motors.forward()
	elif changePin == 3:
		motors.turnRight()
	elif changePin == 4:
		motors.backward()
	else:
		motors.stop()

	response = make_response(redirect(url_for('index')))
	return(response)

app.run(debug=True, host='0.0.0.0', port=8000) #set up the server in debug mode to the port 8000
