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
        return ["U","F1","D","F2","L90","F2","R90","F2","R90","F2","L90","F2", \
                "L90","F6","L90","F1","R90","F1","L90","F4","L90","F1","R90", \
                "F1","L90","F6","L90","U","F2","L90","F3","D","F3","R90","F2", \
                "R90","F3","R90","F2","U","L180"]
    elif pChar == "B":
        return ["U","F1","D","F5","L90","F1","R90","F1","L90","F2","L90","F1", \
                "R90","F1","R90","F1","L90","F2","L90","F1","R90","F1","L90", \
                "F5","L90","F7","L90","U","F2","L90","F1","D","F2","R90","F2", \
                "R90","F2","R90","F2","U","R90","F3","D","F2","R90","F2","R90", \
                "F2","R90","F2","U","L180"]

    else:
        return ["D","F8","L90","F8","L90","F8","L90","F8","L90"]

################################################################################
# Process the sequence passed in and output a character at the required
# co-ordinated.
#
# HISTORY
# =======
# When       Who                     Why
# ---------- ----------------------- -------------------------------------------
# 04/01/2018 Dave Hol'               Initial Version
################################################################################
def plotSequence(pTurtle, pX, pY, pSize, pLine, pFill, pSequence):
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


################################################################################
# Program starts here
#
################################################################################

bob=turtle.Turtle()

plotSequence(bob, 0, 0, 5, "Black", "Yellow", getSequence("A"))
plotSequence(bob, 50, 0, 7, "Black", "Yellow", getSequence("B"))
plotSequence(bob, 150, 0, 9, "Black", "Yellow", getSequence("A"))
