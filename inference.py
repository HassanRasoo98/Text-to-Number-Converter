import json

msg = input('Enter Your Message : ')
msg = msg.upper()

with open('map.json', 'r') as f:
  letter_map = json.load(f)

for letter in msg:
  print(letter_map.get(letter, ''), end=" ")

print()