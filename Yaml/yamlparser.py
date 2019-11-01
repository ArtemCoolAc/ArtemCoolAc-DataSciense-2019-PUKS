import re
pattern = re.compile('\'[0-9]{4}-(0[1-9]|1[012])-(0[1-9]|1[0-9]|2[0-9]|3[01])\':')

i = 0
file = open('SkyTeam-Exchange.yaml', 'r')
splited = open('ste0.yml', 'w')
for j, line in enumerate(file):
    if j<10:
        print(line)
    if re.search(pattern, line) is not None:
        print('here match')
        splited.close()
        i += 1
        print(i)
        filename = 'ste{}.yml'.format(i)
        splited = open(filename, 'w')
        splited.write(line)
    else:
        splited.write(line)
file.close()
if splited:
    splited.close()

#for i, line in enumerate(file): 
#     for match in re.finditer(pattern, line): 
#         print('Found on line {}: {}'.format((i+1), match.group())) 

