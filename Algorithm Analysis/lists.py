import random
import timeit

def test1():
	l = []
	for i in range(1000):
		l = l + [i]

def test2():
	l = []
	for i in range(1000):
		l.append(l)

def test3():
	l = [i for i in range(1000)]
	
def test4():
	l = list(range(1000))

for i in range(10000,1000001,20000):
	t = timeit.Timer("x.index(random.randrange(%d))" % i, "from __main__ import random, x")
	x = list(range(i))
	i_time = t.timeit(number=1000)
	print("%d,%10.3f" % (i, i_time))

'''t1 = Timer("test1()", "from __main__ import test1")
print("concat ", t1.timeit(number=1000), "milliseconds")
t2 = Timer("test2()", "from __main__ import test2")
print("append ", t1.timeit(number=1000), "milliseconds")
t3 = Timer("test3()", "from __main__ import test3")
print("comprehension ", t1.timeit(number=1000), "milliseconds")
t4 = Timer("test4()", "from __main__ import test4")
print("list range ", t1.timeit(number=1000), "milliseconds")'''