#Jacob Wright
#Week 5 Assignment
#GameofWar_v.3
#Collaborated with Daniel McMurry, Marissa Gross, Evan Sauers

import random	

def main():
	"""
	Deck, PlayerAHand and PlayerBHand are all lists
	"""
	
	Deck = []
	PlayerAHand = []
	PlayerBHand = []
	gameCounter = 0

	# Create deck.  Cards are represented by an integer value
	for i in range(52):
		Deck.append(i)
	
	# Shuffle the deck
	random.shuffle(Deck)
	
	# Deal 1/2 the cards to each player
	for x in range(26):
		PlayerAHand.append(Deck.pop())
		PlayerBHand.append(Deck.pop())
	
	# Main Gameplay
		
	while len(PlayerAHand) > 0 and len(PlayerBHand) > 0:
		gameCounter += 1
		PlayerAHand, PlayerBHand = playRound(PlayerAHand, PlayerBHand)
		if gameCounter > 1000:
			print("Game is a draw")
			break
	      
	      
	# End of game
	
	print("There were ", gameCounter, " rounds played")
	print("Player A has " + str(len(PlayerAHand)) + " cards, Player B has " + str(len(PlayerBHand)))
	
def playRound(PlayerA, PlayerB):
	Acard = PlayerA.pop()
	Bcard = PlayerB.pop()
	
	rankA = getRank(Acard)
	rankB = getRank(Bcard)
	
	if rankA > rankB:
    
      #A wins the round
		PlayerA.insert(0,Acard)
		PlayerA.insert(0,Bcard)
	elif rankB > rankA:
    	
      #B wins the round
		PlayerB.insert(0,Bcard)
		PlayerB.insert(0,Acard)
	
	else:
		PlayerA, PlayerB = WAR(PlayerA, PlayerB)
	
	return PlayerA, PlayerB


def WAR(PlayerA, PlayerB):
	print("War")
	
	Astack = []
	Bstack = []
	
	if len(PlayerA) > 4 and len(PlayerB) > 4:
		
	#pull 4 cards out
	  for x in range(4):
	    Astack.append(PlayerA.pop())
	    Bstack.append(PlayerB.pop())
	    
	  if getRank(Astack[3]) > getRank(Bstack[3]):
	  	
	  #a winsall
	  
	    PlayerA = Astack = Bstack = PlayerA
	    
	  elif getRank(Bstack[3]) > getRank(Astack[3]):
	  #b wins all
	  
	    PlayerB= Bstack = Astack = PlayerB
	    
	  else:
	  	  #in case of another War, everyone lose
	  	  
	  	  pass


	return PlayerA, PlayerB

	
def getRank(anyCard):
	return anyCard % 13


if __name__ == '__main__':
	main()

