import random
import matplotlib.pyplot as plt
import numpy as np

def spinwheel():
	return(random.randrange(0,36,1))

def roulette(bet = None, betOn = None):
	landOn = spinwheel()
	if landOn == 0:
		return 0
	elif landOn % 2 == 0:
		if betOn == "e":
			return 2*bet
		else:
			return 0
	elif landOn % 2 == 1:
		if betOn == "e":
			return 0
		else:
			return 2*bet
	else:
		print "Huh?"

def playMartingale(wallet = None, minBet = 0.25, maxBet = 90, hardStop = 100):
	tries = 0
	totalPot = []
	totalPot.append(wallet)
	winnings = 1
	myBet = minBet
	while wallet > minBet and tries < hardStop:
		if winnings == 0:
			myBet = min(myBet*2, maxBet)
		else:
			myBet = minBet
		wallet = wallet - myBet
		winnings = roulette(myBet, betOn = "e")
		wallet = wallet + winnings
		totalPot.append(wallet)
		tries = tries + 1
	return totalPot

def visitsToCasino(n = 10, seedInt=12345):
	visit = {}
	netGain = {}
	random.seed(seedInt)
	for i in range(n):
		print("Visit %s out of %s" % (i, n))
		visit[i] = playMartingale(wallet = 127.75)
		netGain[i] = np.array(visit[i]) - 127.75
	return visit, netGain

def plotWallet(plotMe = []):
	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.plot(plotMe)
	plt.xlabel("Rounds")
	plt.ylabel("Net Gain ($)")
	plt.title("The Martingale Betting System")
	plt.show()

def histWallet(plotMe = [], numBins = 100):
	fig = plt.figure()
	ax = fig.add_subplot(111)
	n, bins, patches = plt.hist(plotMe, numBins, normed=True)
	plt.setp(patches, "facecolor", "g", linewidth=0.0)
	plt.xlabel("Net Gain ($)")
	plt.ylabel("Frequency")
	plt.title("Size of Pot")
	plt.show()