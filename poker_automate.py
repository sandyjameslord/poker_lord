import random
FACES = ["Deuce", "Three", "Four ", "Five ", "Six  ", "Seven", "Eight", "Nine ", "Ten  ", "Jack ", "Queen", "King ", "Ace  "]
SUITS = ['Hearts  ', 'Diamonds', 'Clubs   ', 'Spades  ']
VALUES = ['High Card', 'Pair', 'Two Pair', 'Three of a Kind', 'Straight', 'Flush', 'Full House', 'Four of a Kind', 'Straight Flush']
NAMES = ["P1", "P2", "P3", "P4", "P5"]
def is_high_card(hand):
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
	faces_of_pairs = []
	is_a_two_pair = False
	i = 0
	while i < 13:
		if hand[i] == 2:
			faces_of_pairs.append(i)
		i += 1
	if len(faces_of_pairs) == 2:
		is_a_two_pair = True
	if is_a_two_pair:
		return True, faces_of_pairs[1]
	else:
		return False
def is_three_of_a_kind(hand):
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
	i = 0
	while i < 8:
		if hand[i] == 1 and hand[i+1] == 1 and hand[i+2] == 1 and hand[i+3] == 1 and hand[i+4] == 1:
			return True, i + 4
		i += 1
	return False
def is_flush(hand):
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

def make_hands(NAMES):
	deck = []
	for face in FACES:
		for suit in SUITS:
			deck.append([face, suit])
	random.shuffle(deck)
	dealt = 0
	player = 0
	hands = []
	while dealt < (len(NAMES)*5):
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

def main():
	names = NAMES
	hands = make_hands(names)
	values = []
	for hand in hands:
		value = determine_what_is_in_a_hand(hand)
		values.append(value)
	hand_values = []
	for hand in values:
		hand_value = determine_hand_value(hand)
		hand_values.append(hand_value)
	high_hand = 0
	high_card_involved = 0
	high_hands = []
	for idx, value in enumerate(hand_values):
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
	ties = 0
	for idx, value in enumerate(hand_values):
		if value[0][high_hand] and value[1] == high_card_involved:
			ties += 1
	if ties >= 2:
		return f"tied {VALUES[high_hand]}"
	else:
		for idx, value in enumerate(hand_values):
			if value[0][high_hand] and value[1] == high_card_involved:
				return f"{NAMES[idx]} {VALUES[high_hand]}"

