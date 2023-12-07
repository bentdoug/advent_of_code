from collections import Counter

card_strength = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]

five_kind_ranking = []
four_kind_ranking = []
full_house_ranking = []
three_kind_ranking = []
two_pair_ranking = []
one_pair_ranking = []
high_card_ranking = []
ranking = []

input_file = open("Advent_of_Code\day_7_input.txt", "r")
lines = input_file.readlines()

for line in lines:
    split = line.split(" ")
    hand = split[0]
    bid = split[1]
    new_hand = list(hand)

    char_ct = Counter(hand)
    max_repeats = max(char_ct.values())
    
    if "J" in hand:
        options = []
        new_hand = []
        for key, value in char_ct.items():
            if value == max_repeats:
                options.append(key)
        values = [card_strength.index(x) for x in options]
        make_J_this = card_strength[max(values)]
        
        for char in hand:
            if char != "J":
                new_hand.append(char)
            else:
                new_hand.append(make_J_this)
        print(hand, options, values, make_J_this, new_hand)
        char_ct = Counter(new_hand)
        max_repeats = max(char_ct.values())
    print(max_repeats)
    res = [card_strength.index(x) for x in hand]
    res.append(bid)

    if max_repeats == 5:
        five_kind_ranking.append(res)
    elif max_repeats == 4:
        four_kind_ranking.append(res)
    elif max_repeats == 3 and 2 in char_ct.values():
        full_house_ranking.append(res)
    elif max_repeats == 3:
        three_kind_ranking.append(res)
    elif max_repeats == 2 and list(char_ct.values()).count(2) == 2:
        two_pair_ranking.append(res)
    elif max_repeats == 2:
        one_pair_ranking.append(res)
    else:
        high_card_ranking.append(res)

five_kind_ranking = (sorted(five_kind_ranking, key=lambda x:(x[0], x[1], x[2], x[3], x[4])))
four_kind_ranking = (sorted(four_kind_ranking, key=lambda x:(x[0], x[1], x[2], x[3], x[4])))
full_house_ranking = (sorted(full_house_ranking, key=lambda x:(x[0], x[1], x[2], x[3], x[4])))
three_kind_ranking = (sorted(three_kind_ranking, key=lambda x:(x[0], x[1], x[2], x[3], x[4])))
two_pair_ranking = (sorted(two_pair_ranking, key=lambda x:(x[0], x[1], x[2], x[3], x[4])))
one_pair_ranking = (sorted(one_pair_ranking, key=lambda x:(x[0], x[1], x[2], x[3], x[4])))
high_card_ranking = (sorted(high_card_ranking, key=lambda x:(x[0], x[1], x[2], x[3], x[4])))


ranking = high_card_ranking + one_pair_ranking + two_pair_ranking + three_kind_ranking + full_house_ranking + four_kind_ranking + five_kind_ranking
total = 0
for x in range(len(ranking)):
    total += int(ranking[x][5])*(x+1)
print(total)