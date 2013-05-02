# Write a procedure download_time which takes as inputs a file size, the
# units that file size is given in, bandwidth and the units for
# bandwidth (excluding per second) and returns the time taken to download 
# the file.
# Your answer should be a string in the form
# "<number> hours, <number> minutes, <number> seconds"

# Some information you might find useful is the number of bits
# in kilobits (kb), kilobytes (kB), megabits (Mb), megabytes (MB),
# gigabits (Gb), gigabytes (GB) and terabits (Tb), terabytes (TB).

#print 2 ** 10      # one kilobit, kb
#print 2 ** 10 * 8  # one kilobyte, kB

#print 2 ** 20      # one megabit, Mb
#print 2 ** 20 * 8  # one megabyte, MB

#print 2 ** 30      # one gigabit, Gb
#print 2 ** 30 * 8  # one gigabyte, GB

#print 2 ** 40      # one terabit, Tb
#print 2 ** 40 * 8  # one terabyte, TB

# Often bandwidth is given in megabits (Mb) per second whereas file size 
# is given in megabytes (MB).
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

def download_time(filesize,ufile,speed,uspeed):
    if ufile[0]=='G':
        if ufile[1]=='B':
            time = filesize*2 ** 30 * 8
        else:
            time = filesize*2 ** 30
    elif ufile[0]=='T':
        if ufile[1]=='B':
            time = filesize*2 ** 40 * 8
        else:
            time = filesize*2 ** 40
    elif ufile[0]=='M':
        if ufile[1]=='B':
            time = filesize*2 ** 20 * 8
        else:
            time = filesize*2 ** 20
    else:
        if ufile[1]=='B':
            time = filesize*2 ** 10 * 8
        else:
            time = filesize*2 ** 10
    
    time *= 1.0
    
    if uspeed[0]=='G':
        if uspeed[1]=='B':
            time = time/(speed*2 ** 30 * 8)
        else:
            time = time/(speed*2 ** 30)
    elif uspeed[0]=='T':
        if uspeed[1]=='B':
            time = time/(speed*2 ** 40 * 8)
        else:
            time = time/(speed*2 ** 40)
    elif uspeed[0]=='M':
        if uspeed[1]=='B':
            time = time/(speed*2 ** 20 * 8)
        else:
            time = time/(speed*2 ** 20)
    else:
        if uspeed[1]=='B':
            time = time/(speed*2 ** 10 * 8)
        else:
            time = time/(speed*2 ** 10)
   
    return convert_seconds(time)
    

print download_time(1024,'kB', 1, 'MB')
#>>> 0 hours, 0 minutes, 1 second

print download_time(1024,'kB', 1, 'Mb')
#>>> 0 hours, 0 minutes, 8 seconds  # 8.0 seconds is also acceptable

print download_time(13,'GB', 5.6, 'MB')
#>>> 0 hours, 39 minutes, 37.1428571429 seconds

print download_time(13,'GB', 5.6, 'Mb')
#>>> 5 hours, 16 minutes, 57.1428571429 seconds

print download_time(10,'MB', 2, 'kB')
#>>> 1 hour, 25 minutes, 20 seconds  # 20.0 seconds is also acceptable

print download_time(10,'MB', 2, 'kb')
#>>> 11 hours, 22 minutes, 40 seconds  # 40.0 seconds is also acceptable


