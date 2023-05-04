import json
import random


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


def build_quiz(complete_list, e, m, h, q_len):
    random.shuffle(complete_list)
    random.shuffle(e)
    random.shuffle(m)
    random.shuffle(h)

    q = []

    if q_len == 10:
        pass
    elif q_len == 20:
        pass
    elif q_len == 30:
        pass
    elif q_len == 40:
        pass

    return q


with open('json/acronyms.json', 'r') as f:
    acronym_list = json.load(f)

easy_list = []
medium_list = []
hard_list = []

for acr_dict in acronym_list:
    if acr_dict['difficulty'] == 0:
        easy_list.append(acr_dict.copy())
    elif acr_dict['difficulty'] == 1:
        medium_list.append((acr_dict.copy()))
    else:
        hard_list.append((acr_dict.copy()))

prompt_0_str = 'How many acronyms would you like to study?\n' \
               '\t1.)  10\n' \
               '\t2.)  20\n' \
               '\t3.)  30\n' \
               '\t4.)  40\n\n' \
               '--> '

print(make_banner('Acronyms Quiz'), end='\n\n')

prompt_0 = input(prompt_0_str)
quiz_len = None

while quiz_len is None:
    if prompt_0 == '1':
        quiz_len = 10
        quiz = build_quiz(acronym_list, easy_list, medium_list, hard_list, 10)
    elif prompt_0 == '2':
        quiz_len = 20
        quiz = build_quiz(acronym_list, easy_list, medium_list, hard_list, 20)
    elif prompt_0 == '3':
        quiz_len = 30
        quiz = build_quiz(acronym_list, easy_list, medium_list, hard_list, 30)
    elif prompt_0 == '4':
        quiz_len = 40
        quiz = build_quiz(acronym_list, easy_list, medium_list, hard_list, 40)
    else:
        print(make_banner('Acronyms Quiz'), end='\n')
        print('\nInvalid Input - Please try again\n')
        prompt_0 = input(prompt_0_str)
