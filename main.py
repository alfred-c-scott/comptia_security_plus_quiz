#!/usr/bin/python3
import json
import random
import math

JSON_DIR = 'json/'


# returns formatted fixed length titles for the terminal
def make_banner(message):
    banner_len = 78
    mess_len = len(message)
    banner_diff = banner_len - mess_len
    ct = 0
    dashes = ''
    while ct < banner_diff/2:
        dashes = dashes+'-'
        ct += 1
    message = dashes+message+dashes
    if len(message) > banner_len:
        return message[:len(message)-1]
    else:
        return message


# receives a string as a parameter and returns boolean if
# if string is an integer
def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()


def make_quiz_list(deck_name, length):
    with open(JSON_DIR+'flash.json', 'r') as f:
        flash_dict = json.load(f)

    # list of all cards in deck
    all_cards = flash_dict[deck_name]
    # list of all cards where score is less that 75%
    review_cards = []
    # list of all cards that have not been used in prior exam
    new_cards = []
    # list of all cards that have passing score
    passing_cards = []

    # parses all_cards and separates them into categorical lists
    for card in all_cards:
        if card['attempts'] != 0:
            percent = (card['attempts'] - card['misses'])/card['attempts']
            if percent < 0.75:
                review_cards.append(card.copy())
            else:
                passing_cards.append(card.copy())
        else:
            new_cards.append(card.copy())

    random.shuffle(review_cards)
    random.shuffle(new_cards)
    random.shuffle(passing_cards)

    review_percent = 0.3
    passing_percent = 0.1
    new_percent = 1 - review_percent - passing_percent
    quiz_list = []

    print(f'New        {new_percent}\n'
          f'Review     {review_percent}\n'
          f'Passing    {passing_percent}\n\n'
          f'Sum        {math.ceil(new_percent+review_percent+passing_percent)}')

    return quiz_list


def flash_quiz():
    # print(make_banner('Flash Cards'))

    with open(JSON_DIR+'flash.json', 'r') as f:
        flash_dict = json.load(f)

    deck_list = []

    print(make_banner("Pick Deck") + '\n')
    for i, deck in enumerate(flash_dict.keys()):
        print(f'{str(i + 1)}.  {deck}')
        deck_list.append({'index': i, 'name': deck})

    print()

    deck_choice = None
    valid_input = False
    while not valid_input:
        # do this if first time through loop
        if deck_choice is None:
            deck_choice = input('Choose Deck: ')
        # do this if is integer and a valid deck_choice
        elif is_integer(deck_choice) and int(deck_choice) <= len(deck_list):
            deck_choice = int(deck_choice)
            valid_input = True
        # do this if input is not integer or is string
        else:
            print('\nInvalid Input')
            deck_choice = input('Choose Deck: ')

    print(make_banner('Quiz Length'))
    quiz_length = None
    length_choice = None
    valid_input = False
    while not valid_input:
        # do this if first time in loop
        if length_choice is None:
            print('1.  10 Flash Cards')
            print('2.  20 Flash Cards')
            print('3.  30 Flash Cards')
            print('4.  40 Flash Cards')
            length_choice = input('\nChoose Length\n\n--->')
        # do this if input is integer and a valid option
        elif is_integer(length_choice) and int(length_choice) <= 4:
            length_choice = int(length_choice)
            if length_choice == 1:
                quiz_length = 10
            elif length_choice == 2:
                quiz_length = 20
            elif length_choice == 3:
                quiz_length = 30
            else:
                quiz_length = 40
            valid_input = True
        # do this if input is not an integor or is string
        else:
            print('\nInvalid Input')
            length_choice = input('Choose Length: ')

    deck_name = ''
    for deck in deck_list:
        if deck_choice-1 == deck['index']:
            deck_name = deck['name']

    make_quiz_list(deck_name, quiz_length)


print(make_banner('CompTIA Sec+ Quiz'))

main_screen_prompt = '1. Chapter Based Questions\n' \
                     '2. Review Missed Questions\n' \
                     '3. Study Port Numbers\n' \
                     '4. Study Flash Cards\n' \
                     '5. Quit\n\n' \
                     '--->'

loop_0 = True
while loop_0:
    opt_1 = input(main_screen_prompt)
    print()
    if opt_1 == '1':
        pass
    elif opt_1 == '2':
        pass
    elif opt_1 == '3':
        pass
    elif opt_1 == '4':
        flash_quiz()
        loop_0 = False
    elif opt_1 == '5':
        loop_0 = False
        print('Shutting Down')
    else:
        print('Invalid Input -- TRY AGAIN\n')
