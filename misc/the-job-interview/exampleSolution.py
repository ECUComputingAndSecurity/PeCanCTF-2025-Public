import urllib.request
from pprint import pprint
from html_table_parser.parser import HTMLTableParser
import numpy

url = 'https://docs.google.com/document/d/e/2PACX-1vRW7X8yMO9cM-b6Ao3FbiZysF3MIjARoeO73z0PlG8O_yeM8xxWAWzt9hdoavlh3HR1IOEwWtJFpczI/pub'

#Get xHTML
req = urllib.request.Request(url=url)
f = urllib.request.urlopen(req)
xhtml = f.read()

#Parse the table from xHTML
p = HTMLTableParser()
p.feed(str(xhtml))
table = p.tables[0]
del table[0]

#Find the highest x and y coordinate and save them in an array
maxX = 0
maxY = 0
for i in range(len(table)):
    if int(table[i][0]) > maxX:
        maxX = int(table[i][0])  
    if int(table[i][2]) > maxY:
        maxY = int(table[i][2])

#Initialise an array the size of the highest x and y coordinate
arr = [["-" for _ in range(maxX+1)] for _ in range(maxY+1)]

#Insert unicode string into the respective coordinate
for a in table:
    x = int(a[0])
    y = int(a[2])
    arr[y][x] = a[1]

#Flip array on the x axis as 0,0 on the HTMLTableParser is from the bottom right not top right
arr = numpy.array(arr)


#decode and print each item in the array
for i in arr:
    for j in i:
        if j != "-":
            print(bytes.fromhex(j.replace("\\x", "")).decode("utf-8"), end="")
        else:
            print(" ", end="")
    print()