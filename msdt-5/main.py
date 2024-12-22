import random
import blackjack_art


def get_player_card(hand):
    updated_hand = hand
    player_next_card = random.choice(list(deck.keys()))
    updated_hand.append(player_next_card)
    display_cards(player_next_card)
    return updated_hand


def get_computer_card(hand):
    updated_hand = hand
    computer_next_card = random.choice(list(deck.keys()))
    updated_hand.append(computer_next_card)
    display_cards(computer_next_card)
    return updated_hand


def get_answer(action):
    user_answer = "p"
    while user_answer not in "yn":
        user_answer = input(f"Type 'y' if you want {action} "
                         "or 'n' to pass. ").lower()
    return user_answer


def get_another_card(total_score, cards_in_hand):
    while total_score < 22:
        answer = get_answer(action="another card")
        if answer == "y":
            get_player_card(cards_in_hand)
            total_score = current_score(cards_in_hand)
            print_score("Your", total_score)
        else:
            break

    if total_score == 21:
        print("You are very lucky today!")
    return total_score


def display_cards(card):
    if card == "ace":
        print(blackjack_art.ace)
    elif card == "two":
        print(blackjack_art.two)
    elif card == "three":
        print(blackjack_art.three)
    elif card == "four":
        print(blackjack_art.four)
    elif card == "five":
        print(blackjack_art.five)
    elif card == "six":
        print(blackjack_art.six)
    elif card == "seven":
        print(blackjack_art.seven)
    elif card == "eight":
        print(blackjack_art.eight)
    elif card == "nine":
        print(blackjack_art.nine)
    elif card == "ten":
        print(blackjack_art.ten)
    elif card == "jack":
        print(blackjack_art.jack)
    elif card == "queen":
        print(blackjack_art.queen)
    elif card == "king":
        print(blackjack_art.king)


def current_score(hand):
    """Calculate the total score of all cards in the list.

        Only one ace can have the value 11, and this will be reduced
        to 1 if the hand bust.
        """
    score = 0
    one = False
    for card in hand:
        if card == "ace" and not one:
            one = True
            score += 11
        else:
            score += deck[card]

        # If bust, check if there is an ace and subtract 10
        if score > 21 and one:
            score -= 10
            one = False
    return score


def print_score(who, score):
    print(f"{who} score is {score}")


def who_wins(hand, computer, player):
    updated_score = computer
    while 22 > player > updated_score and updated_score < 17:
        current_hand = get_computer_card(hand)
        updated_score = current_score(current_hand)
        if updated_score > 21:
            break

    if player > 21:
        print("Computer wins")
        print_score("Computer", updated_score)
    elif updated_score > 21:
        print("You win!")
        print_score("Computer", updated_score)
    elif 22 > updated_score > player:
        print("Computer wins")
        print_score("Computer", updated_score)
    elif 22 > player > updated_score:
        print("You win!")
        print_score("Computer", updated_score)
    else:
        print("Draw!")
        print_score("Computer", updated_score)


def new_game(playing):
    computer_hand = []
    player_hand = []
    player_score = 0
    computer_score = 0
    # debuging variable
    # print(playing)
    if playing == 'y':
        print(blackjack_art.logo)

        # select player first cards
        player_hand = get_player_card(player_hand)
        player_hand = get_player_card(player_hand)
        player_score = current_score(player_hand)
        print_score("Your", player_score)

        # select computer first card
        computer_hand = get_computer_card(computer_hand)
        computer_score = current_score(computer_hand)
        print_score("Computer", computer_score)

        # get another card?
        player_score = get_another_card(player_score, player_hand)

        who_wins(computer_hand, computer_score,
                 player_score)
        new_game(playing=get_answer(action="to play"))
    else:
        print("Closing program.")


# card deck
deck = {
    'ace': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10,
    'jack': 10,
    'queen': 10,
    'king': 10,
}

if __name__ == "__main__":
    new_game(playing=get_answer(action="to play"))