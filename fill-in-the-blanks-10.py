# IPND Stage 2 Final Project
import sys;


#Used for verification checks - if user entered a correct input matching options
levels = ["easy", "medium", "hard"]



#challenge strings
#if adding an extra string, make sure to update 'string_picker' with extra strings
#also add answers to variables below
string_easy = '''You are doing the Udacity course on the website ___1___.com. The first part covered the foundational programming language of the internet, ___2___. ___2___ was then supplemented with a second language to abstract the styling. This second language is ___3___. And thus modern webpages are built from ___2___ and ___3___. The next language to be covered is the language that this quiz was written in: ___4___! You should look forward to integrating this with my ___2___ and ___3___ skills......'''
string_medium = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary, tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''
string_hard = '''A common first thing to do in a language is display 'Hello ___1___!' In ___2___ this is particularly easy; all you have to do is type in: ___3___ "Hello ___1___!" Of course, that isn't a very useful thing to do. However, it is an example of how to output to the user using the ___3___ command, and produces a program which does something, so it is useful in that capacity. It may seem a bit odd to do something in a Turing complete language that can be done even more easily with an ___4___ file in a browser, but it's a step in learning ___2___ syntax, and that's really its purpose.'''

#used to isolate string for assessment
string_picker = [string_easy, string_medium, string_hard]




#Solutions to the blanks in the strings
easy_answers = ["Udacity", "HTML", "CSS", "python"]
medium_answers = ["function", "variables", "null", ""]
hard_answers = ["World", "python", "print", "HTML"]
answer_picker = [easy_answers, medium_answers, hard_answers]



#function to select the correct difficulty level requested by user
#user given choice and must input string
#output is the choice selected by the user from the variable 'levels'
def level_selector(user_level_choice):
    print "Please choose a level: easy, medium or hard"
    user_level_choice = raw_input("Level choice is: ")
    if user_level_choice == levels[0] or user_level_choice == levels[1] or user_level_choice == levels[2]:
        # 'if' checks 'levels' variables: easy, medium or hard
        print ""
        print "Your challenge is to complete: "
        print ""
        return user_level_choice
    else: #if user incorrectly spells or inputs non validated choice, requested to re-enter correctly
        print "That's not an option!"
        print ""
        return None


#function to go through blanks in sentence. user given max of 3 tries per question before game quits.
#number of chances resets every time user gets a question correct. note: does not update the sentence in this function, only validates answers
def answer_checker(user_level_choice, answers):
    #Their first array will be used to select the correct string
    for answer_blank in answers:
        print "What is the answer to question " + str(answers.index(answer_blank) + 1) + "?"
        answer_attempt = 1
        max_guesses = 3 #maximum number of guesses a player can have before they lose.
        while answer_attempt <= max_guesses:
            guess = raw_input("Answer: ") #user inputs answer guess
            if guess == answer_blank: #if correct, straight to next question
                print "correct!"
                print ""
                print ""
                answer_attempt = max_guesses
            else: #if incorrect, max of three tries and program exits if failure to get correct
                if answer_attempt == max_guesses:
                    print "Too many tries, better luck next time!"
                    sys.exit() #break if user makes too many tries
                else:
                    print "nope, try again....you have " + str(max_guesses - answer_attempt) + " goes remaining"
            answer_attempt = answer_attempt + 1 #increment i so that reduces number of attempts at guesses


#function to complete the sentence using the correct answer.
#note: could have built separate variables with correct answer and displayed this instead (possibly quicker than if, elif?)
#however, for assessment/demo purposes, this function swaps 'blanks' (e.g. ___1___) for correct answer
def word_transformation(answers, word):
    if word == "___1___":
        return answers[0]
    elif word == "___2___":
        return answers[1]
    elif word == "___3___":
        return answers[2]
    elif word == "___4___":
        return answers[3]
    else:
        return word[0]


#take string and correct answers, merge together to complete sentence. This function calls 'word_transformation' to complete the replacement
def sentence_completion(string, answers):
    processed = "" #blank 'sentence' that will be filled with completed sentence based on while loop below
    sentence_length = len(string)
    index = 0 #number to increment through each character in sentence. Set to start at the first character in the sentence
    while index <= (sentence_length - 1): # while loop to run through every character in sentence. Note: had to be set to 'sentence_length - 1' to not recieve error going incrementing past end of sentence in last while loop.
        test_word = string[index: index + 7] #get the four characters of the word for testing
        #print test_word
        if test_word == "___1___" or test_word == "___2___" or test_word == "___3___" or test_word == "___4___":  #test is word is one of the keywords. if it is....
            word_check = word_transformation(answers, test_word) #.....use the random generators to get the new verb or noun, put the new word into 'output_from_transform' jump forward four spots in in sentence (so all the letters in the VERB or NOUN don't get checked)
            index = index + 6    #increase the character index number by 4 so that it skips past the checked noun or verb.
        word_check = word_transformation(answers, test_word) #in event the 'if' statement is skipped, go straight here, and get the letter from the sentence.
        processed = processed + word_check #add the letter to the holding string 'processed'
        index += 1 #increment 'index' to move forward a single character in the sentence.
    print ""
    print ""
    print "Well done! :)"
    print ""
    print "Your final solution is:"
    print ""
    return processed


#primary starting function. Called to initiate game and call other functions.
def play_game():
    user_level_choice = None #Function for the user to select easy medium or hard
    print "Welcome to my world Game!"
    while user_level_choice == None:     #While loop to check if user input/selection is correct.
        user_level_choice = level_selector(user_level_choice) #function to assess user difficulty level
    string = string_picker[levels.index(user_level_choice)] #Highlights the string that will be used for the answer
    answers = answer_picker[levels.index(user_level_choice)] #select the correct set of answers to user difficulty selection
    print string #prints correct string for user-requested difficulty level
    print ""
    print ""
    answer_checker(user_level_choice, answers) #function to check all user answers. this function will quit program if user has too many attempts
    print ""
    print ""
    #while loop that does the tests to find blank words/gaps this loop increments through sentence one character at a time, but selects 7 characters at a time (length of ___1___ ___2___, etc.)
    #once checked: if no change, adds one letter to 'processed'. If a blank/gap, swaps with correct answer
    #returns the length of a string. Used to assess when at end of sentence in while loop below.
    processed = sentence_completion(string, answers)
    return processed



print play_game()
