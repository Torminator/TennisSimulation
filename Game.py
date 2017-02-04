from Play import Play

class Game(object):

    def __init__(self, player1, player2):
        self.__player1 = player1
        self.__p1Score = 0
        self.__player2 = player2
        self.__p2Score = 0

    def run(self):
        while((self.__p1Score < 4 and self.__p2Score < 4) or abs(self.__p2Score-self.__p1Score) < 2):
            play = Play(self.__player1, self.__player2).run()
            if(play == 1):
                self.__p1Score += 1
            elif(play == 2):
                self.__p2Score += 1
            else:
                print("Error: unexpected value in Game.py")
                break
            #print("Score %i - %i" %(self.__p1Score, self.__p2Score))
        #print("Game finished")
        if(self.__p1Score > self.__p2Score):
            return 1
        elif(self.__p2Score > self.__p1Score):
            return 2
        else:
            return -1
