import stdio
import stdrandom


#rank of cards, from 2 to 14 (inclusive so plus one), random int
rank = stdrandom.uniformInt(2, 14+1)

#rank of cards, from 1 to 4 (inclusive so plus one), random int
suit = stdrandom.uniformInt(1, 4+1)

rankStr = str(rank)
suitStr = str(suit)

#if card ranks are > 10 set numbers to names of cards
if rank == 11:
    rankStr = "Jack"
elif rank == 12:
    rankStr = "Queen"
elif rank == 13:
    rankStr = "King"
elif rank == 14:
    rankStr = "Ace"

#assign suits to cards
if suit == 1:
    suitStr = "Clubs"
elif suit == 2:
    suitStr = "Diamonds"
elif suit == 3:
    suitStr = "Hearts"
elif suit == 4:
    suitStr = "Spades"

#write desired output 
stdio.writeln((rankStr) + " of " + (suitStr))