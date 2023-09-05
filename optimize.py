#!/usr/bin/python3 

################################
# Optimize TicTacToe by avoiding unnessessary calls to the server.
# This removes the href targets from all fields that already contain a symbol.
# This scrtipt requires the TicTacToe index.html file to be preformatted (look in preformatted.html for an example.)
################################

with open("preformatted.html") as tictactoeFile:
    lines = tictactoeFile.readlines()
    tictactoeFile.close()

optimizedLines = []

for line in lines:
    if "class=\"tictactoe-X\">X</a>" in line or "class=\"tictactoe-O\">O</a>" in line:
        optimizedLines.append(line[:line.rfind("href")] + line[line.rfind("class"):])
    else:
        optimizedLines.append(line)
    
with open("index.html", 'w') as optimizedFile:
    for line in optimizedLines:
        optimizedFile.write(line)
    optimizedFile.close()