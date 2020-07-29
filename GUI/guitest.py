import tkinter as tk

def forwardfunc():
	print("forward")

def backwardfunc():
	print("backward")

def rightfunc():
	print("right")

def leftfunc():
	print("left")

def stopfunc():
	print("stop")

window = tk.Tk()
window.title('carbot1 remote')
window.columnconfigure([0, 1, 2], minsize=250)
window.rowconfigure([0, 1, 2], minsize=100)
window.resizable(width=False, height=False)

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