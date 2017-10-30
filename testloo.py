import time

def simulate(function_name,number_simulations):
	time_began = time.time()
	i = 0
	while i < number_simulations:
		i += 1
		function_name()
	time_completed = time.time()
	return time_completed-time_began

def tester():
	return 1

myFunctionTime = simulate(tester,10000000)

print(myFunctionTime) # this prints how many times it took to run the "tester" function 10,000,000 times
