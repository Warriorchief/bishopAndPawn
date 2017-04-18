"""
LAST PROBLEM FROM LEVEL9 OF INTRO TO CODEFIGHTS
Given the positions of a white bishop and a black pawn on the standard chess board, 
determine whether the bishop can capture the pawn in one move.

The bishop has no restrictions in distance for each move, but is limited to diagonal
movement. Check out the example below to see how it can move:

For bishop = "a1" and pawn = "c3", the output should be
bishopAndPawn(bishop, pawn) = true.

For bishop = "h1" and pawn = "h3", the output should be
bishopAndPawn(bishop, pawn) = false.

Input/Output
[time limit] 4000ms (py3)
[input] string bishop
Coordinates of the white bishop in the chess notation.
[input] string pawn
Coordinates of the black pawn in the same notation.
[output] boolean
true if the bishop can capture the pawn, false otherwise.
"""


fyles={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
def bishopAndPawn(bishop, pawn):
    bishspots=[]
    rank=int(bishop[1])
    fyle=fyles[bishop[0]]
    start=(fyle,rank)
    print('bishop starts on the fyle and rank',start)
    bishspots.append(start)    
    #move leftward and upward
    b=start
    f=b[0]
    r=b[1]
    while f>=1 and r<=8:
        b=(f,r)
        bishspots.append(b)
        print('adding the spot',b)
        f-=1
        r+=1    
    #move rightward and upward
    b=start
    f=b[0]
    r=b[1]
    while f<=8 and r<=8:
        b=(f,r)
        bishspots.append(b)
        print('adding the spot',b)
        f+=1
        r+=1        
    #move leftward and downward
    b=start
    f=b[0]
    r=b[1]
    while f>=1 and r>=1:
        b=(f,r)
        bishspots.append(b)
        print('adding the spot',b)
        f-=1
        r-=1        
    #move rightward and downward
    b=start
    f=b[0]
    r=b[1]
    while f<=8 and r>=1:
        b=(f,r)
        bishspots.append(b)
        print('adding the spot',b)
        f+=1
        r-=1           
    bishspots=list(set(bishspots))
    print(bishspots)    
    pawnfyle=fyles[pawn[0]]
    pawnrank=int(pawn[1])
    pawnspot=(pawnfyle,pawnrank)
    print('pawnspot is',pawnspot)
    return pawnspot in bishspots

bishop= "g1"
pawn= "f3"
#print(bishopAndPawn(bishop,pawn)) #--> false CORRECT 