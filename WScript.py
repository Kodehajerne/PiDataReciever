import Adafruit_DHT
import time
import RPi.GPIO as GPIO
import socket
UDP_IP="192.168.3.197"
UDP_PORT = 7777
message = "Default"


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

GPIO.setmode(GPIO.BCM) # referer til GPIO nummer i stedet for PIN nummer 
GPIO.setup(24, GPIO.IN) # Den pin vi gerne vil have data fra

sensor = Adafruit_DHT.DHT11
		
while True:
	humidity, temperature = Adafruit_DHT.read_retry(sensor, 24)
	if humidity is not None and temperature is not None:
		print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
	else:
		print('Failed to get reading. Try again!')
	message = (str(temperature ) + (str(humidity)))
	sock.sendto(bytes(message, 'UTF-8') , (UDP_IP, UDP_PORT))

	
		
time.sleep(10)


