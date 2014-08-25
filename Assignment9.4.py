name = raw_input('Enter file:')
handle = open(name, 'r')

count = dict()

for line in handle:
    if not line.startswith("From:"):continue
    line = line.split()
    line = line[1]
    count[line] = count.get(line, 0) +1

bigcount = None
bigword = None
for word,count in count.items():
    if bigcount == None or count > bigcount:
        bigword = word 
        bigcount = count 

print bigword, bigcount
