name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

count=dict()
lst=list()

for line in handle:
    if not line.startswith("From "):
	    continue
    line=line.strip()
    pos=line.find(":")
    time=line[pos-2:pos]
    count[time]=count.get(time,0)+1
	#print line
    #print pos
    #print time
#print count
lst=count.keys()
lst.sort()
#print lst
for key in lst:
    print key, count[key]
'''
for key,val in count.items():
    lst.append((key,val))
lst.sort()

for key,val in lst:
   print key, val
'''
