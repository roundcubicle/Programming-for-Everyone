# create the variable(s) to hold user input
numlist=[]
l_num=None
s_num=None

def largest(number):
	#print numlist
	l_num=max(number)
	return l_num

def smallest(number):
	s_num=min(number)
	return s_num

#create an infinite loop for prompting the user to enter numbers-
while True:
	num=raw_input('Enter a valid number: ')
	if num == 'done':break
	
	#try / except to verify the user is entering a valid numbers
	try:
		num = int(num)
		numlist.append(num)
	except:
		print ('Invalid input')
if len(numlist) > 0:
		big = largest(numlist)
		small = smallest(numlist)
	
	
print 'Maximum is',big
print 'Minimum is',small
