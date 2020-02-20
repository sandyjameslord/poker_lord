"""This application is a 5-card stud game. It creates a deck, determines the players and deals the cards.
It then evaluates the different hands against each other and determines a winner.
Ties are possible if the face of the winner is the same amongst players."""

import random
FACES = ["Deuce", "Three", "Four ", "Five ", "Six  ", "Seven", "Eight", "Nine ", "Ten  ", "Jack ", "Queen", "King ", "Ace  "]
SUITS = ['Hearts  ', 'Diamonds', 'Clubs   ', 'Spades  ']
VALUES = ['High Card', 'Pair', 'Two Pair', 'Three of a Kind', 'Straight', 'Flush', 'Full House', 'Four of a Kind', 'Straight Flush']
NAMES = ["Kate the Computer  ", "Izzy the Informator", "Chicken the Clicker", "Evie the Evaluator ", "Drew the Drawer    "]
def is_high_card(hand):
	"""Determines and returns if the hand has a high card and what face it is."""
	is_a_high_card = True
	i = 0
	while i < 13:
		if hand[i] > 1:
			is_high_card = False
		i += 1
		
	high_card = 0
	j = 0
	while j < 13 and is_a_high_card == True:
		if hand[j] == 1 and j >= high_card:
			high_card = j
		j += 1
	if is_a_high_card:
		return True, high_card
	else:
		return False 
def is_pair(hand):
	"""Determines and returns if the hand has a pair and what face it is."""
	is_a_pair = False
	i = 0
	while i < 13:
		if hand[i] == 2:
			is_a_pair = True
		i += 1 
	high_card = 0
	j = 0
	while j < 13 and is_a_pair == True:
		if hand[j] == 2 and j >= high_card:
			high_card = j
		j += 1
	if is_a_pair:
		return True, high_card
	else:
		return False
def is_two_pair(hand):
	"""Determines and returns if the hand has a high card and what face is the higher pair."""
	faces_of_pairs = []
	is_a_two_pair = False
	i = 0
	while i < 13:
		if hand[i] == 2:
			faces_of_pairs.append(i)
		i += 1
	if len(faces_of_pairs) == 2:
		is_a_two_pair = True
	for fp in faces_of_pairs:
		print(fp)
	if is_a_two_pair:
		return True, faces_of_pairs[1]
	else:
		return False
def is_three_of_a_kind(hand):
	"""Determines and returns if the hand has a three of a kind and what face it is."""
	is_a_three_of_a_kind = False
	i = 0
	while i < 13:
		if hand[i] == 3:
			is_a_three_of_a_kind = True
		i += 1 
		
	high_card = 0
	j = 0
	while j < 13 and is_a_three_of_a_kind == True:
		if hand[j] == 3 and j >= high_card:
			high_card = j
		j += 1
	if is_a_three_of_a_kind:
		return True, high_card
	else:
		return False 
def is_straight(hand):
	"""Determines and returns if the hand has a straight and what face is its highest member."""
	i = 0
	while i < 8:
		if hand[i] == 1 and hand[i+1] == 1 and hand[i+2] == 1 and hand[i+3] == 1 and hand[i+4] == 1:
			return True, i + 4
		i += 1
	return False
def is_flush(hand):
	"""Determines and returns if the hand has a flush and what its highest face is."""
	is_a_flush = False
	i = 16
	while i >= 13:
		if hand[i] == 5:
			is_a_flush = True
		i -= 1
    
	high_card = 0
	j = 0
	while j < 13 and is_a_flush == True:
		if hand[j] == 1 and j >= high_card:
			high_card = j
		j += 1
	if is_a_flush:
		return True, high_card
	else:
		return False  
def is_full_house(hand):
	"""Determines and returns if the hand has a full house and what face is highest."""
	is_a_full_house = False
	num_three_kind = 0
	num_pair = 0
	i = 0
	while i < 13:
		if hand[i] == 3:
			num_three_kind += 1
		elif hand[i] == 2:
			num_pair += 1
		i += 1
	if num_three_kind ==1 and num_pair == 1:
		is_a_full_house = True
	
	high_card = 0
	j = 0
	while j < 13 and is_a_full_house == True:
		if (hand[j] == 2 or hand[j] == 3) and j >= high_card:
			high_card = j
		j += 1
	if is_a_full_house:
		return True, high_card
	else:
		return False 
def is_four_of_a_kind(hand):
	"""Determines and returns if the hand has a four of a kind and what face it is."""
	is_a_four_of_a_kind = False
	i = 0
	while i < 13:
		if hand[i] == 4:
			is_a_four_of_a_kind = True
		i += 1 
		
	high_card = 0
	j = 0
	while j < 13 and is_a_four_of_a_kind == True:
		if hand[j] == 4 and j >= high_card:
			high_card = j
		j += 1
	if is_a_four_of_a_kind:
		return True, high_card
	else:
		return False 
def is_straight_flush(hand):
	"""Determines and returns if the hand has a straight flush and what face its highest member is."""
	is_a_local_flush = False
	is_a_local_straight = False
	local_high_card = 0
	i = 16
	while i >= 13:
		if hand[i] == 5:
			is_a_local_flush = True
		i -= 1
	if is_a_local_flush:
		j = 0
		while j < 8:
			if hand[j] == 1 and hand[j + 1] == 1 and hand[j + 2] == 1 and hand[j + 3] == 1 and hand[j + 4] == 1:
				is_a_local_straight = True
				local_high_card = j + 4
			j += 1
	if is_a_local_flush and is_a_local_straight:
		return True, local_high_card
	return False

