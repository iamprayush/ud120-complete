#!/usr/bin/python

def outlierCleaner(predictions, ages, net_worths):
	"""
	    Clean away the 10% of points that have the largest
	    residual errors (difference between the prediction
	    and the actual net worth).

	    Return a list of tuples named cleaned_data where
	    each tuple is of the form (age, net_worth, error).
	"""

	cleaned_data = []

    ### your code goes here
	# ages1 = [i[0] for i in ages]
	# predictions1 = [i[0] for i in predictions]
	# net_worths1 = [i[0] for i in net_worths]

	errors = [(i-j)**2 for i,j in zip(predictions, net_worths)]
	#errors1 = [(i-j)**2 for i,j in zip(predictions, net_worths)]
	for i in range(9):
		errors[errors.index(max(errors))] = -1

	for i in range(len(errors)):
		if errors[i] > 0:
			cleaned_data.append((ages[i], net_worths[i], errors[i]))

	print(cleaned_data)
	# print('ages :')
	# print(ages1)
	# print('\n\n')
	# print('pred : \n')
	# print(predictions1)
	# print('\n\n')
	# print('net_worth : \n')
	# print(net_worths1)

	return cleaned_data
