import tkinter as tk
import time 
import RPi.GPIO as GPIO
import multiprocessing
import matplotlib.pyplot as plt
import numpy as np
#import sys
#sys.path.insert(0, '/home/pi/carbot1/RpiMotorLib27/RpiMotorLib')
#fb=False
#fb=True
optopin1=17
optopin2=18
spintime = 6
measuretime = 0.2
k=1
setspeed = 10
#speedlistM1 = []
#speedlistM2 = []

from RpiMotorLib import rpi_dc_lib
GPIO.setmode(GPIO.BCM) 
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def motordrive(motpin1, motpin2, optopin, DC, q):
    try: 
        Motor = rpi_dc_lib.DRV8833NmDc(motpin1 ,motpin2 ,50)
        #print("driving motor")
        speedlist = []
        Motor.forward(100-DC)
#        if fwd==1:
#            Motor.forward(100-DC)
#        elif 
        #print("motor two with feedback started\n")
        avgspeed = measurespeed(optopin)
        now = time.time()
        while (time.time() - now) < spintime:
                    avgspeed = measurespeed(optopin)
                    speedlist = speedlist + [avgspeed]
                    #print("M2 speed = " + str(avgspeed))
                    if fb == True and abs(avgspeed - setspeed) > 1 and DC + k*(setspeed - avgspeed) < 99:
                        DC = DC + k*(setspeed - avgspeed)
                        Motor.forward(100-DC)
        #input("press key to stop") 
        #print("motor stop\n")
        Motor.stop(0)
        #time.sleep(spintime)
        #print("M2 speed = " + str(avgspeed))
    except KeyboardInterrupt:
            print("CTRL-C: Terminating program.")
    except Exception as error:
            print(error)
            print("Unexpected error:")
    finally:
        Motor.cleanup(True)
        q.put(speedlist)
def my_callback(channel):  
    global counter
    counter = counter + 1

def measurespeed(optopin):
    global counter
    counter = 0
    GPIO.add_event_detect(optopin, GPIO.FALLING, callback=my_callback, bouncetime=3) #bouncetime in milliseconds
    time.sleep(measuretime)
    GPIO.remove_event_detect(optopin)
    speed = counter
    return speed

def forwardfunc():
    print("forward")
    q1 = multiprocessing.Queue()
    q2 = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=motordrive, args=(26,19, optopin1, 50,q1))
    p2 = multiprocessing.Process(target=motordrive, args=(13,21, optopin2, 50,q2))
    p2.start()
    p1.start()
    #p1.join()
    #p2.join()
    M2speedlist = q2.get()
    M1speedlist = q1.get()
    #p2.join()
    #histplt,ax_spd = plt.subplots()
    #plt.hist(M1speedlist, label = 'M1 feedback to 100')
    #plt.hist(M2speedlist, label = 'M2 feedback to 100')
    #plt.legend(loc = 'upper right')
    #speedplt,ax2_spd = plt.subplots()
    p1.join()
    p2.join()
    M1speedlistar = np.array(M1speedlist)
    M2speedlistar = np.array(M2speedlist)
    diff = M1speedlistar-M2speedlistar
    print(diff)
    print(M1speedlist)
    print(M2speedlist)
    plt.figure()
    plt.plot(diff,label = 'diff no feedback')
    #plt.plot(M1speedlist,label = 'M1 feedback to 100')
    #plt.plot(M2speedlist,label = 'M2 feedback to 100')
    #plt.legend(loc = 'upper right')
    plt.show(block=False)

def backwardfunc():
    print("backward")
    q1 = multiprocessing.Queue()
    q2 = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=motordrive, args=(19,26, optopin1, 50,q1))
    p2 = multiprocessing.Process(target=motordrive, args=(21,13, optopin2, 50,q2))
    p2.start()
    p1.start()
    #p1.join()
    #p2.join()
    M2speedlist = q2.get()
    M1speedlist = q1.get()
    #p2.join()
    #histplt,ax_spd = plt.subplots()
    #plt.hist(M1speedlist, label = 'M1 feedback to 100')
    #plt.hist(M2speedlist, label = 'M2 feedback to 100')
    #plt.legend(loc = 'upper right')
    #speedplt,ax2_spd = plt.subplots()
    p1.join()
    p2.join()
    M1speedlistar = np.array(M1speedlist)
    M2speedlistar = np.array(M2speedlist)
    diff = M1speedlistar-M2speedlistar
    print(diff)
    print(M1speedlist)
    print(M2speedlist)
    plt.figure()
    plt.plot(diff,label = 'diff no feedback')
    #plt.plot(M1speedlist,label = 'M1 feedback to 100')
    #plt.plot(M2speedlist,label = 'M2 feedback to 100')
    #plt.legend(loc = 'upper right')
    plt.show(block=False)

def rightfunc():
    print("right")

def leftfunc():
    print("left")

def stopfunc():
    print("stop")
    MotorOne = rpi_dc_lib.DRV8833NmDc(26 ,19 ,50 ,False, "motor_one")
    MotorOne.stop(0)
    MotorTwo = rpi_dc_lib.DRV8833NmDc(13 ,21 ,50 ,False, "motor_two")
    MotorTwo.stop(0)

window = tk.Tk()
window.title('carbot1 remote')
window.columnconfigure([0, 1, 2], minsize=250)
window.rowconfigure([0, 1, 2], minsize=100)
window.resizable(width=False, height=False)

fb = tk.IntVar()
fbbut = tk.Checkbutton(window, text = "Feedback", var=fb)
fbbut.grid(row=0, column = 2)

fbut = tk.Button(text = "Fwd", command = forwardfunc, width = 10)
fbut.grid(row=0, column =1)

bbut = tk.Button(text = "Back", command = backwardfunc, width = 10)
bbut.grid(row=2, column =1)

rbut = tk.Button(text = "Right", command = rightfunc, width = 10)
rbut.grid(row=1, column =2)

lbut = tk.Button(text = "Left", command = leftfunc, width = 10)
lbut.grid(row=1, column =0)

stp = tk.Button(text = "Stop", command = stopfunc, width = 10)
stp.grid(row=1, column =1)


window.mainloop()
