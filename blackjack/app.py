'''
Rules of black jack

Press 1 to play 
Press 2 to ask for card 
Press 3 to stop

Press esc to leave the game 

the goal is to have 21 blackjck by summing 2+ cards
A can value 1 or 11
K , Q , J value 10
1,2,3,4,5,6,7,8,9,10 value the same number printed on the card 
If the player goes beyond 21 the game goes to the house 
If the house has 17 directly cannot ask cards 
If the house has under 17 can ask card to reach 21 
If the house goes beyond 21 the game goes to the player

The first card of the delar is faceup and the second one facedown 
The cards of the player are all face up

If the player has to same value card can split and play two differnt hands 

'''
# imports the randomrange function
from random import randrange

# this generate the cards of the player and the dealer
def get_cards(list_of_cards):
    cards = []
    for i in range(2):
        cards.append([card for card in list_of_cards[randrange(len(list_of_cards))]])
    return (cards)



list_of_cards = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
cards_of_the_dealer = get_cards(list_of_cards)
cards_of_the_player = get_cards(list_of_cards)


print(cards_of_the_dealer, cards_of_the_player)
