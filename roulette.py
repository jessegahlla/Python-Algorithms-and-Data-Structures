import random

random.seed(12345)

def spinwheel():
	return(random.randrange(0,36,1))

def roulette(bet = None, betOn = None):
	landOn = spinwheel()
	print("Landed on: %s" % landOn)
	if landOn == 0:
		return 0
	elif landOn % 2 == 0:
		if betOn == "e":
			print("\tYou bet even, you won!")
			return 2*bet
		else:
			print("\tYou lost.")
			return 0
	elif landOn % 2 == 1:
		if betOn == "e":
			print("\tYou lost.")
			return 0
		else:
			print("\tYou bet odd, you win!")
			return 2*bet
	else:
		print "Huh?"

def playMartingale(wallet = None, minBet = 0.25, maxBet = 90, hardStop = 10):
	tries = 0
	totalPot = []
	totalPot.append(wallet)
	winnings = 1
	myBet = minBet
	while wallet > minBet:
		if winnings == 0:
			myBet = min(myBet*2, maxBet)
			if myBet == maxBet:
				print("MAX BET")
		else:
			myBet = minBet
		wallet = wallet - myBet
		print("Betting %s" % myBet)
		winnings = roulette(myBet, betOn = "e")
		wallet = wallet + winnings
		totalPot.append(wallet)
		print("Wallet is now %f" % wallet)
		tries = tries + 1
	print("Broke at %s tries" % tries)
	return totalPot