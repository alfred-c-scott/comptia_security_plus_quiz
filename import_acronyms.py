import re
import json

flash_dict = {}

back_pattern = re.compile(r'--')

with open('acronyms_flash_data', 'r') as f:
    f_data = f.readlines()
    flash_dict['acronym flash cards'] = []
    acronym_dict = {}
    for i, line in enumerate(f_data):
        back_matches = back_pattern.search(line)
        if back_matches:
            acronym_dict['front'] = f_data[i-1][0:len(f_data[i-1])-1]
            acronym_dict['back'] = line[2:len(f_data[i])-1]
            acronym_dict['attempts'] = 0
            acronym_dict['misses'] = 0
            flash_dict['acronym flash cards'].append(acronym_dict.copy())
    i = 0

flash_json = json.dumps(flash_dict, indent=2)

print(flash_json)

with open('flash.json', 'w') as json_out:
    json.dump(flash_json, json_out)
