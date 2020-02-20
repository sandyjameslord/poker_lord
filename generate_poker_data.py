import poker_automate
def generate_poker_data():
    tied = 0
    p1_wins = 0
    p2_wins = 0
    p3_wins = 0
    p4_wins = 0
    p5_wins = 0
    high_card_wins = 0
    pair_wins = 0
    two_pair_wins = 0
    three_of_a_kind_wins = 0
    straight_wins = 0
    flush_wins = 0
    full_house_wins = 0
    four_of_a_kind_wins = 0
    straight_flush_wins = 0
    num_times = int(input("How many times would you like to run the program? (Takes 42 minutes to run 10,000,000 times):"))
    for i in range(num_times):
        data = poker_automate.main()
        print(data)
        if data[0] == "t":
            tied += 1
        if data[1] == "1":
            p1_wins += 1
        if data[1] == "2":
            p2_wins += 1
        if data[1] == "3":
            p3_wins += 1
        if data[1] == "4":
            p4_wins += 1
        if data[1] == "5":
            p5_wins += 1
        if "Two Pair" in data:
            two_pair_wins += 1
        if "Three of a Kind" in data:
            three_of_a_kind_wins += 1
        if "Straight" in data and "Straight Flush" not in data:
            straight_wins += 1
        if "Straight Flush" in data:
            straight_flush_wins += 1
        if "Flush" in data and "Straight Flush" not in data:
            flush_wins += 1
        if "Pair" in data and "Two Pair" not in data:
            pair_wins += 1
        if "Full House" in data:
            full_house_wins += 1
        if "Four of a Kind" in data:
            four_of_a_kind_wins += 1
        if "High Card" in data:
            high_card_wins += 1
    return [tied, p1_wins, p2_wins, p3_wins, p4_wins, p5_wins, high_card_wins, pair_wins, two_pair_wins, three_of_a_kind_wins, straight_wins, flush_wins, full_house_wins, four_of_a_kind_wins, straight_flush_wins]
