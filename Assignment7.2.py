# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
count = 0 
sum = 0
for line in fh:
	if not line.startswith("X-DSPAM-Confidence:"):continue
	#print line
	pos = line.find(" ")
	#print pos
	val= line[pos:].rstrip()
	val = float(val)
	count = count +1
	sum =  sum + val
	#print val
#print sum
	#print val
	
print 'Average spam confidence:', sum/count
