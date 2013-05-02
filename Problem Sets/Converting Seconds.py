# Write a procedure, convert_seconds, which takes as input a non-negative 
# number of seconds and returns a string of the form 
# '<integer> hours, <integer> minutes, <number> seconds' but
# where if <integer> is 1 for the number of hours or minutes, 
# then it should be hour/minute. Further, <number> may be an integer
# or decimal, and if it is 1, then it should be followed by second.
# You might need to use int() to turn a decimal into a float depending
# on how you code this. int(3.0) gives 3

def convert_seconds(secs):
    hrs = int(secs/3600)
    secs = secs%3600
    mins = int(secs/60)
    secs= secs%60
    string = str(hrs)
    if hrs==1:
        string = string+" hour, "
    else:
        string = string+" hours, "
        
    string = string+str(mins)
    if mins==1:
        string = string+" minute, "
    else:
        string = string+" minutes, "
    
    string = string+str(secs)
    if secs==1:
        string = string+" second"
    else:
        string = string+" seconds"
    return string
    
print convert_seconds(3661)
#>>> 1 hour, 1 minute, 1 second

print convert_seconds(7325)
#>>> 2 hours, 2 minutes, 5 seconds

print convert_seconds(7261.7)
#>>> 2 hours, 1 minute, 1.7 seconds