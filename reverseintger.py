'''
Algorithm for Reversing Integer
Mathematical Approch

reversed_number = reversed_number * 10 + original_number % 10

'''

'''
Take input form user and store in original_number

'''

orginal_number = int(input('Enter a number : '))

''' Initize the reverse_number to 0 '''

reverse_number = 0


'''  Loop while original number greater than 0'''

while orginal_number > 0:

    ''' Get reminder of original number dividing by 10'''
    reminder = orginal_number % 10

    ''' Multiply the reversed number by 10 and add reminder also store in itself'''

    reverse_number = reverse_number * 10 + reminder


    ''' Dividing orginal number by 10 and store in itself '''

    original_number = orginal_number // 10



# Printing the result 

print(f'reverse number : {reverse_number}')

