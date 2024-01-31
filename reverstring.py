'''
Reversing the string 

'''

'''
reverse using slice 

orginal_string = str(input('Enter a word to make reverse : '))

reversed_string = orginal_string[::-1]

print(reversed_string)

'''


'''
reverse using listapproch

orginal_string = str(input('Enter a word : '))

new_string = list(orginal_string)
new_string.reverse()

reversed_string = ''.join(new_string)

print(str(reversed_string))

'''
'''
using for loop 

'''
orginal_string = str(input('Enter a string : '))
new_string = ''
#for i in range(len(orginal_string)):
#    new_string = orginal_string[i] + new_string

for char in orginal_string:
    new_string = char + new_string

if orginal_string == new_string:
    print(True)
else:
    print(False)

print(new_string)

