#The sample algorithm seems like a decent approach but seems very complicated to execute.
#I tried numerous variations of tic tac toe on paper to identify,
#how would the algorithm find a possibility of fork, etc.
#It all seems very complicated and an easier way would be instead to check all possible moves of both players
#to identify the best move.
#The best move would be the one which doesn't result in a loss.
#The human and computer moves can be virtually checked recursively for all possible paths.
#While the code is recursively checking al the best paths and finding the best path,
#It can then store the best paths in a list, which can be used to automatically decide what move to place 
#based on human's move
import random

def generateBoard(humanOs,compXs):
    board = [' '] * 9
    for i in range(9):
        if (i in humanOs):
            board[i] = 'O'
        elif(i in compXs):
            board[i] = 'X'
        else:
            board[i] = i
    print ("Current Board looks like: \n")
    print ("%s %s %s" % (board[0], board[1], board[2]))
    print ("%s %s %s" % (board[3], board[4], board[5]))
    print ("%s %s %s" % (board[6], board[7], board[8]))
    print ("\n")

def humanMove(humanOs,compXs):
    generateBoard(humanOs,compXs)
    print "Choose Your Move: "
    move==input()
    if ((move >=0) and (move < 9) and (move not in humanOs) and (move not in compXs)):
        print ("You moved on %d" % move)
        humanOs.append(move)
        return humanOs
    else:
        print "Invalid move, Try again!"
        humanMove(humanOs,compXs)

def checkresult(humanOs,compXs):
    #TODO
    return result


def compMove(humanOs,compXs):
    #TODO
    return compXs

humanOs=[]
compXs=[]
generateBoard(humanOs,compXs)
print "Your moves are represented by O and computer's moves are represented by X"
first = random.randint(0, 1)
if (first == 0):
    print "You won the Toss, You move first"
else:
    print "You lost the Toss, Computer Moves first\n"

#This while block loops untill the entire board is filled up or until a break is called in case of either win
while (len(humanOs)+len(compXs)<9):

    #This if else block decides whose turn it is to play.
    #If Human won the toss then number of human moves should always be equal or more than computer moves and vice versa
    if ((first == 0 and len(humanOs) > len(compXs)) or (first == 1 and len(humanOs) >= len(compXs))):
        compXs= compMove(humanOs,compXs)
    else:
        humanOs=humanMove(humanOs,compXs)

    #This if else block announces if there is a win, loss, draw or doesnt do anything if neither
    result = checkresult(humanOs,compXs)
    if (result == 1):
        print "The Computer Won. The computer can't been beaten"
        break
    elif (result == 2):
        print "You won, My algorithm is faulty"
        break
    elif (len(humanOs)+len(compXs) == 9):
        print "The Game is a draw. The computer can't been beaten"
        break
    else:
        pass
        
print "Game Over"
