## Braedon McCoy and Joseph Moraal ##

# Note enum requires python version 3.0 or greater
from enum import Enum
import random

def evalHand(hand):
    retval = 0
    left, middle, right = hand

    if left > middle:
        ++retval
    if middle > right:
        ++retval
    if left > right:
        ++retval

    return float(retval)

## version of deal with randomization.
def randDeal():
    cardList = [x for x in range(1, 8)]
    print(cardList)
    cards = []

    while len(cardList) > 0:
        index = random.randint(0, len(cardList) - 1)
        cards.append(cardList.pop(index))

    maxHand = (cards[0], cards[2], cards[4])
    minHand = (cards[1], cards[3], cards[5])
    return (maxHand, minHand, cards[6])

def deal():
    maxHand = (6, 3, 1)
    minHand = (7, 5, 2)
    return (maxHand, minHand, 4)

class Node:
    def __init__(self, maxHand, minHand, middleCard):
        self.maxHand = maxHand
        self.minHand = minHand
        self.middleCard = middleCard
        self.children = None

def genNodes_recursiveHelper(node, isMax, depth):
    if depth < 3:
        left, middle, right = (node.maxHand if isMax else node.minHand)

        leftSwap = (node.middleCard, middle, right)
        middleSwap = (left, node.middleCard, right)
        rightSwap = (left, middle, node.middleCard)

        maxHand = (leftSwap if isMax else node.maxHand)
        minHand = (node.minHand if isMax else leftSwap)
        leftChild = Node(maxHand, minHand, left)

        maxHand = (middleSwap if isMax else node.maxHand)
        minHand = (node.minHand if isMax else middleSwap)
        middleChild = Node(maxHand, minHand, middle)

        maxHand = (rightSwap if isMax else node.maxHand)
        minHand = (node.minHand if isMax else rightSwap)
        rightChild = Node(maxHand, minHand, right)

        leftChild = genNodes_recursiveHelper(leftChild, not isMax, depth + 1)
        middleChild = genNodes_recursiveHelper(middleChild, not isMax, depth + 1)
        rightChild = genNodes_recursiveHelper(rightChild, not isMax, depth + 1)

        node.children = (leftChild, middleChild, rightChild)

    return node

def genNodes(maxHand, minHand, middleCard):
    rootNode = Node(maxHand, minHand, middleCard)
    return genNodes_recursiveHelper(rootNode, True, 0)

def printLeaf(node, h, isPruned):
    prunedString = ("true" if isPruned else "false")
    minLeft, minMiddle, minRight = node.minHand
    maxLeft, maxMiddle, maxRight = node.maxHand
    values = (minLeft, minMiddle, minRight, node.middleCard, maxLeft, maxMiddle, maxRight, h, prunedString)
    print("(min = {%d, %d, %d}) (middle = %d) (max = {%d, %d, %d}) -> (h = %d) (pruned = %s)" % values)

def shouldPrune(h, parentH, isMax):
    if isMax and (h > parentH):
        return True
    elif not isMax and (h < parentH):
        return True

    return False

def pruneNodes_recursiveHelper(node, isMax, parentH, isPruned):
    h = evalHand(node.maxHand if isMax else node.minHand)

    if node.children:
        left, middle, right = node.children

        h = pruneNodes_recursiveHelper(left, not isMax, parentH, isPruned)
        pruneRemaining = shouldPrune(h, parentH, isMax)

        middleH = pruneNodes_recursiveHelper(middle, not isMax, h, pruneRemaining)
        if not pruneRemaining and ((isMax and h < middleH) or (not isMax and h > middleH)):
            h = middleH
            pruneRemaining = shouldPrune(h, parentH, isMax)

        rightH = pruneNodes_recursiveHelper(right, not isMax, h, pruneRemaining)
        if not pruneRemaining and ((isMax and h < rightH) or (not isMax and h > rightH)):
            h = rightH
    else:
        printLeaf(node, h, isPruned)

    return h

def pruneNodes(rootNode):
    return pruneNodes_recursiveHelper(rootNode, False, float("Inf"), False)

if __name__ == "__main__":
    maxHand, minHand, middleCard = deal()
    rootNode = genNodes(maxHand, minHand, middleCard)
    h = pruneNodes(rootNode)

    print ("Result: %d" % (h))
