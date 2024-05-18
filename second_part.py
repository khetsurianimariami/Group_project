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