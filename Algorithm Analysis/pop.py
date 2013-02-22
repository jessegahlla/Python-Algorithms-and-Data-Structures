import timeit

popzero = timeit.Timer("x.pop(0)", "from __main__ import x")
popend = timeit.Timer("x.pop()", "from __main__ import x")

print("\tsize\tpop(0)\tpop()")
for i in range(1000000, 10000001, 1000000):
	x = list(range(i))
	pt = popend.timeit(number=1000)
	x = list(range(i))
	pz = popzero.timeit(number=1000)
	print("%s\t%15.5f\t%15.5f" % (len(range(i)),pz,pt))