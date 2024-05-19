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


