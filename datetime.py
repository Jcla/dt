import datetime,sys
t=datetime.datetime.now()
th=t.hour
print t.minute,"minutes past",t.hour,"o'clock"
#print "Please enter the hour to test:"
#th=int(sys.stdin.readline())
if th < 12:
  print "Morning"
elif th < 17:
  print "Afternoon"
elif th < 19:
  print "Evening"
else: 
  print "Night"
  