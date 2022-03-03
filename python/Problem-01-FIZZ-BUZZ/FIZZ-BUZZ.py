#FIZZ-BUZZ:
# Write a program that displays by console (with a print) the numbers from 1 to 100 
# (both included and with a line break between each print), substituting the following:
#     - Multiples of 3 for the word "fizz".
#     - Multiples of 5 for the word "buzz".
#     - Multiples of 3 and 5 at the same time for the word "fizzbuzz".


for num in range(1,101):
    if num%3 == 0 and num%5 ==0:
        print('fizzbuzz')

    elif num%3 == 0:     
        print('fizz')

    elif num%5 == 0:
        print('buzz')
    
    else:
        print(num)