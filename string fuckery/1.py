# -*- coding: utf-8 -*-
import re
import os
pliki=os.listdir('..\..\..\..\pulipt\mors')
l=0
noext=list()
veryshort=list()
DA=list()
chan=list()
booru=list()
twitter=list()
imgur=list()


unfiltered=list()
for name in pliki:
    #trim the file extension and store it in ext
    #only if the '.' is detected within the last 5(??) characters
    if name.rfind('.')==-1:
        noext.append(name)
        continue
    elif len(name)<=4:#if filename too short it goes into the trash
        veryshort.append(name)
        continue
    else:
        dotindex=name.rfind('.')
        ext=name[dotindex+1:]
        name=name[:dotindex+1]
    
    
    
    
    #filters below
    filtered=False
    z=re.search('[-][d][^.]{6}[.]',name)
    if ('_by_' in name) and z:
        DA.append(name)
        filtered=True
    z=re.search('[0-9]{12}',name)

    if z and len(name)>=13 and len(name)<=20:
        chan.append(name)
        filtered = True
    z=re.search('\d{5}[_]{2}',name)
    if z:
        booru.append(name)
        filtered=True
    z=re.search("[A-Z]+[a-zA-Z0-9-_]{13}",name)
    if z and len(name)==16:
        twitter.append(name)
        filtered=True
    if name[:-1].isalnum() and len(name)==8:
        imgur.append(name)
        filtered=True
    if not filtered:
        unfiltered.append(name)


    


#tests
print('all')
print (len(pliki))
#print(noext)
print('DA')
print(len(DA))
print('chan')
print(len(chan))
print('booru')
print(len(booru))
print('twitter')
print(len(twitter))
#print(twitter)
#print(veryshort)
print('imgur')
print(len(imgur))
print(imgur)
print('unfiltered')
print(len(unfiltered))


my_file = open("output.txt", "w")

for i in unfiltered:
    my_file.write(i+"      "+str(len(i))+"\n")
my_file.close()



"""
p = re.compile( ... )
m = p.match( 'string goes here' )
if m:
    print('Match found: ', m.group())
else:
    print('No match')
"""