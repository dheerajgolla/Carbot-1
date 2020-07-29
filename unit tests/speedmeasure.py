import RPi.GPIO as GPIO  
import time
GPIO.setmode(GPIO.BCM)  
# GPIO 23 & 17 set up as inputs, pulled up to avoid false detection.  
# So we'll be setting up falling edge detection for both 
#GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
def my_callback(channel):  
	global counter
	print counter
	counter = counter + 1

#def my_callback2(channel):  
#    print "falling edge detected on 23"  
counter = 0
# when a falling edge is detected on port 17, regardless of whatever   
# else is happening in the program, the function my_callback will be run
# 'bouncetime=300' includes the bounce control written into interrupts2a.py
early = time.time()
#while (time.time() - now) < 10000: 
GPIO.add_event_detect(17, GPIO.FALLING, callback=my_callback, bouncetime=300)
# when a falling edge is detected on port 23, regardless of whatever   
# else is happening in the program, the function my_callback2 will be run  
# 'bouncetime=300' includes the bounce control written into interrupts2a.py  
#GPIO.add_event_detect(23, GPIO.FALLING, callback=my_callback2, bouncetime=300)
if (time.time() - now) >= 10:
	GPIO.remove_event_detect(17)
	
speed = counter/10
print speed
