'''
reversing the integer by list approch

'''
#taking input from user 
orginal_number = int(input("Enter a number : "))

#converting int to list

first_number = list(str(orginal_number))

#reversing list using reverse method
first_number.reverse()

#converting list into number
reverse_number = ''.join(first_number)

print(f' The reverse number is {int(reverse_number)}')