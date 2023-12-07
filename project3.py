import random

def get_random_word():
    with open('10000_Words.csv', 'r') as word_file:
        lines = word_file.readlines()
        words = [line.strip() for line in lines]
        for word in words:
            if len(word) < 4:
                words.remove(word)
    return random.choice(words)
        
random_word = get_random_word()
print(random_word) #--> for testing purposes

word = []
def word_setup():
    for char in random_word:
        word.append("_")

ready_word = word_setup()
print("The word has " + str(len(random_word)) + " letters.")
print(word)

win = False
num_guess = 0
def get_user_guess():
    global win
    global num_guess
    print("You have " + str(6 - num_guess) + " guesses left.")

    while num_guess < 7 and not win:
        user_guess = input('Guess a letter: ')
        if user_guess in random_word:
            print("\nCorrect!")
            for i in range(len(random_word)):
                if random_word[i] == user_guess:
                    print("The letter " + user_guess + " is in position " + str(i+1) + ".")
                    word[i] = user_guess
            print(word)
            print("You have " + str(6 - num_guess) + " guesses left\n")
            check_winner()
        else:
            print("Incorrect!")
            num_guess += 1
            print("You have " + str(6 - num_guess) + " guesses left\n")
            print(word)
            
        check_winner()

def check_winner():
    global win
    for char in word:
        if "_" not in word:
            win = True
    if win == True:
        print("You win!")
        exit()
    if num_guess == 6 and win == False:
        print("You lose")
        print("The word was " + random_word + ".")
        exit()

get_user_guess()
