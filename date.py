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

# why is there a list 'n' still..
# do not store anything but ONE previous value make it a variable not list
# try this method

# def breakText(line, breakCharacter):
#     i = 0
#     lastBreak = -1
#     while i < len(line):
#         if line[i] == breakCharacter:
#             print(line[lastBreak+1:i])
#             lastBreak = i
#         elif i == len(line) - 1:
#             print(line[lastBreak+1:])
#         i += 1

# text = 'this is a test string.. just to see if this works'
# breakText(text, ' ')

# you should be able to use this method and get the same result
# try breakText(date, '/')