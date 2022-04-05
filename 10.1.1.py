import random as rand
from os import system, name
from time import sleep

#the dictionry of the hangman status
HANGMAN_PHOTOS = {1: '\n\tx-------x',
2: '\n\tx-------x\n\
\t|\n\
\t|\n\
\t|\n\
\t|\n\
\t|\n\
\t|',
3: '\n\tx-------x\n\
\t|       |\n\
\t|       O\n\
\t|\n\
\t|\n\
\t|\n\
\t|',
4: '\n\tx-------x\n\
\t|       |\n\
\t|       O\n\
\t|       |\n\
\t|\n\
\t|\n\
\t|',
5: '\n\tx-------x\n\
\t|       |\n\
\t|       O\n\
\t|       |\n\
\t|      /|\\\n\
\t|\n\
\t|',
6: '\n\tx-------x\n\
\t|       |\n\
\t|       O\n\
\t|       |\n\
\t|      /|\\\n\
\t|      /\n\
\t|',
7: '\n\tx-------x\n\
\t|       |\n\
\t|       O\n\
\t|       |\n\
\t|      /|\\\n\
\t|      / \\\n\
\t|',}

def show_secreat_word(secreat_word, old_letter_guessed):
    """
    this function showing the secreat word in this format: d _ _ _ : _ d _ a_ _
        :param secreat_word: the secreat word
        :param old_letter_guessed: list of charectors

        value
            :type secreat_word: string/str
            :type old_letter_guessed: list of all letters the player enterd

        return: this function print a word in secreat format
        rtype: is empty string to avoid None problem
    """
    print('\t', end='')
    for i in range(len(secreat_word)):
        if i == 0:
            if secreat_word[i] in old_letter_guessed:
                print(secreat_word[i], end='')
            else:
                print('_', end='')
        else:
            if secreat_word[i] in old_letter_guessed:
                print(' ' + secreat_word[i], end='')
            else:
                print(' _', end='')
    print()
    return ''

def clear():
    """
    this function checks what opering system you are using
    and clear the screan for you
    """
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")

def pause():
    """
    this function checks what opering system you are using
    and pause the system before exiting
    """
    if name == "nt":
        _ = system("pause")
    else:
        _ = system("read-p")

def is_valid_input(letter_guessed):
    """
    the function checks if the letter guessed is valid or not

    :param letter_guessed: the letter of the player enterd

    type
        :value letter_guessed: str/string

    return:  if the letter is valid input the function returns true
            else the function returns false

    rtype: bool/boolean
    """
    for i in letter_guessed:
        if not (i >= 'a' or i >= 'A') and (i <= 'z' or i <= 'Z'):
            return False

    if len(letter_guessed) > 1:
        return False

    return True
   
def try_update_letter_guessed(letter_guessed, old_letter_guessed):
    """
    this function trying to add the guessed letter to old letter list
    the function using the is_valid_input() function for help

    :param letter_guessed: the letter of the player enterd
    :param old_letter_guessed: the list of all the letters the player ever enterd

    value
        :type letter_guessed: str/string
        :type old_letter_guessed: list of letters
    return: the function return true is she sucsessfuly adding the letter
            else the function return false
    rtype: bool/boolean
    """
    if letter_guessed in old_letter_guessed:
        return False
    elif is_valid_input(letter_guessed):
        old_letter_guessed.append(letter_guessed)
        return True
    else:
        return False

def check_win(secret_word, old_letter_guessed):
    """
    the function checks if all the word inside the list of old guessed
    
    :param secreat_word: the secreat word according the choose_word() function
    :param old_letter_guessed: the list of all the chars the player enterd

    value
        :type secreat_word: str/string
        :type old_letter_guessed: list of letters
    return: the function return true if the game win
            else the function returns false(it dosent mean the game lost)
    rtype: bool/boolean 
    """
    is_all_chars_in = True
    for i in secret_word:
        if i not in old_letter_guessed:
            is_all_chars_in = False
    if is_all_chars_in:
        return True
    else:
        return False

