from .set import Set

class Match(object):

    def __init__(self, player1, player2, sets):
        # set the first player in the match
        self.__player1 = player1
        # set his score to 0
        self.__p1Score = 0
        # set the second player in the match
        self.__player2 = player2
        # set his score to 0
        self.__p2Score = 0
        # set number of sets to win (normal tournaments = 2, grand slam = 3)
        self.__numofWSets = sets

    def run(self):
        count = 0
        stats = [0,0,0,0,0,0]
        # the players play so long until one player reach the necessary number of won sets
        while (self.__p1Score < self.__numofWSets and self.__p2Score < self.__numofWSets):
            # create a new instance set
            set = Set(self.__player1, self.__player2, count)
            # start a new set and get the result
            setResult = set.run()
            # check who won the set and add it to the score
            if(setResult == 1):
                self.__p1Score += 1
            elif(setResult == 2):
                self.__p2Score += 1
            else:
                print("Error: unexpected value in match.py")
                break
            # the counter to know how many games are played to determine whose turn it is to serve
            count += set.count
            print("Score %i - %i" %(self.__p1Score, self.__p2Score))
            print()
        print("Match finished")
        print("%s %i:%i %s" %(self.__player1.getName(), self.__p1Score, self.__p2Score, self.__player2.getName()))
        print()
        if(self.__p1Score > self.__p2Score):
            return 1
        else:
            return 2
