import tkinter as tk
import pdb

def addfunc():
	num1 = ent1.get()
	numm1 = float(num1)
	num2 = ent2.get()
	#pdb.set_trace()
	print(type(num1))
	numm2=float(num2)
	res = numm1+numm2
	#value = (greeting["text"])
	greeting.configure(text = res)
	#greeting["text"] = f"{res}"

window = tk.Tk()
window.title("addition machine")
greeting = tk.Label(text="carbot1 control center")
ent1 = tk.Entry(window)
ent2 = tk.Entry(window)
#greeting.pack()
ent1.pack()
ent2.pack()
add = tk.Button(text = "click to add", command = addfunc)
#add.bind("<Button-1", addfunc())
add.pack()
greeting["text"] = f"ans"
greeting.pack()
window.mainloop()
