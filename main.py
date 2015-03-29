# Joe Moraal and Braedon McCoy

from enum import Enum
import random

class CardPosition(Enum):
    LEFT = 0
    MIDDLE = 1
    RIGHT = 2

class Player:
    def __init__(self, inName, inHand, isMax):
        left, middle, right = inHand

        self.name = inName
        self.reversed = (left > right)
        self.hand = (left, middle, right)
        self.isMax = isMax

    def chooseMove(self, middleCard):
        left, middle, right = self.hand

        if reversed:
            if middleCard > left:
                self.hand = (middleCard, middle, right)
                return left
            elif middleCard < right:
                self.hand = (left, middle, middleCard)
                return right
            else:
                self.hand = (left, middleCard, right)
                return middle
        else:
            if middleCard < left:
                self.hand = (middleCard, middle, right)
                return left
            elif middleCard > right:
                self.hand = (left, middle, middleCard)
                return right
            else:
                self.hand = (left, middleCard, right)
                return middle

    def isInOrder(self):
        left, middle, right = self.hand

        ascending = (left < middle) and (middle < right)
        descending = (left > middle) and (middle > right)
        return ascending or descending

def deal():
    cardList = [x for x in range(1, 8)]
    print(cardList)
    cards = []

    while len(cardList) > 0:
        index = random.randint(0, len(cardList) - 1)
        cards.append(cardList.pop(index))

    playerOne = Player("playerOne", (cards[0], cards[2], cards[4]), True)
    playerTwo = Player("playerTwo", (cards[1], cards[3], cards[5]), False)
    return (playerOne, playerTwo, cards[6])

if __name__ == "__main__":
    gameOver = False
    winningPlayer = None
    playerOne, playerTwo, middleCard = deal()
    playerOrder = (playerOne, playerTwo)

    while not gameOver:
        h = 0
        # PLAYER ONE
        middleCard = playerOne.chooseMove(middleCard)

        if playerOne.isInOrder():
            gameOver = True
            winningPlayer = playerOne

        left, middle, right = playerOne.hand
        if(playerOne.isMax):
            if(left > middle):
                h += 1
            if(left > right):
                h += 1
            if(middle > right):
                h += 1
        else:
            if(left > middle):
                h -= 1
            if(left > right):
                h -= 1
            if(middle > right):
                h -= 1

        print ("%s: (%d, %d, %d)" % (playerOne.name, left, middle, right))
        print ("middleCard: %d" % (middleCard))

        # PLAYER TWO
        middleCard = playerTwo.chooseMove(middleCard)

        if playerTwo.isInOrder():
            gameOver = True
            winningPlayer = playerTwo

        left, middle, right = playerTwo.hand
        if(playerTwo.isMax):
            if(left > middle):
                h += 1
            if(left > right):
                h += 1
            if(middle > right):
                h += 1
        else:
            if(left > middle):
                h -= 1
            if(left > right):
                h -= 1
            if(middle > right):
                h -= 1

        print ("%s: (%d, %d, %d)" % (playerTwo.name, left, middle, right))
        print ("middleCard: %d" % (middleCard))

        

    print ("%s won the game!" % (winningPlayer.name))
    if(winningPlayer.isMax):
        print("+1")
    else:
        print("-1")