def determine_game_type():
	"""Asks the user what kind of game to play. One game automatically generates 5 computer players, the other game allows
for user input on the number and names of the players."""
	kind_of_game = int(input("""There are two games:
Would you like to choose the number of total players, the number of human players, and the humans' names? (type 1)
Or would you like to see some quick play with 5 computer players? (type 1)
What'll it be, (1) or (2)?
"""))
	while kind_of_game != 1 and kind_of_game != 2:
		kind_of_game = int(input("""What'll it be, (1) or (2)?"""))
	if kind_of_game == 1:
		names = get_game_ready()
	else:
		names = NAMES
	return names
def get_game_ready():
	"""If the user elects to control the numbers and names of the players, they do so using this method.
Returns the names of players"""
	num_players = int(input("""How many players will be playing today? (between 2 and 5):  """))
	while num_players > 5 or num_players < 2:
		num_players = int(input("""Between 2 and 5 players please:  """))
	num_number_of_people = int(input("""How many of these players will be humans?:  """))
	while num_number_of_people > num_players or num_number_of_people < 0:
		num_number_of_people = int(input(f"""Please enter a number equal to or less than the number of players ({num_players}):  """))
	num_people = num_number_of_people
	while num_people > 0:
		NAMES[abs(num_people - num_number_of_people)] = input(f"""Name of player {abs(num_people - num_number_of_people)+1}:  """)
		num_people -= 1
	while len(NAMES) > num_players:
		NAMES.pop()
	return NAMES
def make_hands(names):
	"""This method creates a new deck, shuffles it, and deals 5 cards to each player.
Returns the hands."""
	deck = []
	for face in FACES:
		for suit in SUITS:
			deck.append([face, suit])
	random.shuffle(deck)
	dealt = 0
	player = 0
	hands = []
	while dealt < (len(names)*5):
		hand = []
		i = 0
		while i < 5:
			hand.append(deck.pop())
			i += 1
		dealt += 5
		player += 1
		hands.append(hand)
	return hands
def determine_what_is_in_a_hand(hand):
	"""This method organizes the hand into higher level components, such as the number of each card and the number of each suit in the hand.
Returns an array of these components."""
	face_organization = [0,0,0,0,0,0,0,0,0,0,0,0,0] # deuce, three, four, five, six, seven, eight, nine, ten, jack, queen, king, ace
	suit_organization = [0,0,0,0] #spades, diamonds, hearts, clubs
	for face, suit in hand:
		i = 0
		while i < len(FACES):
			if face.startswith(FACES[i]):
				face_organization[i] += 1
			i += 1
		j = 0
		while j < len(SUITS):
			if suit.startswith(SUITS[j]):
				suit_organization[j] += 1
			j += 1
	hand_organization = face_organization + suit_organization
	return hand_organization
def determine_hand_value(hand):
	"""This method determines the value of a hand from amongst the possible VALUES.
Returns an array of booleans and the high card involved."""
	hand_value = [False, False, False, False, False, False, False, False, False]	
	value = is_straight_flush(hand)
	if value:
		hand_value[8] = True
		return hand_value, value[1]
	value = is_four_of_a_kind(hand)
	if value:
		hand_value[7] = True
		return hand_value, value[1]
	value = is_full_house(hand)
	if value:
		hand_value[6] = True
		return hand_value, value[1]
	value = is_flush(hand)
	if value:
		hand_value[5] = True
		return hand_value, value[1]
	value = is_straight(hand)
	if value:
		hand_value[4] = True
		return hand_value, value[1]
	value = is_three_of_a_kind(hand)
	if value:
		hand_value[3] = True
		return hand_value, value[1]
	value = is_two_pair(hand)
	if value:
		hand_value[2] = True
		return hand_value, value[1]
	value = is_pair(hand)
	if value:
		hand_value[1] = True
		return hand_value, value[1]
	value = is_high_card(hand)
	if value:
		hand_value[0] = True
		return hand_value, value[1]
def compare_hand_values(hand_values):
	"""Compares the relative strength of each hand.
Returns the best hand, the best card involved, and a list of the hands that match the best (for a tie)."""
	high_hand = 0
	high_card_involved = 0
	high_hands = []
	for idx, value in enumerate(hand_values):
		print("value: ", value)
		i = 0
		while i < 9:
			if value[0][i] and i >= high_hand:
				if i > high_hand:
					high_hands.clear()
					high_hands.append(idx)
				else:
					high_hands.append(idx)
				high_hand = i
			i += 1
	for player in high_hands:
		for idx, value in enumerate(hand_values):
			if player == idx:
				if value[1] >= high_card_involved:
					high_card_involved = value[1]
	return high_hand, high_card_involved, high_hands

def main():
	"""This function runs all other methods and displays the results."""
	print("""Welcome to 5 Card Stud!""")
	names = determine_game_type()
	hands = make_hands(names)
	values = []
	for hand in hands:
		value = determine_what_is_in_a_hand(hand)
		values.append(value)
	hand_values = []
	for hand in values:
		hand_value = determine_hand_value(hand)
		hand_values.append(hand_value)
	high_hand, high_card_involved, high_hands = compare_hand_values(hand_values)
	print(f"\nHere are the hands for this game:\n")
	for id, hand in enumerate(hands):
		print(f"{NAMES[id]} : {hand}")
	print()
	print("high_hand: ", VALUES[high_hand], "    high_card_involved: ", FACES[high_card_involved])
	print()
	for idx, value in enumerate(hand_values):
		if value[0][high_hand] and value[1] == high_card_involved:
			print(f"{(NAMES[idx]).strip()} is the big winner with a {(VALUES[high_hand]).strip()}, {(FACES[high_card_involved]).strip()}s high")

print(help)
main()

