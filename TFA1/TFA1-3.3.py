firstName = input('Enter first name: ')
lastName = input('Enter last name: ')
age = input('Enter age: ')
conNum = input('Enter contact number: ')
course = input('Enter course: ')

formattedText = ('Last Name: {} \nFirst Name: {} \nAge: {} \nContact Number: {} \nCourse: {} \n')
f = open('TFA1/students.txt', 'a+')
f.write(formattedText.format(lastName, firstName, age, conNum, course))
line = f.readline()
f.close()

print('Information has been saved to \'students.txt\'.')