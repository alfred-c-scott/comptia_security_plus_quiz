import re

q_num_pattern = re.compile(r'[0-9]{1,3}\. ')

q_directory = 'practice_tests/'
mock_q_directory = 'mock_files/'

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
q_dict = {}

# set to false to use mock data files
mock = True

if mock:
    q_files = mock_question_files
    a_files = mock_answer_files
else:
    q_files = question_files
    a_files = answer_files

# opens a single data file, reformats the data, and adds to q_list
with open(q_directory+'ch_4_questions') as f:
    f_data = f.read()
    f_data = f_data.replace('\n', ' ')
    ct = 1
    q_num_matches = q_num_pattern.finditer(f_data)
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
        begins_match = q_begins.search(f_data)
        ends_match = q_ends.search(f_data)
        if begins_match and ends_match:
            q_list.append(f_data[begins_match.start():ends_match.start() - 1])
        # detects the last question in the string
        elif begins_match and not ends_match:
            q_list.append(f_data[begins_match.start():len(f_data)])
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
    print(q_list[enum])
