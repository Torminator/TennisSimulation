class Play(object):

    # player1 is always the server
    # player2 returns
    # game switches the parameter call
    def __init__(self, player1, player2):
        self.__player1 = player1
        self.__player2 = player2

    def run(self):
        p1Serve = self.__player1.getServe()
        if(p1Serve == 2):
            #print("Player 1 won a point by ace")
            return 1
        elif(p1Serve == -1):
            #print("Player 2 won a point by double fault")
            return 2
        elif(p1Serve == 1):
            #print("Second serve return")
            p2Return = self.__player2.getS2Return()
            if(p2Return == 1):
                #print("Player 2 won a point by winner")
                return 2
            elif(p2Return == -1):
                #print("Player 1 won a point by error")
                return 1
            elif(p2Return == 0):
                #print("Play goes on")
                count = 0
                while True:
                    p1Hit = self.__player1.getHitServe(count, False)
                    if(p1Hit == 1):
                        #print("Player 1 won a point by winner")
                        return 1
                        break
                    elif(p1Hit == -1):
                        #print("Player 2 won a point by error")
                        return 2
                        break
                    elif(p1Hit == 0):
                        #print("Play goes on")
                        p2Hit = self.__player2.getHitReturn()
                        if (p1Hit == 1):
                            #print("Player 2 won a point by winner")
                            return 2
                            break
                        elif (p1Hit == -1):
                            #print("Player 1 won a point by error")
                            return 1
                            break
                    else:
                        print("System broken")
                        return -1
                    count += 1
            else:
                print("System broken")
                return -1
        elif(p1Serve == 0):
            #print("First serve return")
            p2Return = self.__player2.getS1Return()
            if(p2Return == 1):
                #print("Player 2 won a point by winner")
                return 2
            elif(p2Return == -1):
                #print("Player 1 won a point by error")
                return 1
            elif(p2Return == 0):
                #print("Play goes on")
                count = 0
                while True:
                    p1Hit = self.__player1.getHitServe(count, True)
                    if (p1Hit == 1):
                        #print("Player 1 won a point by winner")
                        return 1
                        break
                    elif (p1Hit == -1):
                        #print("Player 2 won a point by error")
                        return 2
                        break
                    elif (p1Hit == 0):
                        #print("Play goes on")
                        p2Hit = self.__player2.getHitReturn()
                        if (p1Hit == 1):
                            #print("Player 2 won a point by winner")
                            return 2
                            break
                        elif (p1Hit == -1):
                            #print("Player 1 won a point by error")
                            return 1
                            break
                    else:
                        print("System broken")
                        return -1
                    count += 1
            else:
                print("System broken")
                return -1
        else:
            print("System broken")
            return -1




