import numpy

class Player(object):

    # Number of arguments to represent the Tennisplayer
    __N = 12

    def __init__(self, name, pvector):
        # every tennis player has a name
        self.__name = name
        # check if the given vector has the right size
        if(len(pvector) != self.__N):
            print("Not enough arguments")
        else:
            # Probability the player hits the first serve
            self.__P1Serve = pvector[0]
            # Probability the player hits an ace with the first serve
            self.__P1ServeWinner = pvector[1]
            # Probability the player hits the second serve
            self.__P2Serve = pvector[2]
            # Probability the player hits an ace with the second serve
            self.__P2ServeWinner = pvector[3]
            # Bonus to the probability to hit a winner after the first serve
            # Idea: the player with the first serve can normally produced pressure
            # after the serve to get a more easy point
            self.__1ServeBonus = pvector[4]
            # Bonus to the probability to hit a winner after the second serve
            self.__2ServeBonus = pvector[5]
            # Determines for how many shots the bonus durates
            self.__bonusTime = 5
            # Probability to hit the return after the first serve back
            self.__P1Return = pvector[6]
            # Probability to hit a winner after the first serve
            self.__P1ReturnWinner = pvector[7]
            # Probability to hit the return after the second serve back
            self.__P2Return = pvector[8]
            # Probability to hit a winner after the second serve
            self.__P2ReturnWinner = pvector[9]
            # Probability to return the ball in a normal rally
            self.__PHit = pvector[10]
            # Probability to hit a winner in a rally
            self.__PHitWinner = pvector[11]

    # returns the name of the player
    def getName(self):
        return self.__name

    # next functions are all similar to each other
    # using the numpy random number generator with a bernoulli distribution
    # with the probabilities given by the player
    # the function return what events happened

    # if first serve hits we see if the player hits an ace then we return 2
    # if first serve hits and and the player can not shoot an ace then we return 0
    # if first serve fails and the second serve fails we return -1
    # if first serve fails and the second serve hits we return 1
    # and if the player shoot an ace with the second serve we return 2
    def getServe(self):
        if(numpy.random.binomial(1,self.__P1Serve,1) == 1):
            if (numpy.random.binomial(1, self.__P1ServeWinner, 1) == 1):
                return 2
            else:
                return 0
        elif(numpy.random.binomial(1, self.__P2Serve, 1) == 1):
            if (numpy.random.binomial(1, self.__P2ServeWinner, 1) == 1):
                return 2
            else:
                return 1
        else:
            return -1

    # we return a first serve and the player can either miss the shot the function returns -1
    # or hits a winner the function returns 1 or just returns the ball to the opponent the function returns 0
    def getS1Return(self):
        if (numpy.random.binomial(1, self.__P1Return, 1) == 1):
            if (numpy.random.binomial(1, self.__P1ReturnWinner, 1) == 1):
                return 1
            else:
                return 0
        else:
            return -1
    # we return a second serve and the player can either miss the shot the function returns -1
    # or hits a winner the function returns 1 or just returns the ball to the opponent the function returns 0
    def getS2Return(self):
        if (numpy.random.binomial(1, self.__P2Return, 1) == 1):
            if (numpy.random.binomial(1, self.__P2ReturnWinner, 1) == 1):
                return 1
            else:
                return 0
        else:
            return -1

    # two getHit
    # 1. for the returning player
    # 2. for the serving player because he gets a bonus

    # the player can either hit a winner => return 1
    # the player can miss his shot => return -1
    # the player returns the ball to the opponent => 0
    def getHitReturn(self):
        if(numpy.random.binomial(1, self.__PHit, 1) == 1):
            if(numpy.random.binomial(1, self.__PHitWinner, 1) == 1):
                return 1
            else:
                return 0
        else:
            return -1

    # additionally to getHitReturn the serving player gets a bonus for a specific number of shots
    # the bonus decreases linear with the number of shots
    # after the bounus expired the player shots only with his normal probabilities
    def getHitServe(self, numHits, serve):
        if (numpy.random.binomial(1, self.__PHit, 1) == 1):
            if (serve):
                if (numpy.random.binomial(1, self.__PHitWinner + max(
                            self.__1ServeBonus * ((self.__bonusTime - numHits) / self.__bonusTime), 0), 1) == 1):
                    return 1
                else:
                    return 0
            else:
                if (numpy.random.binomial(1, self.__PHitWinner + max(
                            self.__2ServeBonus * ((self.__bonusTime - numHits) / self.__bonusTime), 0), 1) == 1):
                    return 1
                else:
                    return 0
        else:
            return -1