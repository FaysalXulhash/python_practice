secret_num = int(input('Enter your secret number: '))
guess_count = 0
guess_limit = int(input('How many time want to guess? '))

while guess_count < guess_limit:
    guess = int(input('Guess a number!: '))
    guess_count += 1
    if guess == secret_num:
        print("You Won!!!")
        break
