from .game import Game
from .tiebreak import TieBreak

class Set(object):

    def __init__(self, player1, player2, count):
        self.__player1 = player1
        self.__p1Score = 0
        self.__player2 = player2
        self.__p2Score = 0
        self.count = count

    def run(self):
        while ((self.__p1Score < 6 and self.__p2Score < 6) or abs(self.__p2Score - self.__p1Score) < 2):
            if(self.__p1Score == 6 and self.__p2Score == 6):
                tieBreak = TieBreak(self.__player1, self.__player2).run()
                if (tieBreak == 1):
                    self.__p1Score += 1
                elif (tieBreak == 2):
                    self.__p2Score += 1
                else:
                    print("Error: unexpected value in set.py")
                print("Score %i - %i" % (self.__p1Score, self.__p2Score))
                break
            else:
                if(self.count % 2 == 0):
                    game = Game(self.__player1, self.__player2).run()
                    if(game == 1):
                        self.__p1Score += 1
                    elif(game == 2):
                        self.__p2Score += 1
                    else:
                        print("Error: unexpected value in set.py")
                        break
                else:
                    game = Game(self.__player2, self.__player1).run()
                    if (game == 1):
                        self.__p2Score += 1
                    elif (game == 2):
                        self.__p1Score += 1
                    else:
                        print("Error: unexpected value in set.py")
                        break
            self.count += 1
            print("Score %i - %i" %(self.__p1Score, self.__p2Score))
        print("Set finished")
        if (self.__p1Score > self.__p2Score):
            return 1
        elif (self.__p2Score > self.__p1Score):
            return 2
        else:
            return -1
