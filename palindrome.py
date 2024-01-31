'''
checking wheather number is palindrome

'''

# taking input from user

orginal_number = int(input(" Enter a number : "))

if orginal_number == int(str(orginal_number)[::-1]):
    print('Number is palindrome ', orginal_number)
else:
    print('Number is not palindrome', orginal_number)


