import random

card_value_dictionary = {'Joker': 14, 'Ace': 13, 'King': 12, 'Queen': 11, 'Jack': 10, '10': 9, '9': 8, '8': 7, '7': 6,
                         '6': 5, '5': 4, '4': 3, '3': 2, '2': 1}

war_score = {'User Wins': 0, 'Computer Wins': 0, 'Games Played': 0}


def war_rules():

    print()

    print('Welcome to War! Be the first player to collect all 54 cards!')

    print()

    print('Each player will compare their first card in their hand with each other. The player with the highest value '
          'card wins and that player gets both cards put into their card pile.')

    print('If both cards are the same value then their is a WAR!')

    print('Once the WAR starts the two compared cards, along with the next three cards from each player\'s hand will '
          'be added to the WAR pile.')

    print('The two players will then compare their next card and the player with the highest value card wins the WAR '
          'and gets all of the cards in the WAR pile.')

    print('In the event that a player does not have enough cards for a WAR, the other player wins automatically.')

    print('If both players do not have enough cards for a WAR, then the player with the most cards wins.')

    print('Lastly, if both players have the same amount of cards and cannot have a WAR, the last card in the player '
          'hand is compared to the other player, with the highest value being the winner.')

    print('In the event of a tie in this case, the cards will all be shuffled and dealt out again.')

    print()

    print('Good luck!')

    print()

    input('Press "enter" to continue: ')

    print()


def create_deck():

    created_deck = []

    counter = 4

    card_suite = ['Ace', 'King', 'Queen', 'Jack', '10', '9', '8', '7', '6', '5', '4', '3', '2']

    jokers = ['Joker', 'Joker']

    while counter > 0:

        for card in card_suite:

            created_deck.append(card)

            if len(created_deck) % 13 == 0:

                counter -= 1

    for card in jokers:

        created_deck.append(card)

    return created_deck


def deck_shuffler(deck):

    shuffle_number = 0

    user_pick_shuffle = False

    random_shuffle = False

    while True:

        shuffle_choice = input('Type "0" to pick how many times the deck is shuffled or type "1" to have it shuffled '
                               'randomly: ')

        if shuffle_choice == '0':

            user_pick_shuffle = True

            break

        elif shuffle_choice == '1':

            random_shuffle = True

            break

        else:

            print('Please type either a "0" or a "1".')

            print()

    if user_pick_shuffle:

        while True:

            times_shuffled = input('Enter how many times to shuffle the deck: ')

            if times_shuffled.isdigit():

                if times_shuffled == '0':

                    print('Type in a number greater than 1.')

                    print()

                else:

                    shuffle_number = int(times_shuffled)

                    print('The deck will be shuffled {} time(s).'.format(shuffle_number))

                    print()

                    break

            else:

                print('Please enter a valid integer.')

                print()

    elif random_shuffle:

        shuffle_number = random.randint(1, 10)

        print('The deck will be shuffled {} time(s).'.format(shuffle_number))

        print()

    while shuffle_number > 0:

        random.shuffle(deck)

        shuffle_number -= 1

    input('Press "enter" to continue: ')

    print()

    return deck


def deck_dealer(deck):

    user_hand = deck[0::2]

    computer_hand = deck[1::2]

    return user_hand, computer_hand


