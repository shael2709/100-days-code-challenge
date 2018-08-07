def cmpnd_intst(principle, rate, time): 
	CI = principle * (pow((1 + rate / 100), time))
	print("Compound interest is", CI)

cmpnd_intst(10000, 10.25, 5)
