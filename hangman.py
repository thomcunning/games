import random


def is_done(result):

    if result == '' or ' _ ' in result:
        return False
    else:
        print ('You got it!')
        return True


def show_guess_result(total_guesses, hidden_word):

    correct_guesses = []


    if total_guesses != []: #to display hidden_word (as underlines) before first guess

        for i in hidden_word:
            if i in total_guesses:
                correct_guesses.append(i)
        
        result = ''

        for i in hidden_word:
            if i in correct_guesses:
                result = result + i
            else:
                result = result + ' _ '

        return result

    else:
        result = ''
        for i in hidden_word:
            result = result + ' _ '
        print('The word is:')
        print(result)
        return result



#open the file for the list of words, split all words into 'word_list', pick one at random to be 'hidden _word'.

file = open('list_file.txt','r')
line= file.readline()

word_list=[]
word_list=line.split(",")

var = random.randint(0,len(word_list)-1)
hidden_word = word_list[var]
file.close()

#set incrementer for guesses to 0, call 'show_guess_result()' for first time to display the number of characters (as underlines)

num_guesses = 0
total_guesses = []
result = show_guess_result(total_guesses, hidden_word)




#while 'hidden_word' is not guessed yet, play the guessing game...

while is_done(result) != True:

    guess = input('Your total number of guesses so far is: ' + str(num_guesses) + '.\nGuess a lower case letter:')
    
    if len(guess) ==1:
        guess = guess.lower()

        if guess.isalpha():

            if guess in total_guesses:
                print('You already guessed that. Try another letter.')

            else: 
                total_guesses.append(guess)
                num_guesses +=1
                result = show_guess_result(total_guesses, hidden_word)
                print(result)
            
        else:
            print('Your guess was not an alphabetical character. Guess again.')
    else:
        print('Enter only a single, lowercase alphabetical character guess.')

