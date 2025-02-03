firstName = input('Enter your first name: ')
lastName = input('Enter your last name: ')
age = input('Enter your age: ')
slicedName = firstName[0:3]
formattedText = 'Hello, {}! Welcome. You are {} years old.'

print('Full Name: ' + firstName + ' ' + lastName)
print('Sliced Name: ' + slicedName)
print(formattedText.format(slicedName, age))