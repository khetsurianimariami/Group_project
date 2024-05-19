import random

# შევქმენით კარტის 4 დასტა
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
colors = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
scores = {'J': 11, 'Q': 12, 'K': 13, 'A': 20}

deck = []
for rank in ranks:
    for color in colors:
        deck.append((rank, color))
deck = deck * 4
random.shuffle(deck)


def deal_cards(num_cards):
    # დავურიგეთ მოთამაშეს კარტები
    cards = []
    for _ in range(num_cards):
        card = deck.pop()
        cards.append(card)
    return cards


def calculate_score(player_cards):
    # დავთვალეთ ჯამი
    score = 0
    for j in player_cards:
        if j[0] in scores.keys():
            score += scores[j[0]]
        else:
            score += int(j[0])
    return score


def change_card(player_cards, card_index, deck):
    # შვუცვალოთ მოთამაშეს ერთი სასურველი კარტი
    player_cards[card_index] = deck.pop()
    return player_cards


def card_change_handler(players_cards_dict):
    # ვკითხოთ თუ სურს შეცვლა და რომლის შეცვლა სურს
    for player_name in players_cards_dict:
        while True:
            is_change_need = input(f"{player_name} would you like to change card (y/n): ").lower()
            if is_change_need in ("n", "y"):
                break
            print("Please enter 'y' or 'n'")
            continue

        if is_change_need == "n":
            break

        while True:
            card_index = int(input(f"{player_name} which card index do you want to change? [0-4]: "))
            try:
                players_cards_dict[player_name] = change_card(players_cards_dict[player_name], card_index, deck)
                break
            except IndexError:
                print("You entered a wrong index!!! ")
                continue

    return players_cards_dict

def count_colors(cards_lst):
    # ვთვლით ერთსა და იმავე ფერებს
    color_count_dict = {'Clubs': 0, 'Spades': 0, 'Diamonds': 0, 'Hearts': 0}
    for rank, color in cards_lst:
        color_count_dict[color] += 1
    max_color_count = max(color_count_dict.values())
    return max_color_count


def winner_of_colors(players_cards_dict):
    # ვავლენთ ფერებით გამარჯვებულებს
    players_cards_color_dict = {}
    for player_name, player_cards in players_cards_dict.items():
        players_cards_color_dict[player_name] = count_colors(player_cards)

    min_score = min(players_cards_color_dict.values())
    num_min_score = list(players_cards_color_dict.values()).count(min_score)

    if num_min_score == 1:
        winners_lst = []
        for player_name in players_cards_dict:
            if players_cards_dict[player_name] == min_score:
                continue
            winners_lst.append(player_name)
        return winners_lst

    return list(players_cards_dict.keys())


def count_ranks(cards_lst):
    # ვთვლით ერთსა და იმავე კარტებს
    ranks_count_dict = {rank: 0 for rank in ranks}
    for rank, color in cards_lst:
        ranks_count_dict[color] += 1
    max_rank_count = max(ranks_count_dict.values())
    return max_rank_count


def winner_of_ranks(players_cards_dict):
    # ვავლენთ რანკებით გამარჯვებულებს
    players_cards_rank_dict = {}
    for player_name, player_cards in players_cards_dict.items():
        players_cards_rank_dict[player_name] = count_ranks(player_cards)

    min_score = min(players_cards_rank_dict.values())
    num_min_score = list(players_cards_rank_dict.values()).count(min_score)

    if num_min_score == 1:
        winners_lst = []
        for player_name in players_cards_dict:
            if players_cards_dict[player_name] == min_score:
                continue
            winners_lst.append(player_name)
        return winners_lst

    return list(players_cards_dict.keys())


def find_winner(players_cards_dict):
    # ვიპოვოთ გამარჯვებული
    players_score_dict = dict()
    for player_name, player_cards in players_cards_dict.items():
        players_score_dict[player_name] = calculate_score(player_cards)

    min_score = min(players_score_dict.values())
    num_min_score = list(players_score_dict.values()).count(min_score)

    if num_min_score == 1:
        winners_lst = []
        for player_name in players_score_dict:
            if players_score_dict[player_name] == min_score:
                continue
            winners_lst.append(player_name)
        return winners_lst

    colors_winners = winner_of_colors(players_cards_dict)
    if colors_winners == 2:
        return colors_winners

    ranks_winners = winner_of_ranks(players_cards_dict)
    return ranks_winners


def print_player_cards(players_cards_dict):
    # დავბეჭდოთ მოთამაშეთა კარტები
    for player_name, player_cards in players_cards_dict.items():
        print(player_name, player_cards)


def generate_cards(player_names, num_cards):
    # კარტების დარიგება, ეკითხება შეცვლაზე და თუ სურთ უცვლის კარტს
    players_cards_dict = {}
    for name in player_names:
        players_cards_dict[name] = deal_cards(num_cards)

    print_player_cards(players_cards_dict)

    card_change_handler(players_cards_dict)
    print_player_cards(players_cards_dict)

    return players_cards_dict


def get_unique_name(entered_names, message):
    while True:
        name = input(message)
        if name in entered_names:
            print("Enter a valid name. This name has already been used.")
        else:
            return name


def main():
    num_cards = 5

    entered_names = set()

    name_1 = get_unique_name(entered_names, "Please input players number 1: ")
    entered_names.add(name_1)
    name_2 = get_unique_name(entered_names, "Please input players number 2: ")
    entered_names.add(name_2)
    name_3 = get_unique_name(entered_names, "Please input players number 3: ")
    entered_names.add(name_3)

    players_cards_dict = generate_cards([name_1, name_2, name_3], num_cards)

    winners = find_winner(players_cards_dict)

    # ვატრიალებთ ციკლს ერთი გამარჯვებულის პოვნამდე
    while len(winners) != 1:
        print("Next round")
        players_cards_dict = generate_cards(winners, num_cards)

        winners = find_winner(players_cards_dict)

    print(f"Winner is {winners[0]}")


if __name__ == "__main__":
    main()
