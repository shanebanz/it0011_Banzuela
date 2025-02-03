print('Reading Student Information:')
f = open('TFA2/students.txt', 'r')

for content in f:
    print(content)
f.close()