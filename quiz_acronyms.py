import json
import random


def banner(message):
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


def build_quiz(n_a, e, m, h, multiplier):
    random.shuffle(n_a)
    random.shuffle(e)
    random.shuffle(m)
    random.shuffle(h)

    num_n_a = 4 * multiplier
    num_e = 1 * multiplier
    num_m = 2 * multiplier
    num_h = 3 * multiplier

    q = n_a[0:num_n_a]
    print(f"len of q:        {len(q)}")
    if len(e) < num_e:
        print(f"length of e:     {len(e)}")
        print(f"num needed:      {num_e}")
        if len(e) != 0:
            q.append(e)
        num_to_pull = num_e - len(e)
        print(f"needed from n_a: {num_to_pull}")
        tmp_lst = n_a[len(q):len(q)+num_to_pull]
        for a in tmp_lst:
            q.append(a)
    else:
        tmp_list = e[0:num_e]
        for a in tmp_list:
            q.append(a)
    if len(m) < num_m:
        pass
    if len(h) < num_h:
        pass

    for a in q:
        print(a['acronym'])
    print(f"len of q:        {len(q)}")
    return q


with open('json/acronyms.json', 'r') as f:
    acronym_list = json.load(f)


easy_list = []
medium_list = []
hard_list = []
no_attempts_list =[]

for acr_dict in acronym_list:
    if acr_dict['difficulty'] == 1:
        easy_list.append(acr_dict.copy())
    elif acr_dict['difficulty'] == 2:
        medium_list.append((acr_dict.copy()))
    elif acr_dict['difficulty'] == 3:
        hard_list.append((acr_dict.copy()))
    else:
        no_attempts_list.append(acr_dict.copy())

prompt_0_str = 'How many acronyms would you like to study?\n' \
               '\t1.)  10\n' \
               '\t2.)  20\n' \
               '\t3.)  30\n' \
               '\t4.)  40\n\n' \
               '--> '

print(banner('Acronyms Quiz'), end='\n\n')

prompt_0 = input(prompt_0_str)
# quiz_len = None

while True:
    if prompt_0 == '1' or '2' or '3' or '4':
        # quiz_len = 10
        quiz = build_quiz(no_attempts_list, easy_list, medium_list, hard_list, int(prompt_0))
        break
    # elif prompt_0 == '2':
        # quiz_len = 20
        # quiz = build_quiz(no_attempts_list, easy_list, medium_list, hard_list, 20)
    # elif prompt_0 == '3':
        # quiz_len = 30
        # quiz = build_quiz(no_attempts_list, easy_list, medium_list, hard_list, 30)
    # elif prompt_0 == '4':
        # quiz_len = 40
        # quiz = build_quiz(no_attempts_list, easy_list, medium_list, hard_list, 40)
    else:
        print(banner('Acronyms Quiz'), end='\n')
        print('\nInvalid Input - Please try again\n')
        prompt_0 = input(prompt_0_str)
