import multiprocessing
import time
import matplotlib.pyplot as plt
import random
a=[]
def fuuc(a,q):
	for i in range(1,5):
		time.sleep(1)
		j = random.gauss(4,2)
		a = a + [i]
	q.put(a)

if __name__ == '__main__':
	q1 = multiprocessing.Queue()
	p1 = multiprocessing.Process(target = fuuc, args = (a,q1))
	q2 = multiprocessing.Queue()
	p2 = multiprocessing.Process(target = fuuc, args = (a*2,q2))
	p1.start()
	p2.start()
	print("before join")
	# p1.join()
	# p2.join()
	a1 = q1.get()
	a2 = q2.get()
	print(a1, a2)
	print('after join')
	print(a1, a2)
	# plt.hist(a1, 50)
	# plt.hist(a2, 50)
	# plt.show()