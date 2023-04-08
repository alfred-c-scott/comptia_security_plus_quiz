import re

q_num_pattern = re.compile(r'[0-9]{1,3}\. ')

q_directory = 'practice_tests/'

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
mock_question_files = [
    q_directory+'ch_1_mock_questions',
    q_directory+'ch_2_mock_questions',
]
mock_answer_files = [
    q_directory+'ch_1_mock_answer_key',
    q_directory+'ch_2_mock_answer_key',
]

q_list = []
q_dict = {}

mock = True

if mock:
    q_files = mock_question_files
    a_files = mock_answer_files
else:
    q_files = question_files
    a_files = answer_files

with open(q_directory+'ch_4_questions') as f:
    f_data = f.read()
    f_data = f_data.replace('\n', ' ')
    ct = 1
    q_num_matches = q_num_pattern.finditer(f_data)
    for match in q_num_matches:
        q_num = int(match.group()[0:len(match.group()) - 2])
        if ct == q_num:
            ct += 1

    num_of_qs = ct - 1

    ct = 1
    while ct <= num_of_qs:
        q_begins = re.compile(rf'{str(ct)}\. ')
        q_ends = re.compile(rf'{str(ct + 1)}\. ')
        begins_match = q_begins.search(f_data)
        ends_match = q_ends.search(f_data)
        if begins_match and ends_match:
            q_list.append(f_data[begins_match.start():ends_match.start() - 1])
        elif begins_match and not ends_match:
            q_list.append(f_data[begins_match.start():len(f_data)])
        ct += 1

choice_pattern = re.compile(r'[ABCD]\. ')

for enum, q in enumerate(q_list):
    choice_matches = choice_pattern.finditer(q)
    for c in choice_matches:
        if q[c.start() - 1] != ' ':
            q = q[:c.start()] + ' ' + q[c.start():]
            q_list[enum] = q
            break
    print(q_list[enum])
