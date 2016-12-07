print "please enter the date in date-month-year format.use only - or / to separate"
d = raw_input()
n = []
for i in range(len(d)):
    if d[i]=='-' or d[i]=='/':
        n.append(i)
date = int(d[0:n[0]])
month = int(d[n[0]+1:n[1]])
year = int(d[n[1]+1:len(d)+1])
print date, "th day of", month,"th month in the year", year
