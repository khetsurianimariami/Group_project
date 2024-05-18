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


def main():
    num_cards = 5
    name_1 = input("Please input players number 1: ")
    name_2 = input("Please input players number 2: ")
    name_3 = input("Please input players number 3: ")

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