from TennisPlayer import Player
from Match import Match

# creating the vector to describe the skills of the players
# no empirical evidence, just toy numbers
goodServePlayer = [0.65, 0.075, 0.99, 0.005, 0.15, 0.05, 0.75, 0.005, 0.9, 0.075, 0.8, 0.05]
goodWinnerPlayer = [0.6, 0.05, 0.99, 0.003, 0.1, 0.04, 0.8, 0.005, 0.9, 0.1, 0.85, 0.07]
goodReturnPlayer = [0.57, 0.02, 0.98, 0.003, 0.075, 0.03, 0.85, 0.015, 0.95, 0.2, 0.8, 0.05]
goodBaselinePlayer = [0.6, 0.03, 0.99, 0.002, 0.07, 0.03, 0.85, 0.005, 0.925, 0.075, 0.9, 0.02]

# create instances of two players who play a match
player1 = Player("Milos Raonic", goodServePlayer)
player2 = Player("Andy Murray", goodWinnerPlayer)
player3 = Player("Kei Nishikori", goodBaselinePlayer)
player4 = Player("Tomas Berdych", goodReturnPlayer)

# create an instance of a match featuring both players
sf1match = Match(player1, player2, 3).run()
sf2match = Match(player3, player4, 3).run()
# starts the match
if(sf1match == 1):
    if(sf2match == 1):
        fmatch = Match(player1, player3, 3).run()
    else:
        fmatch = Match(player1, player4, 3).run()
else:
    if (sf2match == 1):
        fmatch = Match(player2, player3, 3).run()
    else:
        fmatch = Match(player2, player4, 3).run()