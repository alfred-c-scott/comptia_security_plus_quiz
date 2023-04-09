#!/usr/bin/python

import re
import json

q_directory = 'practice_tests/'
mock_q_directory = 'mock_files/'

def make_q_dict(question):
    f_c_pattern = re.compile(r' [ABCD]\. ')
    c_match = f_c_pattern.finditer(question)
    q_match = q_num_pattern.search(question)
    f_dict = {}
    f_dict['q_num'] = int(q_match.group()[q_match.start():q_match.end() - 2])
    a_start = None
    a_end = None
    b_start = None
    b_end = None
    c_start = None
    c_end = None
    d_start = None
    d_end = None
    for c in c_match:
        if c.group() == ' A. ':
            a_start = c.start()
            a_end = c.end()
        if c.group() == ' B. ':
            b_start = c.start()
            b_end = c.end()
        if c.group() == ' C. ':
            c_start = c.start()
            c_end = c.end()
        if c.group() == ' D. ':
            d_start = c.start()
            d_end = c.end()
            pass
    f_dict['q_txt'] = q[q_match.end():a_start]
    f_dict['choices'] = []
    f_dict['choices'].append({'opt': 'A', 'opt_text': q[a_end:b_start], 'is_correct': False})
    f_dict['choices'].append({'opt': 'B', 'opt_text': q[b_end:c_start], 'is_correct': False})
    f_dict['choices'].append({'opt': 'C', 'opt_text': q[c_end:d_start], 'is_correct': False})
    f_dict['choices'].append({'opt': 'D', 'opt_text': q[d_end:len(question)], 'is_correct': False})
    return f_dict


def set_correct_answer(q_d, q_n, chap, ans, exp):
    q_lst = q_d[chap]
    for q in q_lst:
        if q_n == q['q_num']:
            for ch in q['choices']:
                if ch['opt'] == ans:
                    ch['is_correct'] = True
                    ch['explanation'] = exp
    return q_d

# data from practice exam book
question_files = [
    q_directory+'ch_1_questions',
    q_directory+'ch_2_questions',
    q_directory+'ch_3_questions',
    q_directory+'ch_4_questions',
    q_directory+'ch_5_questions'
]

answer_files = [
    q_directory+'ch_1_answer_key',
    q_directory+'ch_2_answer_key',
    q_directory+'ch_3_answer_key',
    q_directory+'ch_4_answer_key',
    q_directory+'ch_5_answer_key'
]

# data files for demo
mock_question_files = [
    mock_q_directory+'ch_1_mock_questions',
    mock_q_directory+'ch_2_mock_questions',
]

mock_answer_files = [
    mock_q_directory+'ch_1_mock_answer_key',
    mock_q_directory+'ch_2_mock_answer_key',
]

q_list = []
master_q_list = []
q_dict = {}

# set to false to use mock data files
mock = False

if mock:
    q_files = mock_question_files
    a_files = mock_answer_files
else:
    q_files = question_files
    a_files = answer_files

q_num_pattern = re.compile(r'\d{1,3}\. ')

# opens a single data file, reformats the data, and adds to q_list
for data_file in q_files:
    with open(data_file, 'r') as f:
        q_data = f.read()
        q_data = q_data.replace('\n', ' ')
        ct = 1
        q_num_matches = q_num_pattern.finditer(q_data)
        for match in q_num_matches:
            # changes q_num match from string to integer
            q_num = int(match.group()[0:len(match.group()) - 2])
            # the questions are in order in the data file and this verifies that
            # and increments the counter to the next expected question number
            if ct == q_num:
                ct += 1

        # total number of questions in data file
        num_of_qs = ct - 1

        # reset counter
        ct = 1

        # finds the beginning and end of question and then adds the string to q_list
        while ct <= num_of_qs:
            q_begins = re.compile(rf'{str(ct)}\. ')
            q_ends = re.compile(rf'{str(ct + 1)}\. ')
            begins_match = q_begins.search(q_data)
            ends_match = q_ends.search(q_data)
            if begins_match and ends_match:
                q_list.append(q_data[begins_match.start():ends_match.start() - 1])
                q_data = q_data[ends_match.start():]
            # detects the last question in the string
            elif begins_match and not ends_match:
                q_list.append(q_data[begins_match.start():len(q_data)])
            ct += 1

        choice_pattern = re.compile(r'[ABCD]\. ')

        # reads question strings in q_list and reformats the string adding
        # a space before the choice option if there isn't one
        for enum, q in enumerate(q_list):
            choice_matches = choice_pattern.finditer(q)
            for c in choice_matches:
                if q[c.start() - 1] != ' ':
                    q = q[:c.start()] + ' ' + q[c.start():]
                    q_list[enum] = q
                    break
            # print(q_list[enum])

        # adds entire list of questions into a master list that will house
        # a list of all the questions seperated by chapters and then
        # re-declares q_list as an empty list
        master_q_list.append(q_list)
        q_list = []

chapter_ct = 0

for enum_0, chapter in enumerate(master_q_list):
    q_dict[str(enum_0+1)] = []
    for q in chapter:
        q_dict[str(enum_0+1)].append(make_q_dict(q))
    chapter_ct = enum_0+1

for enum_1, data_file in enumerate(answer_files):
    with open(data_file, 'r') as f:
        a_data = f.read()
        a_data = a_data.replace('\n', ' ')
        ct = 1
        q_num_matches = q_num_pattern.finditer(a_data)
        for match in q_num_matches:
            q_num = int(match.group()[:len(match.group())-2])
            if ct == q_num:
                answer = a_data[match.end():match.end()+1]
                next_q_pattern = re.compile(rf'{q_num+1}\. ')
                next_q_match = next_q_pattern.search(a_data)
                if next_q_match:
                    explanation = a_data[match.end()+3:next_q_match.start()]
                else:
                    explanation = a_data[match.end()+3:]
                q_dict = set_correct_answer(q_dict, q_num, str(enum_1+1), answer, explanation)
                ct += 1

# print(f'There are {chapter_ct} chapters in list')
ct = 0
while ct < chapter_ct:
    print(f'Chapter {ct+1}')
    q_lst = q_dict[str(ct+1)]
    for q in q_lst:
        print(q['q_num'], end=' ')
        choice_list = q['choices']
        for c in choice_list:
            if c['is_correct']:
                print(c['opt'])
                print(c['explanation'])
                pass
    ct += 1

quiz_json = json.dumps(q_dict, indent=2)

with open('quiz.json', 'w') as out_f:
    json.dump(quiz_json, out_f)
