# Importerer adafruit for at understøtte sensorens egenskaber. 
import Adafruit_DHT
import time
import RPi.GPIO as GPIO
# Socket bliver importeret for at konvertere vores beskeder fra TCP til UDP.
import socket
UDP_IP="192.168.6.151"
UDP_PORT = 7777
message = "Default"



sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

GPIO.setmode(GPIO.BCM) # referer til GPIO nummer i stedet for PIN nummer 
GPIO.setup(24, GPIO.IN) # Den pin vi gerne vil have data fra

# instancerer sensor til at understøtte Adafruits egenskaber. (aflæse temperatur og fugt)
sensor = Adafruit_DHT.DHT11 
		
while True:
# Temperatur og fugt bliver sat på sensor og pin 24. 
	humidity, temperature = Adafruit_DHT.read_retry(sensor, 24)
	if humidity is not None and temperature is not None:
	#temperatur og fugt udskrift når scriptet bliver kørt
		stringformat = 'Temp {0:0.1f} *C  Humidity {1:0.1f} %'.format(temperature, humidity) 
		print(stringformat)
		message = (stringformat)
		#Sender stringformat til modtager IP og PORT
		sock.sendto(bytes(message, 'UTF-8') , (UDP_IP, UDP_PORT))
	else:
		print('Failed to get reading. Try again!')
	

	
		
time.sleep(10)


