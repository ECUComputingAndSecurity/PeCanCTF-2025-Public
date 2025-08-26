A published google doc url,
<https://docs.google.com/document/d/e/2PACX-1vRW7X8yMO9cM-b6Ao3FbiZysF3MIjARoeO73z0PlG8O_yeM8xxWAWzt9hdoavlh3HR1IOEwWtJFpczI/pub>,  is provided containing a 3 column table (x-cord, character, and y-cord).
The challenge is to reconstruct the flag based on the grid, placing the character in the relevant cords.

This is either done by copying the grid from the doc and reading the file or web scraping.
Then an array needs to be defined based on the highest x and y cords to define the array. The grid can then be looped over and characters inserted into the relevant positions before printing in a terminal.
Example code for the solution has been provided. 
Note:  The terminal will need to be zoomed out due to the size of the output.


# Tyler's update
The core challenge is to scrape the content of the given URL and create a display using the data.
The URL leads to a google doc which has a list of coords and characters for each coordinate.
If you lay out the characters positioned by the coordinates it will draw the flag.

The flag will be written out in the terminal, you can alternatively write to a file.
The characters should be kept as is, there's no need to modify them.
The original solve script uses a parser that I couldn't find, I used parsel to replicate the solve.