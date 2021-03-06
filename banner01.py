import turtle
################################################################################
# Return the sequence of moves for a given character.
#
# Instructions
# ============
# When adding a sequence, ensure the turtle starts in the bottom left corner
# and finishes in the top right corner, ready to start the next character.
#
# Key:
#      Fn : Forward n          Bn : Back n
#      Ln : Left n degrees     Rn : Right n degrees
#      U  : Pen up             D  : Pen down
#      Sn : Start fill #n      E  : End fill
#
# HISTORY
# =======
# When       Who                     Why
# ---------- ----------------------- -------------------------------------------
# 04/01/2018 Dave Hol'               Initial Version
################################################################################
def getSequence(pChar):

    if pChar == "A":
        return ["U","F1","L90", "F1", "R90", \
                "S1", "D","F2","L90","F2","R90", \
                "F2","R90","F2","L90","F2", "L90","F6","L90","F1","R90","F1", \
                "L90","F4","L90","F1","R90", "F1","L90","F6","L90", "E","U", \
                "F2","L90","F3","D","S2", "F3","R90","F2", "R90","F3","R90", \
                "F2","E", "U","L180","F5","R90","F4","L90"]
    elif pChar == "B":
        return ["U","F1","L90", "F1", "R90", \
                "S1", "D", "F5","L90","F1","R90", \
                "F1","L90","F2","L90","F1", "R90","F1","R90","F1","L90","F2", \
                "L90","F1","R90","F1","L90", "F5","L90","F7","L90","E", "U", \
                "F2","L90","F1","D","S2", "F2","R90","F2", "R90","F2","R90", \
                "F2","E", "U","R90","F3","D","S2","F2","R90","F2","R90", \
                "F2","R90","F2","E", "U","L180", \
                "F5", "R90", "F5", "L90"]
    elif pChar == "C":
        return ["U","F1","L90", "F1", "R90", "F1", "D","S1", "F4","L90","F1", \
                "R90", "F1","L90","F1","L90", "F2", "L90","F1","R90","F2", \
                "R90","F5", "R90", "F2", "R90", "F1", "L90", "F2", "L90", \
                "F1", "L90", "F1", "R90", "F1", "L90", "F4", "L90", "F1", \
                "R90", "F1", "L90", "F5", "L90", "F1", "R90", "F1","E", \
                "U", "L90", \
                "F6", "R90", "F1", "L90"]
    elif pChar == "D":
        return ["U","F1","L90", "F1", "R90", "D","S1", "F5","L90","F1", \
                "R90", "F1","L90","F5","L90", "F1", "R90","F1", "L90","F5", \
                "L90","F7", "L90", "E", "U", \
                "F2", "L90", "F1", \
                "D", "S2", "F5", "R90", "F2", "R90", "F5", "R90", "F2", \
                "R180", "E","U", \
                "F5", "R90", "F2", "L90"]
    elif pChar == "E":
        return ["U","F1","L90", "F1", "R90", \
                "S1", "D", \
                "F6","L90","F1", "L90", "F4", "R90", "F2", "R90", "F3", \
                "L90", "F1", "L90", "F3", "R90", "F2", "R90", "F4", "L90", \
                "F1", "L90", "F6", "L90", "F7", \
                "E", "U", \
                "F1", "L90", "F7"]
    elif pChar == "F":
        return ["U","F1","L90", "F1", "R90", \
                "S1", "D", \
                "F2","L90","F3", "R90", "F3", \
                "L90", "F1", "L90", "F3", "R90", "F2", "R90", "F4", "L90", \
                "F1", "L90", "F6", "L90", "F7", \
                "E", "U", \
                "F1", "L90", "F7"]
    elif pChar == "G":
        return ["U","F1","L90", "F1", "R90", "F1", "D","S1", "F4","L90","F1", \
                "R90", "F1","L90","F3","L90", "F3", "L90","F1", \
                "L90", "F1", "R90","F2", "R90", "F2", \
                "R90","F5", "R90", "F2", "R90", "F1", "L90", "F2", "L90", \
                "F1", "L90", "F1", "R90", "F1", "L90", "F4", "L90", "F1", \
                "R90", "F1", "L90", "F5", "L90", "F1", "R90", "F1","E", \
                "U", "L90", \
                "F6", "R90", "F1", "L90"]
    elif pChar == "H":
        return ["U","F1","L90", "F1", "R90", \
                "S1", "D", \
                "F2","L90","F3", "R90", "F2", \
                "R90", "F3", "L90", "F2", "L90", "F7", "L90", "F2", "L90", \
                "F3", "R90", "F2", "R90", "F3", "L90", "F2", "L90", "F7", \
                "E", "U", \
                "F1", "L90", "F7"]
    elif pChar == "I":
        return ["U","F1","L90", "F1", "R90", \
                "S1", "D", \
                "F6","L90","F1", "L90", "F2", "R90", "F5", "R90", "F2", \
                "L90", "F1", "L90", "F6", "L90", "F1", "L90", "F2", "R90", \
                "F5", "R90", "F2", "L90", "F1", \
                "E", "U", \
                "F1", "L90", "F7"]
    elif pChar == "J":
        return ["U","F1","L90", "F2", "R90", \
                "S1", "D", \
                "F1","R90","F1", "L90", "F3", "L90", "F1", "R90", "F1", \
                "L90", "F5", "R90", "F1", "L90", "F1", "L90", "F5", "L90", \
                "F1", "L90", "F2", "R90", "F5", "R90", "F1", "R90", "F1", \
                "L90", "F2", "L90", "F1", \
                "E", "U", \
                "F2", "L90", "F7"]
    elif pChar == "K":
        return ["U","F1","L90", "F1", "R90", \
                "S1", "D", \
                "F2","L90","F2", "R90", "F1", "R90", "F1", "L90", "F1", \
                "R90", "F1", "L90", "F2", "L90", "F1", "L90", "F1", "R90", \
                "F1", "L90", "F1", "R90", "F1", "L90", "F1", "R90", "F1", \
                "R90", "F1", "L90", "F1", "R90", "F1", "L90", "F1", "R90", \
                "F1", "L90", "F1", "L90", "F2", "L90", "F1", "R90", "F1", \
                "L90", "F1", "R90", "F1", "R90", "F2", "L90", "F2", "L90", \
                "F7", \
                "E", "U", \
                "F1", "L90", "F7"]
    elif pChar == "L":
        return ["U","F1","L90", "F1", "R90", \
                "S1", "D", \
                "F6","L90","F1", "L90", "F4", "R90", "F6", "L90", "F2", \
                "L90", "F7", \
                "E", "U", \
                "F1", "L90", "F7"]
    elif pChar == "M":
        return ["U","F1","L90", "F1", "R90", \
                "S1", "D", \
                "F2","L90","F4", "R90", "F1", "R90", "F2", "L90", "F1", \
                "L90", "F2", "R90", "F1", "R90", "F4", "L90", "F2", "L90", "F7", \
                "L90", "F2", "L90", "F1", "R90", "F1", "L90", "F1", "R90", "F1", \
                "R90", "F1", "L90", "F1", "R90", "F1", "L90", "F2", "L90" ,"F7", \
                "E", "U", \
                "F1", "L90", "F7"]
    elif pChar == "N":
        return ["U","F1","L90", "F1", "R90", \
                "S1", "D", \
                "F2","L90","F3", "R90", "F1", "R90", "F1", "L90", "F1", "R90", "F2", \
                "L90", "F2", "L90", "F7", "L90", "F2", "L90", "F3", "R90", "F1", \
                "R90", "F1", "L90", "F1", "R90", "F2", "L90", "F2", "L90", "F7", \
                "E", "U", \
                "F1", "L90", "F7"]
    elif pChar == "O":
        return ["U","F1","L90", "F2", "R90", \
                "S1", "D", \
                "F1","R90","F1", "L90", "F4", "L90", "F1", "R90", "F1", "L90", "F5", \
                "L90", "F1", "R90", "F1", "L90", "F4", "L90", "F1", "R90", "F1", \
                "L90", "F5", \
                "E", "U", \
                "L90", "F2", "S2", "D", "F2", "L90", "F5", "L90", "F2", "L90", "F5", \
                "L90", "E", "U", \
                "F5", "R90", "F2", "L90"]
    elif pChar == "P":
        return ["U","F1","L90", "F1", "R90", \
                "S1", "D", \
                "F2","L90","F3", "R90", "F3", "L90", "F1", "R90", "F1", \
                "L90", "F2", "L90", "F1", "R90", "F1", "L90", "F5", "L90", "F7", \
                "E", "U", \
                "L90", "F2","L90", "F4",\
                "S2", "D", \
                "F2", "R90", "F2", "R90", "F2", "R90", "F2","E", "U", \
                "L180", "F5", "R90", "F5", "L90"]
    elif pChar == "Q":
        return ["U","F1","L90", "F2", "R90", \
                "S1", "D", \
                "F1","R90","F1", "L90", "F2", "L90", "F1", "R90", "F1", "R90", "F1", \
                "L90", "F2", "L90", "F1", "L90", "F1", "R90", "F1", "R90", "F1", \
                "L90",  "F4", \
                "L90", "F1", "R90", "F1", "L90", "F4", "L90", "F1", "R90", "F1", \
                "L90", "F5", \
                "E", "U", \
                "L90", "F2", "S2", "D", "F1", "L90", "F2", "R90", "F1", "L90", "F3", \
                "L90", "F2", "L90", "F5", "E", "U", \
                "L90", "F2", "L90", "F1", "S2", "D", "F1", "R90", "F1", "R90", \
                "F1", "R90", "F1", "E", "U", \
                "L180", "F3", "R90", "F3", "L90"]
    elif pChar == "R":
        return ["U","F1","L90", "F1", "R90", \
                "S1", "D", \
                "F2","L90","F3", "R90", "F1", "R90", "F1", "L90", "F1", "R90", "F2", \
                "L90", "F2", "L90", "F2", "L90", "F1", "R90", "F2", "R90", "F1", \
                "L90", "F2", "L90", "F1", "R90", "F1", "L90", "F5", "L90", "F7", \
                "E", "U", \
                "L90", "F2","L90", "F4",\
                "S2", "D", \
                "F2", "R90", "F2", "R90", "F2", "R90", "F2","E", "U", \
                "L180", "F5", "R90", "F5", "L90"]
    elif pChar == "S":
        return ["U","F1","L90", "F2", "R90", \
                "S1", "D", \
                "F1","R90","F1", "L90", "F4", "L90", "F1", "R90", "F1", "L90", "F2", \
                "L90", "F1", "R90", "F1", "L90", "F3", "R90", "F2", "R90", "F2", \
                "R90", "F1", "L90", "F2", "L90", "F1", "L90", "F1", "R90", "F1", "L90", \
                "F4", "L90", "F1", "R90", "F1", "L90", "F2", "L90", "F1", "R90", "F1", \
                "L90", "F3", "R90", "F2", "R90", "F2", "R90", "F1", "L90", "F2", "L90", \
                "F1", "L90", "E", "U", "F7", "R90", "F2", "L90"]
    elif pChar == "T":
        return ["U","F3","L90", "F1", "R90", \
                "S1", "D", \
                "F2","L90","F6", "R90", "F2", "L90", "F1", "L90", "F6", \
                "L90", "F1", "L90", "F2", "R90", "F6", "L90", \
                "E", "U", \
                "F5", "R90", "F1","L90"]
    elif pChar == "U":
        return ["U","F1","L90", "F2", "R90", \
                "S1", "D", \
                "F1","R90","F1", "L90", "F4", "L90", "F1", "R90", "F1", "L90", "F6", \
                "L90", "F2", "L90", "F6", "R90", "F2", "R90", "F6", "L90", "F2", \
                "L90", "F6", "L90", "F1", \
                "E", "U", \
                "F7", "R90", "F2", "L90"]
    elif pChar == "V":
        return ["U","F2","L90", "F2", "R90", \
                "S1", "D", \
                "F1","R90","F1", "L90", "F2", "L90", "F1", "R90", "F1", "L90", "F1", \
                "R90", "F1", "L90","F5", "L90", "F2" , "L90", "F5", \
                "R90", "F2", "R90", "F5", "L90", "F2", \
                "L90", "F5", "L90", "F1", "R90", "F1", "L90", \
                "E", "U", \
                "F6", "R90", "F2", "L90"]
    elif pChar == "W":
        return ["U","F1","L90", "F1", "R90", \
                "S1", "D", \
                "F2", "L90", "F1", "R90", "F1", "L90", "F1", "R90", "F1", \
                "R90", "F1", "L90", "F1", "R90", "F1", "L90", "F2", "L90" ,"F7", \
                "L90", "F2","L90","F4", "R90", "F1", "R90", "F2", "L90", "F1", \
                "L90", "F2", "R90", "F1", "R90", "F4", "L90", "F2", "L90", "F7", \
                "E", "U", \
                "F1", "L90", "F7"]
    elif pChar == "X":
        return ["U","F1","L90", "F1", "R90", \
                "S1", "D", \
                "F2", "L90", "F2", "R90", "F2", "R90", "F2", "L90", "F2", \
                "L90", "F2", "L90", "F1", "R90", "F1", "L90", "F1", "R90" ,"F1", \
                "R90", "F1","L90","F1", "R90", "F1", "L90", "F2", "L90", \
                "F2", "L90", "F2", "R90", "F2", "R90", "F2", "L90", "F2", \
                "L90", "F2", "L90", "F1", "R90", "F1", "L90", "F1", "R90" ,"F1", \
                "R90", "F1","L90","F1", "R90", "F1", "L90", "F2", \
                "E", "U", \
                "F1", "L90", "F7"]
    elif pChar == "Y":
        return ["U","F3","L90", "F1", "R90", \
                "S1", "D", \
                "F2", "L90", "F3", "R90", "F1", "L90", "F1", "R90", "F1", \
                "L90", "F3", "L90", "F2", "L90", "F3", "R90", "F2", "R90" ,"F3", \
                "L90", "F2","L90","F3", "L90", "F1", "R90", "F1", "L90", \
                "F1", "R90", "F3", "L90", \
                "E", "U", \
                "F5", "R90", "F1","L90"]
    elif pChar == "Z":
        return ["U","F1","L90", "F1", "R90", \
                "S1", "D", \
                "F6", "L90", "F1", "L90", "F4", "R90", "F1", "R90", "F1", \
                "L90", "F1", "R90", "F1", "L90", "F1", "R90", "F1", "L90" ,"F1", \
                "R90", "F1", "L90", "F2", "L90", \
                "F6", "L90", "F1", "L90", "F4", "R90", "F1", "R90", "F1", \
                "L90", "F1", "R90", "F1", "L90", "F1", "R90", "F1", "L90" ,"F1", \
                "R90", "F1", "L90", "F2", "L90", \
                "E", "U", \
                "F7", "R90", "F1","L90"]
    elif pChar == " ":
        return ["U","F8"]
    else:
        return ["U","F1","L90", "F1", "R90", "D", \
                "F6","L90","F6","L90","F6","L90","F6","L90", "U", \
                "F7","R90","F1","L90"]

