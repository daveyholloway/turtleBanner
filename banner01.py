import turtle
################################################################################
# Return the sequence of moves for a given character.
#
# Key:
#      Fn : Forward n          Bn : Back n
#      Ln : Left n degrees     Rn : Right n degrees
#      U  : Pen up             D  : Pen down
#      S  : Start fill         E  : End fill
#
# HISTORY
# =======
# When       Who                     Why
# ---------- ----------------------- -------------------------------------------
# 04/01/2018 Dave Hol'               Initial Version
################################################################################
def getSequence(pChar):

    if pChar == "A":
        return ["U","F1","L90", "F1", "R90","S1", "D","F2","L90","F2","R90", \
                "F2","R90","F2","L90","F2", "L90","F6","L90","F1","R90","F1", \
                "L90","F4","L90","F1","R90", "F1","L90","F6","L90", "E","U", \
                "F2","L90","F3","D","S2", "F3","R90","F2", "R90","F3","R90", \
                "F2","E", "U","L180"]
    elif pChar == "B":
        return ["U","F1","L90", "F1", "R90","D","S1", "F5","L90","F1","R90", \
                "F1","L90","F2","L90","F1", "R90","F1","R90","F1","L90","F2", \
                "L90","F1","R90","F1","L90", "F5","L90","F7","L90","E", "U", \
                "F2","L90","F1","D","S2", "F2","R90","F2", "R90","F2","R90", \
                "F2","E", "U","R90","F3","D","S2","F2","R90","F2","R90", \
                "F2","R90","F2","E", "U","L180"]
    elif pChar == "C":
        return ["U","F1","L90", "F1", "R90", "F1", "D","S1", "F4","L90","F1", \
                "R90", "F1","L90","F1","L90", "F2", "L90","F1","R90","F2", \
                "R90","F5", "R90", "F2", "R90", "F1", "L90", "F2", "L90", \
                "F1", "L90", "F1", "R90", "F1", "L90", "F4", "L90", "F1", \
                "R90", "F1", "L90", "F5", "L90", "F1", "R90", "F1","E", \
                "U", "L90"]
    else:
        return ["D","F8","L90","F8","L90","F8","L90","F8","L90"]

################################################################################
# Process the sequence passed in and output a character at the required
# co-ordinates.
#
# pLine is the line colour, pFill1 is the fill colour for the letter being
# plotted, pFill2 is the fill colour of the background.
#
# HISTORY
# =======
# When       Who                     Why
# ---------- ----------------------- -------------------------------------------
# 04/01/2018 Dave Hol'               Initial Version
################################################################################
def plotSequence(pTurtle, pX, pY, pSize, pLine, pFill1, pFill2, pSequence):
    # First move to the specified position
    pTurtle.penup()
    pTurtle.setx(pX)
    pTurtle.sety(pY)

    # Then start looping thru the sequence passed in
    for i in range(0,len(pSequence)):

        # Determine the instruction
        wInstruction = pSequence[i][0]

        if wInstruction == "F":          # forward
            pTurtle.forward(int(pSequence[i][1:len(pSequence[i])]) * pSize)

        elif wInstruction == "B":        # backwards
            pTurtle.backwards(int(pSequence[i][1:len(pSequence[i])]) * pSize)

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

plotSequence(bob, -50, 0, 5, "Black", "Green", "White", getSequence("C"))
plotSequence(bob, 0, 0, 5, "Black", "Yellow", "White", getSequence("A"))
plotSequence(bob, 50, 0, 5, "Black", "Red", "White", getSequence("B"))
plotSequence(bob, 100, 0, 5, "Black", "Blue", "White", getSequence("C"))
