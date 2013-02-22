import timeit
import random

for i in range(10000, 1000001, 20000):
	t1 = timeit.Timer("del x[random.randrange(%d)]" % i, "from __main__ import random, x")
	x = list(range(i))
	del_list_time = t1.timeit(number=1000)
	print("%d, %10.3f" % (i, del_list_time))