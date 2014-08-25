fname = raw_input("Enter file name: ")
if len(fname) == 0:
    fname = 'romeo.txt'
fh = open(fname)
lst = list()
for line in fh:
    lst = lst + line.split()
#print lst  
lst.sort()
#print lst
lst2=[]
for word in lst:
	if word not in lst2:
		lst2.append(word)
print lst2
