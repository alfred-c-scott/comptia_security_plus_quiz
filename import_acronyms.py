import re
import json

flash_dict = {}

back_pattern = re.compile(r'--')

with open('acronyms_flash_data', 'r') as f:
    f_data = f.readlines()

flash_dict['acronym_flash_cards'] = []
acronym_dict = {}
for i, line in enumerate(f_data):
    back_matches = back_pattern.search(line)
    if back_matches:
        acronym_dict['front'] = f_data[i-1][0:len(f_data[i-1])-1]
        acronym_dict['back'] = line[2:len(f_data[i])-1]
        acronym_dict['attempts'] = 0
        acronym_dict['misses'] = 0
        flash_dict['acronym_flash_cards'].append(acronym_dict.copy())
i = 0

with open('json/flash.json', 'w') as f:
    json.dump(flash_dict, f, indent=2)

with open('json/flash.json', 'r') as f:
    my_dict = json.load(f)
