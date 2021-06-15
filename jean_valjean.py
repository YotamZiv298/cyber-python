def analyze_number_digits():
    num = int(input('Please enter your number: '))
    # if 10000 <= num <= 99999:
    print('You entered the number: {0}'.format(num))
    print('The digits of this number are: ', end='')
    sum_of_digits = 0
    for ch in str(num):
        print(ch + ' ', end='')
        sum_of_digits += int(ch)
    print('\nThe sum of the digits is: {0}'.format(sum_of_digits))


analyze_number_digits()