################################################################################
# Process the sequence passed in and output a character at the current turtle
# position.
#
# pLine is the line colour, pFill1 is the fill colour for the letter being
# plotted, pFill2 is the fill colour of the background.
#
# HISTORY
# =======
# When       Who                     Why
# ---------- ----------------------- -------------------------------------------
# 04/01 /2018 Dave Hol'               Initial Version
# 05/01/2018 Dave Hol'               Removed X and Y parameters as we use the
#                                    current turtle position.
################################################################################
def plotSequence(pTurtle, pSize, pLine, pFill1, pFill2, pSequence):

    # Start looping thru the sequence passed in
    for i in range(0,len(pSequence)):

        # Determine the instruction
        wInstruction = pSequence[i][0]

        if wInstruction == "F":          # forward
            pTurtle.forward(int(pSequence[i][1:len(pSequence[i])]) * pSize)

        elif wInstruction == "B":        # backwards
            pTurtle.backward(int(pSequence[i][1:len(pSequence[i])]) * pSize)

        elif wInstruction == "L":        # left
            pTurtle.left(int(pSequence[i][1:len(pSequence[i])]))

        elif wInstruction == "R":        # right
            pTurtle.right(int(pSequence[i][1:len(pSequence[i])]))

        elif wInstruction == "U":        # pen up
            pTurtle.penup()

        elif wInstruction == "D":        # pen down
            pTurtle.pendown()

        elif wInstruction == "S":        # begin fill
            # The number after S determines which of the 2 fill colours to use
            if pSequence[i][1:len(pSequence[i])] == "1":
                pTurtle.color(pLine,pFill1)
            elif pSequence[i][1:len(pSequence[i])] == "2":
                pTurtle.color(pLine,pFill2)

            pTurtle.begin_fill()

        elif wInstruction == "E":        # end fill
            pTurtle.end_fill()


################################################################################
# Program starts here
#
################################################################################

bob=turtle.Turtle()

wSize = 5
bob.penup()
bob.backward(150)

wMessage="EKIT EKIT EKIT EKIT EKIT "


for i in range(0,len(wMessage)):
    plotSequence(bob, wSize, "Black", "Green", "White", getSequence(wMessage[i]))
    bob.forward(wSize)
    bob.left(360/len(wMessage))
