#1

my_dict = {1.12: 'aa', 67.9: 45, 3.11: 'ccc', 7.9: 'dd', 9.2: 'ee', 7.1: 'ff',
           0.12: 'qq', 1.91: 'aa', 10.12: [1, 2, 3], 99.0: {9, 0, 1}}
print(min(my_dict) + max(my_dict))




#2

users = [
    {'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
    {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
    {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
    {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
    {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
    {'name': 'John', 'phone': '233-421-32', 'email': ''},
    {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
    {'name': 'Alina', 'phone': '+7948-799-2434', 'email': 'ali.ch.b@gmail.com'},
    {'name': 'Robert', 'phone': '420-2011', 'email': ''},
    {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
    {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
    {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
    {'name': 'Roman', 'phone': '+7459-145-8059', 'email': 'roma988@mail.ru'},
    {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
    {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
    {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}
]

names = sorted([u['name'] for u in users if u['phone'].endswith('8')])
print(*names)




#3
users = [
    {'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
    {'name': 'Helga', 'phone': '555-1618'},
    {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
    {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
    {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
    {'name': 'John', 'phone': '233-421-32', 'email': ''},
    {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
    {'name': 'Alina', 'phone': '+7948-799-2434'},
    {'name': 'Robert', 'phone': '420-2011', 'email': ''},
    {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
    {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
    {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
    {'name': 'Roman', 'phone': '+7459-145-8059'},
    {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
    {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
    {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}
]

names = sorted([u['name'] for u in users if not u.get('email')])
print(*names)



#4
num = input()

d = {
    '0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
    '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'
}

print(*[d[digit] for digit in num])


#5

course = input()

data = {
    'CS101': ('3004', 'Хайнс', '8:00'),
    'CS102': ('4501', 'Альварадо', '9:00'),
    'CS103': ('6755', 'Рич', '10:00'),
    'NT110': ('1244', 'Берк', '11:00'),
    'CM241': ('1411', 'Ли', '13:00')
}

room, teacher, time = data[course]
print(f"{course}: {room}, {teacher}, {time}")


#6

text = input()

keyboard = {
    **{c: '1'*(i+1) for i, c in enumerate(".,?!:")},
    **{c: '2'*(i+1) for i, c in enumerate("ABC")},
    **{c: '3'*(i+1) for i, c in enumerate("DEF")},
    **{c: '4'*(i+1) for i, c in enumerate("GHI")},
    **{c: '5'*(i+1) for i, c in enumerate("JKL")},
    **{c: '6'*(i+1) for i, c in enumerate("MNO")},
    **{c: '7'*(i+1) for i, c in enumerate("PQRS")},
    **{c: '8'*(i+1) for i, c in enumerate("TUV")},
    **{c: '9'*(i+1) for i, c in enumerate("WXYZ")},
    ' ': '0'
}

result = ""

for ch in text.upper():
    if ch in keyboard:
        result += keyboard[ch]

print(result)


#7

text = input()

morse = {
    'A': '.-',   'B': '-...', 'C': '-.-.', 'D': '-..',  'E': '.',    'F': '..-.',
    'G': '--.',  'H': '....', 'I': '..',   'J': '.---', 'K': '-.-',  'L': '.-..',
    'M': '--',   'N': '-.',   'O': '---',  'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...',  'T': '-',    'U': '..-',  'V': '...-', 'W': '.--',  'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----','2': '..---','3': '...--','4': '....-','5': '.....',
    '6': '-....','7': '--...','8': '---..','9': '----.','0': '-----'
}

encoded = [morse[ch] for ch in text.upper() if ch in morse]
print(*encoded)


#8

result = {x: x**2 for x in range(11, 16)}


#9

dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}

result = {}

for k in dict1:
    result[k] = dict1[k] + dict2.get(k, 0)

for k in dict2:
    if k not in result:
        result[k] = dict2[k]


#10




text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'

result = {}

for ch in text:
    result[ch] = result.get(ch, 0) + 1


#11


words = s.split()

count = {}
for w in words:
    count[w] = count.get(w, 0) + 1
max_count = max(count.values())
candidates = [w for w in count if count[w] == max_count]
print(min(candidates))

#12




result = {}

for dog, name, surname, age in pets:
    owner = (name, surname, age)
    result.setdefault(owner, []).append(dog)


#13

import re

text = input().lower()
words = re.findall(r'[a-zA-Z]+', text)
count = {}
for w in words:
    count[w] = count.get(w, 0) + 1
min_count = min(count.values())
candidates = [w for w in count if count[w] == min_count]
print(min(candidates))


#14

ids = input().split()
used = {}
result = []
for id_ in ids:
    if id_ not in used:
        used[id_] = 0
        result.append(id_)
    else:
        used[id_] += 1
        result.append(f"{id_}_{used[id_]}")   
print(*result)


