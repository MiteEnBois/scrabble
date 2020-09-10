cases = {
    "TWS": ["0,0", "0,7", "0,14", "7,0", "7,14", "14,0", "14,7", "14,14"],
    "tls": ["1,5", "1,9", "5,1", "5,5", "5,9", "5,13", "9,1", "9,5", "9,9", "9,13", "13,5", "13,9"],
    "DWS": ["1,1", "1,13", "2,2", "2,12", "3,3", "3,11", "4,4", "4,10", "7,7", "10,10", "10,4", "11,11", "11,3", "12,12",
            "12,2", "13,13", "13,1"],
    "dls": ["0,3", "0,11", "2,6", "2,8", "3,0", "3,7", "3,14", "6,2", "6,6", "6,8", "6,12", "7,3", "7,11", "8,2", "8,6",
            "8,8", "8,12", "11,0", "11,7", "11,14", "12,6", "12,8", "14,3", "14,11"],
    "★": ["7,7"]
}
points = {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 'K': 10, 'L': 1, 'M': 2,
          'N': 1, 'O': 1, 'P': 3, 'Q': 8, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 10, 'X': 10, 'Y': 10, 'Z': 10}
ammount = {'A': 9, 'B': 2, 'C': 2, 'D': 3, 'E': 15, 'F': 2, 'G': 2, 'H': 2, 'I': 8, 'J': 1, 'K': 1, 'L': 5,
           'M': 3, 'N': 6, 'O': 6, 'P': 2, 'Q': 1, 'R': 6, 'S': 6, 'T': 6, 'U': 6, 'V': 2, 'W': 1, 'X': 1, 'Y': 1, 'Z': 1}
board = []
speciales = []


def setup_board(size):
    b = []
    for x in range(size):
        line = []
        for y in range(size):
            space = " "
            line.append(space)
        b.append(line)
    for x in cases:
        for y in cases[x]:
            coord = y.split(",")
            b[int(coord[0])][int(coord[1])] = x
    return b


def printb(board):
    size = len(board)
    nobonus = True
    scrabble = "   S C R A B B L E"
    space = int((64-len(scrabble))/2)
    print(" "*space + scrabble)
    txt = "     "
    for x in range(len(board)):
        letter = chr(ord('A')+x)
        txt = txt + letter+"   "
    print(txt)
    print("   ╔═══"+"╤═══"*(size-1)+"╗")
    firstline = True
    l = 1
    for x in board:
        if not firstline:
            print("   ╟───"+"┼───"*(size-1)+"╢")
        else:
            firstline = False
        if l < 10:
            line = f" {l} ║"
        else:
            line = f"{l} ║"
        l = l+1
        firstcol = True
        for y in x:
            if len(y) == 3:
                add = y
                if nobonus:
                    add = "   "
            else:
                add = " "+y+" "
            if not firstcol:
                add = "│"+add
            else:
                firstcol = False

            line = line + add
        print(line+"║")
    print("   ╚═══"+"╧═══"*(size-1)+"╝")


def addword(x, y, word, dir):
    wordsplit = word.upper()
    coordx = x
    coordy = y
    score = 0
    dws = False
    tws = False
    coords = []
    for letter in wordsplit:
        board[coordx][coordy] = letter
        bonus = speciales[coordx][coordy]
        txt = ""
        if bonus == "dls":
            score = score + points[letter]*2
            txt = txt + f"{letter} : +{points[letter]}*2 (double lettre)"
        elif bonus == "tls":
            score = score + points[letter]*3
            txt = txt + f"{letter} : +{points[letter]}*3 (triple lettre)"
        else:
            score = score + points[letter]
            txt = txt + f"{letter} : +{points[letter]}"
        if bonus == "TWS":
            tws = True
            txt = txt + " Mot compte triple!"
        if bonus == "DWS" or bonus == "★":
            dws = True
            txt = txt + " Mot compte double!"
        print(txt)
        if dir == 'h':
            coordy = coordy+1
        else:
            coordx = coordx+1
    if dws:
        score = score*2
    if tws:
        score = score*3
    print(f"score final du mot : {score}")
    print("----------")
    return score


board = setup_board(15)
speciales = setup_board(15)

addword(7, 7, "test", 'h')
addword(7, 8, "erstest", 'v')
addword(9, 8, "steaks", 'h')
printb(board)
