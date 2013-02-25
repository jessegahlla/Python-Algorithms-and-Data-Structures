import queue

def hotpotato(names = [], num = None):
	circleJerk = queue.queue()
	for name in names:
		circleJerk.enqueue(name)
	while circleJerk.size() > 1:
		for i in range(num):
			circleJerk.enqueue(circleJerk.dequeue())
		circleJerk.dequeue()
	return circleJerk.dequeue()