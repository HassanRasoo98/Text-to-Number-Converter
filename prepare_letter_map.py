import json

letter_map = {' ': 0}
base = '2'
number = ''

for i in range(65, 91):
    letter = chr(i)
    number += base

    print(chr(i), number)
    if chr(i) not in letter_map:
      letter_map[chr(i)] = number

    if base == '7' or base == '9':
      if len(number) == 4:
          number = ''
          base = int(base) + 1
          base = str(base)

    else:
         if len(number) == 3:
          number = ''
          base = int(base) + 1
          base = str(base)

with open('map.json', 'w') as f:
   json.dump(letter_map, f, indent=2)