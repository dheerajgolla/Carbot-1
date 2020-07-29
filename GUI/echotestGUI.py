import tkinter as tk
# import RPi.GPIO as GPIO
# import time
# triggerpin = 12
# echopin = 5

# GPIO.setmode(GPIO.BCM)

# GPIO.setup(triggerpin, GPIO.OUT,pull_up_down=GPIO.PUD_DOWN)
# GPIO.setup(triggerpin, GPIO.OUT,pull_up_down=GPIO.PUD_DOWN)

def singleecho():
	GPIO.output(triggerpin, GPIO.LOW)
	time.sleep(0.000002)
	GPIO.output(triggerpin, GPIO.HIGH)
	time.sleep(0.000010)
	GPIO.output(triggerpin, GPIO.LOW)
	#GPIO.add_event_detect(echopin, GPIO.RISING, callback=echo_callback, bouncetime=3)
	GPIO.wait_for_edge(echopin, GPIO.RISING, timeout= 25) #timeout in millisecs
	if GPIO.input(echopin) is True:
		tic = time.time()
		GPIO.wait_for_edge(echopin, GPIO.FALLING, timeout= 25)
		duration = time.time() - tic
		distcm = (duration/58)*1000000
		distance.set(distcm)


def echoloop():
	GPIO.output(triggerpin, GPIO.LOW)
	time.sleep(0.000002)
	GPIO.output(triggerpin, GPIO.HIGH)
	time.sleep(0.000010)
	GPIO.output(triggerpin, GPIO.LOW)
	#GPIO.add_event_detect(echopin, GPIO.RISING, callback=echo_callback, bouncetime=3)
	while loop == True:
		GPIO.wait_for_edge(echopin, GPIO.RISING, timeout= 25) #timeout in millisecs
		if GPIO.input(echopin) is True:
			tic = time.time()
			GPIO.wait_for_edge(echopin, GPIO.FALLING, timeout= 25)
			duration = time.time() - tic
			distcm = (duration/58)*1000000
			distance.set(distcm)
		while time.time()-toc < 0.06:
			time.sleep(0.005)

def stoploop:
	loop = 0


def echoloop():
	distance.configure(text = 'this')

# def echo_callback():


def singleecho():
	distance.configure(text = 'that')

window = tk.Tk()
window.title('echo locator')

window.columnconfigure([0, 1, 2], minsize=250)
window.rowconfigure([0, 1, 2], minsize=100)
window.resizable(width=False, height=False)
distlabel = tk.Label(text="distance:")
distlabel.grid(row=0, column = 1)
#distance = tk.Label(text = '')
#distance.grid(row=0, column = 2)
dist=tk.Label(master, text="", textvariable=distance).grid(row=0,column=2, sticky=W)
ebut = tk.Button(text = "start single echo", command = singleecho, width = 20)
ebut.grid(row=0, column = 0)
loopbut = tk.Button(text = "start echo loop", command = echoloop, width = 20)
loopbut.grid(row=1, column = 0)
window.mainloop()