def gameplay_function(user_hand, computer_hand):

    turn = 1

    user_card_pile = []

    computer_card_pile = []

    war_card_list = []

    war_card_shuffle = []

    while True:

        print('Turn: {}'.format(turn))

        print('-------------------------------------------------------------------------------------------------------')

        print()

        print('Computer Info:')

        print('Computer\'s Current Card: {}'.format(computer_hand[0]))

        print('Number of Cards in Computer\'s Pile: {}'.format(len(computer_card_pile)))

        print('Number of Cards in The Computer\'s Hand: {}'.format(len(computer_hand)))

        print()

        print('User Info:')

        print('Your Current Card: {}'.format(user_hand[0]))

        print('Number of Cards in Your Pile: {}'.format(len(user_card_pile)))

        print('Number of Cards in Your Hand: {}'.format(len(user_hand)))

        print()

        print('-------------------------------------------------------------------------------------------------------')

        # input('Press enter to continue: ')

        print()

        if card_value_dictionary[computer_hand[0]] < card_value_dictionary[user_hand[0]]:

            print('Your card has a higher value, so you get both cards.')

            print()

            user_card_pile.append(user_hand[0])

            user_hand.remove(user_hand[0])

            user_card_pile.append(computer_hand[0])

            computer_hand.remove(computer_hand[0])

            turn += 1

            # input('Press enter to continue: ')

            print()

        elif card_value_dictionary[computer_hand[0]] > card_value_dictionary[user_hand[0]]:

            print('The computer\'s card has a higher value, so it gets both cards.')

            print()

            computer_card_pile.append(user_hand[0])

            user_hand.remove(user_hand[0])

            computer_card_pile.append(computer_hand[0])

            computer_hand.remove(computer_hand[0])

            turn += 1

            # input('Press enter to continue: ')

            print()

        else:

            print('You and the computer have the same value card, so it\'s WAR!')

            print()

            print('The cards that were compared, along with three other cards from each players hand, will be put into '
                  'the war pile for the winner to collect.')

            print()

            # input('Press enter to continue: ')

            print()

            while True:

                war_counter = 3

                war_card_list.append(user_hand[0])

                user_hand.remove(user_hand[0])

                war_card_list.append(computer_hand[0])

                computer_hand.remove(computer_hand[0])

                if len(user_hand) == 0:

                    print('You ran out of cards!')

                    print('The cards in your card pile will be put into your hand and shuffled a random amount of '
                          'times.')

                    print()

                    for card in user_card_pile:

                        user_hand.append(card)

                    user_card_pile.clear()

                    shuffle_number = random.randint(1, 10)

                    print('Your new hand was shuffled {} time(s).'.format(shuffle_number))

                    while shuffle_number > 0:

                        random.shuffle(user_hand)

                        shuffle_number -= 1

                    print()

                    # input('Press enter to continue: ')

                    print()

                if len(computer_hand) == 0:

                    print('The computer ran out of cards!')

                    print('The cards in the computer\'s card pile will be put into its hand and shuffled a random '
                          'amount of times.')

                    print()

                    for card in computer_card_pile:

                        computer_hand.append(card)

                    computer_card_pile.clear()

                    shuffle_number = random.randint(1, 10)

                    print('The computer\'s new hand was shuffled {} time(s).'.format(shuffle_number))

                    while shuffle_number > 0:

                        random.shuffle(computer_hand)

                        shuffle_number -= 1

                    print()

                    # input('Press enter to continue: ')

                    print()

                if len(user_hand) < 4 and len(computer_hand) < 4:

                    print('You and the computer do not have enough cards for a WAR!')

                    print('So, I will determine who wins based on the number of cards in the hands.')

                    print()

                    if len(user_hand) < len(computer_hand):

                        print('The computer has more cards, so it wins automatically.')

                        print()

                        for card in user_hand:

                            computer_card_pile.append(card)

                        user_hand.clear()

                        for card in war_card_list:

                            computer_card_pile.append(card)

                        war_card_list.clear()

                        for card in computer_hand:

                            computer_card_pile.append(card)

                        computer_hand.clear()

                        break

                    elif len(user_hand) > len(computer_hand):

                        print('You have more cards than the computer, so you win automatically.')

                        print()

                        for card in computer_hand:

                            user_card_pile.append(card)

                        computer_hand.clear()

                        for card in war_card_list:

                            user_card_pile.append(card)

                        war_card_list.clear()

                        for card in user_hand:

                            user_card_pile.append(card)

                        user_hand.clear()

                        break

                    else:

                        print('You and the computer have the same amount of cards, so we will compare the last cards.')

                        print()

                        if card_value_dictionary[user_hand[-1]] > card_value_dictionary[computer_hand[-1]]:

                            print('Your last card has a higher value than the computer\'s, so you win the WAR!')

                            print()

                            for card in computer_hand:

                                user_card_pile.append(card)

                            computer_hand.clear()

                            for card in war_card_list:

                                user_card_pile.append(card)

                            war_card_list.clear()

                            for card in user_hand:

                                user_card_pile.append(card)

                            user_hand.clear()

                            break

                        elif card_value_dictionary[user_hand[-1]] < card_value_dictionary[computer_hand[-1]]:

                            print('The computer\'s last card has a higher value, so it wins the WAR!')

                            print()

                            for card in user_hand:

                                computer_card_pile.append(card)

                            user_hand.clear()

                            for card in war_card_list:

                                computer_card_pile.append(card)

                            war_card_list.clear()

                            for card in computer_hand:

                                computer_card_pile.append(card)

                            computer_hand.clear()

                            break

                        else:

                            print('Since the last cards also have the same value the cards will be shuffled and '
                                  'redistributed.')

                            print()

                            for card in user_hand:

                                war_card_shuffle.append(card)

                            user_hand.clear()

                            for card in computer_hand:

                                war_card_shuffle.append(card)

                            computer_hand.clear()

                            for card in war_card_list:

                                war_card_shuffle.append(card)

                            war_card_list.clear()

                            war_shuffle = random.randint(1, 10)

                            print('The cards will be shuffled {} time(s).'.format(war_shuffle))

                            print()

                            while war_shuffle > 0:

                                random.shuffle(war_card_shuffle)

                                war_shuffle -= 1

                            user_hand = war_card_shuffle[0::2]

                            computer_hand = war_card_shuffle[1::2]

                            war_card_shuffle.clear()

                            break

                elif len(user_hand) < 4:

                    print('You do not have enough cards for the war, so the computer wins automatically.')

                    print()

                    for card in user_hand:

                        computer_card_pile.append(card)

                    user_hand.clear()

                    for card in war_card_list:

                        computer_card_pile.append(card)

                    war_card_list.clear()

                    x = 3

                    while x > 0:

                        computer_card_pile.append(computer_hand[0])

                        computer_hand.pop(0)

                        x -= 1

                    break

                elif len(computer_hand) < 4:

                    print('The computer does not have enough cards for the war, so you win automatically.')

                    print()

                    for card in computer_hand:

                        user_card_pile.append(card)

                    computer_hand.clear()

                    for card in war_card_list:

                        user_card_pile.append(card)

                    war_card_list.clear()

                    x = 3

                    while x > 0:

                        user_card_pile.append(user_hand[0])

                        user_hand.pop(0)

                        x -= 1

                    break

                else:

                    while war_counter > 0:

                        war_card_list.append(user_hand[0])

                        user_hand.remove(user_hand[0])

                        war_card_list.append(computer_hand[0])

                        computer_hand.remove(computer_hand[0])

                        war_counter -= 1

                    print('User Current Card: {}'.format(user_hand[0]))

                    print('Computer Current Card: {}'.format(computer_hand[0]))

                    print()

                    if card_value_dictionary[computer_hand[0]] < card_value_dictionary[user_hand[0]]:

                        print('Your card has a higher value, so you win the WAR!')

                        print()

                        for card in war_card_list:

                            user_card_pile.append(card)

                        war_card_list.clear()

                        user_card_pile.append(user_hand[0])

                        user_hand.remove(user_hand[0])

                        user_card_pile.append(computer_hand[0])

                        computer_hand.remove(computer_hand[0])

                        break

                    elif card_value_dictionary[computer_hand[0]] > card_value_dictionary[user_hand[0]]:

                        print('The computer\'s card has a higher value, so it wins the WAR!')

                        print()

                        for card in war_card_list:

                            computer_card_pile.append(card)

                        war_card_list.clear()

                        computer_card_pile.append(user_hand[0])

                        user_hand.remove(user_hand[0])

                        computer_card_pile.append(computer_hand[0])

                        computer_hand.remove(computer_hand[0])

                        break

                    else:

                        print('You and the computer both have the same value card, so there is still a WAR!')

                        print()

                        print('The compared cards, along with three other cards from each player\'s hand, will be put '
                              'into the war pile.')

                        print()

            turn += 1

            # input('Press enter to continue: ')

            print()

        if len(user_card_pile) + len(user_hand) == 54:

            print('You got all of the cards! You WIN!')

            print()

            war_score['User Wins'] += 1

            war_score['Games Played'] += 1

            break

        if len(computer_card_pile) + len(computer_hand) == 54:

            print('The computer got all of the cards! The computer WINS!')

            print()

            war_score['Computer Wins'] += 1

            war_score['Games Played'] += 1

            break

        if len(user_hand) == 0:

            print('You ran out of cards!')

            print('The cards in your card pile will be put into your hand and shuffled a random amount of times.')

            print()

            for card in user_card_pile:

                user_hand.append(card)

            user_card_pile.clear()

            shuffle_number = random.randint(1, 10)

            print('Your new hand was shuffled {} time(s).'.format(shuffle_number))

            while shuffle_number > 0:

                random.shuffle(user_hand)

                shuffle_number -= 1

            print()

            # input('Press enter to continue: ')

            print()

        if len(computer_hand) == 0:

            print('The computer ran out of cards!')

            print('The cards in the computer\'s card pile will be put into its hand and shuffled a random amount of '
                  'times.')

            print()

            for card in computer_card_pile:

                computer_hand.append(card)

            computer_card_pile.clear()

            shuffle_number = random.randint(1, 10)

            print('The computer\'s new hand was shuffled {} time(s).'.format(shuffle_number))

            while shuffle_number > 0:

                random.shuffle(computer_hand)

                shuffle_number -= 1

            print()

            # input('Press enter to continue: ')

            print()


def war_replay():

    print('Here is the score: ')

    print(war_score)

    print()

    while True:

        replay = input('Would you like to play again? ("Yes"/"No"): ')

        if replay.upper() == 'YES':

            print('Okay, let\'s go again!')

            x = 60

            while x > 0:

                print()

                x -= 1

            break

        elif replay.upper() == 'NO':

            print('Okay, good game!')

            exit()

        else:

            print('Please type either "Yes" or "No".')

            print()


war_rules()


while True:

    total_deck = create_deck()

    shuffled_deck = deck_shuffler(total_deck)

    player_decks = deck_dealer(shuffled_deck)

    gameplay_function(player_decks[0], player_decks[1])

    war_replay()
    