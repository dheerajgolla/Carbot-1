import time 
import RPi.GPIO as GPIO
import multiprocessing
#import sys
#sys.path.insert(0, '/home/pi/Documents/tech/RpiMotorLib/RpiMotorLib')

optopin1=17
optopin2=18

from RpiMotorLib import rpi_dc_lib
GPIO.setmode(GPIO.BCM) 
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#MotorOne = rpi_dc_lib.DRV8833NmDc(26 ,19 ,50 ,True, "motor_one")

def motoronedrive(DC1):
	try: 
		MotorOne = rpi_dc_lib.DRV8833NmDc(26 ,19 ,50 ,False, "motor_one")
		#print("driving motor")
		MotorOne.forward(100-DC1)
		avgspeed = measurespeed(optopi88n1)
		#input("press key to stop") 
		#print("motor stop\n")
		#MotorOne.stop(0)
		time.sleep(spintime)
		#print(avgspeed)
	except KeyboardInterrupt:
    		print("CTRL-C: Terminating program.")
	except Exception as error:
    		print(error)
    		print("Unexpected error:")
	finally:
		MotorOne.cleanup(False)
	
def motortwodrive(DC2):
	try: 
		MotorTwo = rpi_dc_lib.DRV8833NmDc(13 ,21 ,50 ,False, "motor_two")
		#print("driving motor")
		MotorTwo.forward(100-DC2)
		avgspeed = measurespeed(optopin2)
		#input("press key to stop") 
		#print("motor stop\n")
		#MotorOne.stop(0)
		time.sleep(spintime)
		#print(avgspeed)
	except KeyboardInterrupt:
    		print("CTRL-C: Terminating program.")
	except Exception as error:
    		print(error)
    		print("Unexpected error:")
	finally:
		MotorTwo.cleanup(False)

# def motoronestop():
# 	try: 
# 		MotorOne = rpi_dc_lib.DRV8833NmDc(26 ,19 ,50 ,True, "motor_one")
# 		#print("driving motor")
# 		#MotorOne.forward(100-DC1)
# 		#avgspeed = measurespeed()
# 		#input("press key to stop") 
# 		#print("motor stop\n")
# 		MotorOne.stop(0)
# 		#time.sleep(spintime)
# 		print('motor 1 stopping')
# 	except KeyboardInterrupt:
#     		print("CTRL-C: Terminating program.")
# 	except Exception as error:
#     		print(error)
#     		print("Unexpected error:")
# 	finally:
# 		MotorOne.cleanup(False)

# def motortwostop()
# 	try: 
# 		MotorTwo = rpi_dc_lib.DRV8833NmDc(13 ,21 ,50 ,True, "motor_two")
# 		#print("driving motor")
# 		#MotorTwo.forward(100-DC2)
# 		#avgspeed = measurespeed()
# 		#input("press key to stop") 
# 		#print("motor stop\n")
# 		MotorTwo.stop(0)
# 		#time.sleep(spintime)
# 		print('motor 2 stopping')
# 	except KeyboardInterrupt:
#     		print("CTRL-C: Terminating program.")
# 	except Exception as error:
#     		print(error)
#     		print("Unexpected error:")
# 	finally:
# 		MotorTwo.cleanup(False)


def my_callback(channel):  
	global counter
	#print(counter)
	counter = counter + 1

def measurespeed(optopin):
	global counter
	counter = 0
	early = time.time()
	GPIO.add_event_detect(optopin, GPIO.FALLING, callback=my_callback, bouncetime=300)
	time.sleep(1)
	GPIO.remove_event_detect(optopin)
	speed = counter
	return speed

def stline():
	#process 1
	p1 = multiprocessing.Process(target=motoronedrive, args=(85, )) 
	p2 = multiprocessing.Process(target=motortwodrive, args=(85, ))
	p1.start()
	p2.start()

	#motoronedrive(85)
	#avgspeed1 = measurespeed(optopin1)
	#process 2
	#motortwodrive(85)
	#avgspeed2 = measurespeed(optopin2)

if __name__ == '__main__':
	stline()
