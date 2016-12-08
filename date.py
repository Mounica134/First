print "please enter the date in date-month-year format.use only - or / to separate"
d = raw_input()
n = []
for i in range(len(d)):
    if d[i]=='-' or d[i]=='/':
        n.append(i)
        if len(n)<2:
            if n[0]>0:
                print int(d[0:n[0]]),
        else:
            while len(n)>2:
                n.remove(n[len(n)-3])
            if n[1]-n[0]>1:
                print int(d[n[0]+1:n[1]]),
print int(d[n[1]+1:len(d)])
#dont store all the positions of the separating characters it is a waste of memory
# only store the previous one and update it each time
