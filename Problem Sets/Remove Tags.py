# Question 4: Remove Tags

# When we add our words to the index, we don't really want to include
# html tags such as <body>, <head>, <table>, <a href="..."> and so on.

# Write a procedure, remove_tags, that takes as input a string and returns
# a list of words, in order, with the tags removed. Tags are defined to be
# strings surrounded by < >. Words are separated by whitespace or tags. 
# You may assume the input does not include any unclosed tags, that is,  
# there will be no '<' without a following '>'.

def remove_tags(string):
    l = []
    temp=""
    j=len(string)
    i=0
    while j>0:
        if (string[i]==' ' and (not string[i]=='\n') and (not (temp.strip())=='' )):
            l.append(temp.strip())
            temp=""
        elif string[i] == '<':
            while(1):
                i+=1
                j-=1
                if(string[i]=='>'):
                    break
            if not (temp.strip())=='':
                l.append(temp)
                temp=""
        else:
             if((not string[i]=='\n') and (not (string[i]==' ' or string[i]==''))):
                 temp+=string[i]
                    
        i+=1
        j-=1
    if not temp=="":
        l.append(temp)
    return l

print remove_tags('''<h1>Title</h1><p>This is a
                    <a href="http://www.udacity.com">link</a>.<p>''')
#>>> ['Title','This','is','a','link','.']

print remove_tags('''<table cellpadding='3'>
                     <tr><td>Hello</td><td>World!</td></tr>
                     </table>''')
#>>> ['Hello','World!']

print remove_tags("<hello><goodbye>")
#>>> []

print remove_tags("This is plain text.")
#>>> ['This', 'is', 'plain', 'text.']