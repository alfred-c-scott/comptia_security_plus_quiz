import json

with open('acronyms_flash_data_2') as a:
    acronym_list = a.readlines()

with open('acronym_flash_data_definitions_2') as d:
    definition_list = d.readlines()


# dictionary layout
# my_acronym_dict_list = [
#     {
#         'acronym': '',
#         'definition': '',
#         # will be set to 0, 1, or 2 by user with 0 being easiest, 2 being hardest
#         'difficulty': '',
#     }
# ]
acronym_dict = {}
acronym_dict_list = []

for i, acronym in enumerate(acronym_list):
    acronym_dict['acronym'] = acronym[0:len(acronym)-1]
    acronym_dict['definition'] = definition_list[i][0:len(definition_list[i])-1]
    acronym_dict['difficulty'] = 2
    # print(acronym, end=': ')
    # print(definition_list[i])
    acronym_dict_list.append(acronym_dict.copy())

for a_dict in acronym_dict_list:
    print(a_dict['acronym'], end=':  ')
    print(a_dict['definition'], end=':  ')
    print(f"difficulty: {a_dict['difficulty']}")

with open('json/acronyms.json', 'w') as j:
    json.dump(acronym_dict_list, j, indent=2)

