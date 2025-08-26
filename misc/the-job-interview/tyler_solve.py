import urllib.request
from parsel import Selector
import numpy

# Set the target URL
url = 'https://docs.google.com/document/d/e/2PACX-1vRW7X8yMO9cM-b6Ao3FbiZysF3MIjARoeO73z0PlG8O_yeM8xxWAWzt9hdoavlh3HR1IOEwWtJFpczI/pub'

# Send the request and get the HTML content from the google doc
req = urllib.request.Request(url=url)
f = urllib.request.urlopen(req)
html = f.read().decode('utf-8')

# Create Parsel selector and selected HTML elements that have either the table or tr tag
sel = Selector(text=html)
rows = sel.css('table tr')

# Parse table data
table = []
for row in rows:    
    cells = row.css('span::text').getall() # ::text doesn't exist in css but is how parsel knows to take only the content
    if len(cells) >= 3:
        table.append([cell.strip() for cell in cells])

# Removing header
del table[0]

# Find the highest x and y coordinate - probably didn't need to do it this way, but was part of the original script
# index 0 refers to the x coord and index 2 is the y coord
maxX = 0
maxY = 0
for i in range(len(table)):
    if int(table[i][0]) > maxX:
        maxX = int(table[i][0])
    if int(table[i][2]) > maxY:
        maxY = int(table[i][2])


# Initialize array - This creates an array at the size we need
# We populate it with - which is actually not needed, we remove them in the next step
arr = [["-" for _ in range(maxX + 1)] for _ in range(maxY + 1)]

# We loop over every entry in our table, grab the x and y value and insert our character at those coordinates
for row in table:
    x = int(row[0])
    y = int(row[2])
    arr[y][x] = row[1]

# Convert our array to a numpy array, I'm not sure this is needed but a hold over from the original solve script
np_arr = numpy.array(arr)
print(np_arr)

# I convert the array into a string as I will save it to a file
result = ''
for row in np_arr:
    for item in row:
        if item != "-":
            result += item
        else:
            result += ' '

    result += '\n'

# Save the string to a file
file = open('output.txt', 'w')
file.writelines(result)
file.close()