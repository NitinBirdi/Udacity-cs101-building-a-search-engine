# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#
def isLeapYear(year):
    return year

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    yy=1
    yyn=0
    mm = [0,31,59,90,120,151,181,212,243,273,304,334,365]
    mon =[0,31,28,31,30,31,30,31,31,30,31,30,31]
    days=0
    
    i = month1
    while(i<month2):
        days=days+mon[i]
        i=i+1
    
    days=days-day1+day2
    
    if(year2-year1>1 or (year2>=year1-1 and month2>2)):
        days = days+(int)(((year2*1.0)-(year1*1.0))*(365.25))
        if(month1<=2 and year1%4==0):
            if(year1%100==0):
                if(year1%400==0):
                    days=days+1
            else:
               days=days+1
        else:
            if(month2>2 and year2%4==0):
            
                if(year2%100==0):
                    if(year2%400==0):
                        days=days+1
                else:
                   days=days+1
     
    return days   


# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()
