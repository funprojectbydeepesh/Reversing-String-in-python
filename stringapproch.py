''''
reversing the integer using string approch

'''

''' taking input from user and store in orginal_number'''

orginal_number = int(input('Enter the number : '))

''' converting the  int into str '''

str_integer = str(orginal_number)




''' 
loop the str in their length 

reverse_integer = ''

for i in range(len(str_integer)):

    reverse_integer =  str_integer[i] + reverse_integer

'''

reverse_integer = str_integer[::-1]

'''
The [::-1] operation is one-liner for reversing an iterable i.e. list, strings, tuples etc. which can be iterated 

'''

# Print the output
print(int(reverse_integer))