def print_hangman(num_of_tries):
    """
    this function printing the hangman gift according to the HANGMAN_PHOTOS dictionary
    """
    print(HANGMAN_PHOTOS[num_of_tries+1])

def choose_word(file_path, index):
    """
    the function choosing secreat word frome file(the player nead to enterd)
    the function choosing the word from the word file in index the flayer nead to enterd
    the function close the file automatic

    :param file_path: the path to the words file
    :param index: index to word inside the word file

    value
        :type file_path: str/string
        :type index: str/string (i did casting to int)

    return: the secreat word
    rtype: tr/string
    """
    index = int(index) #casting str to int 
    with open(file_path, 'r') as x: #open the file and close the file 
        x = x.read().split() #make the file contant to str/string and split him to words
        list_words =[x[0]] #list saveing the words from the file
        for i in x: #if word not in the list so add the word to list
            if i not in list_words:
                list_words.append(i)
        
        #the while loop make shur the index not going to be out of range
        #if the index > from the num of words so the index return to the start of the file
        while index > len(list_words):
            index -= len(list_words)
            
    return list_words[index-1] #return the word from the choosing index

def print_strt_gift():   
    """
    the function printing the welcome screan
    """  
    print("""
     _    _                                         
    | |  | |                                        
    | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
    |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    | |  | | (_| | | | | (_| | | | | | | (_| | | | |
    |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/  |                      
                        |___/""")

def print_old_list(old_letter_guessed):
    """
    the function printing the list of letters guessed

    :param old_letter_guessed: list of letters

    value
        :type old_letter_guessed: str/string
    return: None
    rtype: void/the function printing but she has no return value
    """
    print('\t', end='')
    for i in range(len(old_letter_guessed)):
        if i != len(old_letter_guessed)-1:
            print(old_letter_guessed[i] + ' => ', end='')
        else:
            print(old_letter_guessed[i])

def run_game(secreat_word, old_letter_guessed, MAX_TRIES, num_of_tries):
    """
    this is the function who responsible to run the game loop

    :param secreat_word: the secreat word according the choose_word() function
    :param old_letter_guessed: the list of all the charectors the player ever enterd
    :param MAX_TRIES: this is the maximum num of trys the player has
    :param num_of_tries: this parameter counting the num of mistakes the player enterd
    """
    print_hangman(num_of_tries)
    show_secreat_word(secreat_word, old_letter_guessed)

    while num_of_tries < MAX_TRIES:
        letter_guessed = input('\tEnter your guess here: ')

        if try_update_letter_guessed(letter_guessed, old_letter_guessed):
            if check_win(secreat_word, old_letter_guessed):
                print()
                show_secreat_word(secreat_word, old_letter_guessed)
                print('\tYou are wining')
                break
            if letter_guessed in secreat_word:
                print()
                show_secreat_word(secreat_word, old_letter_guessed)
            else:
                if num_of_tries < MAX_TRIES-1:
                    print('\t:(')
                    num_of_tries += 1
                    print_hangman(num_of_tries)
                    print()
                    show_secreat_word(secreat_word, old_letter_guessed)
                else:
                    print('\n\tYou are loosing !\n\tThe word is: ' + secreat_word)
                    break
        else:
            if not is_valid_input(letter_guessed):
                print('\tX') 
            else:
                print('\tX')
                print_old_list(old_letter_guessed)
                       

def main():
    clear() #the function clean the screan
    print_strt_gift() #the function printing the welcome screan
    sleep(3) #this function pause the screan for 3 seconds
    clear() #the function clean the screan

    print() #print empty line
    file_path = input('\tEnter path for words file: ') #the fil path (user input)
    index_word = input('\tEnter index for word in file: ') #the secreat word index (user input)
    print() #print empty line

    secreat_word = choose_word(file_path, index_word) #make the secreat wor and save it to variable
    old_letter_guessed = [] #make the list of all player trys
    MAX_TRIES = 7 #the maximun life of the flayer
    num_of_tries = 0 #player mistakes

    run_game(secreat_word, old_letter_guessed, MAX_TRIES, num_of_tries) #call the function who run the game

    print() #print ampty line
    

if __name__ == '__main__':
    main()
