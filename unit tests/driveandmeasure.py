import time 
import RPi.GPIO as GPIO
#import sys
#sys.path.insert(0, '/home/pi/Documents/tech/RpiMotorLib/RpiMotorLib')


from RpiMotorLib import rpi_dc_lib
GPIO.setmode(GPIO.BCM) 
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#MotorOne = rpi_dc_lib.DRV8833NmDc(26 ,19 ,50 ,True, "motor_one")

def motordrive():
	try: 
		MotorOne = rpi_dc_lib.DRV8833NmDc(26 ,19 ,50 ,True, "motor_one")
		print("driving motor")
		MotorOne.forward(15)
		avgspeed = measurespeed()
		input("press key to stop") 
		print("motor stop\n")
		MotorOne.stop(0)
		#time.sleep(3)
		print(avgspeed)
	except KeyboardInterrupt:
    		print("CTRL-C: Terminating program.")
	except Exception as error:
    		print(error)
    		print("Unexpected error:")
	finally:
		MotorOne.cleanup(False)
	

def my_callback(channel):  
	global counter
	#print(counter)
	counter = counter + 1

def measurespeed():
	global counter
	counter = 0
	early = time.time()
	GPIO.add_event_detect(17, GPIO.FALLING, callback=my_callback, bouncetime=300)
	time.sleep(10)
	GPIO.remove_event_detect(17)
	speed = counter/10
	return speed

motordrive()
avgspeed = measurespeed()
input("press key to stop") 
motorstop()
print(avgspeed)



