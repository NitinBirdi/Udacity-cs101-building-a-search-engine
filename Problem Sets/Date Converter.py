# Question 5: Date Converter

# Write a procedure date_converter which takes two inputs. The first is 
# a dictionary and the second a string. The string is a valid date in 
# the format month/day/year. The procedure should return
# the date written in the form <day> <name of month> <year>.
# For example , if the
# dictionary is in English,

english = {1:"January", 2:"February", 3:"March", 4:"April", 5:"May", 
6:"June", 7:"July", 8:"August", 9:"September",10:"October", 
11:"November", 12:"December"}

# then  "5/11/2012" should be converted to "11 May 2012". 
# If the dictionary is in Swedish

swedish = {1:"januari", 2:"februari", 3:"mars", 4:"april", 5:"maj", 
6:"juni", 7:"juli", 8:"augusti", 9:"september",10:"oktober", 
11:"november", 12:"december"}

# then "5/11/2012" should be converted to "11 maj 2012".

# Hint: int('12') converts the string '12' to the integer 12.

def date_converter(lang, date):
    month = date[:date.find('/')]
    date = date[date.find('/')+1:]
    day = date[:date.find('/')]
    date = date[date.find('/')+1:]
    
    return (day+" "+lang[int(month)]+" "+date)
   

print date_converter(english, '5/11/2012')
#>>> 11 May 2012

print date_converter(english, '5/11/12')
#>>> 11 May 12

print date_converter(swedish, '5/11/2012')
#>>> 11 maj 2012

print date_converter(swedish, '12/5/1791')
#>>> 5 december 1791
