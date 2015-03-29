# Joe Moraal and Braedon McCoy

from enum import Enum
import random


def evalHand(self, hand):
    retval = 0
    left, middle, right = hand

    if left > middle then ++retval
    if middle > right then ++retval
    if left > right then ++retval

    return retval

class Player:
    def __init__(self, name, hand):
        self.hand = hand
        self.name = name

    def complete(self):
        return abs(evalHand(self.hand)) == 3

## version of deal with randomization.
def deprecated_deal():
    cardList = [x for x in range(1, 8)]
    print(cardList)
    cards = []

    while len(cardList) > 0:
        index = random.randint(0, len(cardList) - 1)
        cards.append(cardList.pop(index))

    playerMax = Player("max", (cards[0], cards[2], cards[4]))
    playerMin = Player("min", (cards[1], cards[3], cards[5]))
    return (playerMax, playerMin, cards[6])

def deal():
    playerMax = Player("max", (6, 3, 1))
    playerMin = Player("min", (7, 5, 2))
    return (playerMax, playerMin, 4)

class Node:
    def __init__(self, maxHand, minHand, middleCard):
        self.maxHand = maxHand
        self.minHand = minHand
        self.middleCard = middleCard
        self.children = None

def genNodes_recursiveHelper(node, isMax, depth):
    if depth < 3:
        left, middle, right = (if isMax then node.maxHand else node.minHand)

        leftSwap = (node.middleCard, middle, right)
        middleSwap = (left, node.middleCard, right)
        rightSwap = (left, middle, node.middleCard)

        maxHand = (if isMax then leftSwap else node.maxHand)
        minHand = (if isMax then node.minHand else leftSwap)
        leftChild = Node(maxHand, minHand, left)

        maxHand = (if isMax then middleSwap else node.maxHand)
        minHand = (if isMax then node.minHand else middleSwap)
        middleChild = Node(maxHand, minHand, middle)

        maxHand = (if isMax then rightSwap else node.maxHand)
        minHand = (if isMax then node.minHand else rightSwap)
        rightChild = Node(maxHand, minHand, right)

        leftChild = genNodes_recursiveHelper(leftChild, not isMax, depth + 1)
        middleChild = genNodes_recursiveHelper(middleChild, not isMax, depth + 1)
        rightChild = genNodes_recursiveHelper(rightChild, not isMax, depth + 1)

        node.children = (leftChild, middleChild, rightChild)

    return node

def genNodes(playerMax, playerMin, middleCard):
    rootNode = Node(playerMax.hand, playerMin.hand, middleCard)
    return genNodes_recursiveHelper(rootNode, True, 0)

def pruneNodes_recursiveHelper():
    pass

def pruneNodes():
    pass

def evalMove(hand, middleCard):
    left, middle, right = hand

    hl = evalHand((middleCard, middle, right))
    hm = evalHand((left, middleCard, right))
    hr = evalHand((left, middle, middleCard))

    return (hl, hm, hr)

if __name__ == "__main__":
    playerMax, playerMin, middleCard = deal()
    rootNode = genNodes(playerMax, playerMin, middleCard)
    result = pruneNodes(rootNode)

    print ("Result: %d" % (result))
