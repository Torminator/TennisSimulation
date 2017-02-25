from .play import Play

class TieBreak(object):

    def __init__(self, player1, player2):
        self.__player1 = player1
        self.__p1Score = 0
        self.__player2 = player2
        self.__p2Score = 0

    def run(self):
        whoseTurn = True
        count = 0
        while((self.__p1Score < 7 and self.__p2Score < 7) or abs(self.__p2Score-self.__p1Score) < 2):
            if(count % 2 != 0):
                whoseTurn = not whoseTurn
            if(whoseTurn):
                play = Play(self.__player1, self.__player2).run()
                if(play == 1):
                    self.__p1Score += 1
                elif(play == 2):
                    self.__p2Score += 1
                else:
                    print("Error: unexpected value in TieBreak.py")
                    break
            else:
                play = Play(self.__player2, self.__player1).run()
                if (play == 1):
                    self.__p2Score += 1
                elif (play == 2):
                    self.__p1Score += 1
                else:
                    print("Error: unexpected value in TieBreak.py")
                    break
            count += 1
            #print("Score %i - %i" %(self.__p1Score, self.__p2Score))
        #print("Game finished")
        if(self.__p1Score > self.__p2Score):
            return 1
        elif(self.__p2Score > self.__p1Score):
            return 2
        else:
            return -1
