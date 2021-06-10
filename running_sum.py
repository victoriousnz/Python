def main():
    total = 0
    while True:
        num = input('Enter a number (q to quit): ')

        if num.lower() == 'q':
            print('Goodbye!')
            break

        try:
            total += int(num)
            print('The current total is:', total)
        except ValueError:
            print('Integers only please. Try again.')

main()