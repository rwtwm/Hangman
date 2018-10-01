import random

def print_word(playWord):
        printWord = ""
        for char in playWord:
                if char == '^':
                        printWord += "_ "
                else:
                        printWord += "{} ".format(char)
	
        printWord = printWord[:-1]
        print(printWord)

   

#Opens dictionary file, finds its length and stores a random word as the 'clue' word. 
sowpods = open("sowpods.txt","r")
lines = sowpods.readlines()
target_line = random.randint(1, len(lines))
clue = lines[target_line-1].strip()


print("Welcome to hangman")
game = True
lives = 6
my_word = "^"*(len(clue))


print(my_word)
my_word_list = list(my_word)
my_failed_list = []


#Main game loop
while game:
        print_word(''.join(my_word_list))
        this_guess = input("Guess a letter: ")

        if clue.find(this_guess) != -1 :
                for i,x in enumerate(clue):
                        if this_guess == x:
                                my_word_list[i] = this_guess.upper()
        elif this_guess not in my_failed_list:
                my_failed_list.append(this_guess)
                lives = lives - 1
        else:
                print("You've already tried that")

        print(''.join(my_word_list))
        print(my_failed_list)
              
        if ''.join(my_word_list).upper() == clue.upper():
                print("well done")
                game = False

        if lives == 0:
                print('Bad luck, the word was {}'.format(clue))
                game = False

        

                
        





