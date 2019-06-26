''' Write a program to read through the python1.txt and figure out the 
distribution by hour of the day for each of the messages. You can pull the hour out 
from the 'From ' line by finding the time and then splitting the string a second 
time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by
hour as shown below
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1
'''
a=list()
fname=input('Enter file name: ')
file1=open(fname)

counts=dict()
for line in file1:
    if line.startswith('From '):
        words=line.split()
        time=words[5]
        time1=time.split(':')
        hrs=time1[0]
        counts[hrs]=counts.get(hrs,0)+1

for k, v in list(counts.items()):
    a.append((k, v))    
a.sort()                             
for k, v in a:
    print(k, v)
