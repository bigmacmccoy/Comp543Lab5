# Comp543Lab5
Comp 543 Intro to AI Lab 5

Problem Description:

	A new card game, Swap-N-Sort is sweeping the nation. It is a 2 player (MAX and MIN) card game played with only 7 cards, each labeled with a number between 1 and 7 (inclusive). 
	In general
	•	Setup:  Each player is dealt 3 cards face up, and the seventh is placed in the center. 
	•	Objective: To be the first player whose 3 cards are arranged in increasing numerical order
	•	Play: The game is played in turns; on each turn a player selects a card to trade with the card in the center. 
	•	Result: If the MAX player wins the result is +1 and if the MIN player wins the result is -1.
	•	Evaluation function: Evaluate non-terminal game states.
		o	Initialize h=0. 
		o	Now consider MIN’s hand. Look at each pair of cards and add 1 to h for each pair that is not in increasing order. For example, if MIN’s hand is 4, 1, 2 then we add 2 to h because 4 > 1 and 4 > 2, but 1 < 2.  
		o	Next consider MAX’s hand. Subtract 1 from h for each pair that is not in increasing order. For example, if MIN’s hand is 4, 1, 2 and MAX’s hand is 3, 7, 6 then h = +1. 

ALPHA-BETA pruning applied to game instance
	•	Deal of the cards gives MIN a hand of 7, 5, 2 and MAX a hand of 6, 3, 1, with 4 in the center. 
	•	MAX will go first
	•	Perform ALPHA-BETA pruning on the tree that is obtained by cutting off after 3 steps (MAX, MIN, MAX). 
	•	You should explore the actions in the following order:
		o	Trade the leftmost card for the center
		o	Trade the middle for the center
		o	Trade the rightmost for the center. 
	•	For each leaf node (27 in all) report
		o	hand of each player 
		o	Value of h
		o	If it is not pruned
				The alpha and beta values at the leaf node, its parent, grandparent and great-grandparent (root) after that leaf is evaluated.
		o	If the node is pruned
				Write “pruned” instead of these values
