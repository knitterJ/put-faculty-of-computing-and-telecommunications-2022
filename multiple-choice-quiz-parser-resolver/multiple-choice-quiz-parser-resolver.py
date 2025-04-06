# -*- coding: utf-8 -*-
"""
Create a program that reads the data from a text file with filled up quiz/questionnaire,
Then compare parsed data with correct answers stored in another file.
The program should display the total number of correct answers in percentage point,
and then indicates which questions were answered incorrectly
Threshold to pass the test equals 50%.
"""

file_path_users_answers = "./multiple_choice_quiz_example_answers.txt"
file_path_correct_answers = "./multiple_choice_quiz_correct_answers.txt"


def parsePunchedCard(file_path):
    text_file = open(file_path, "r")
    data = text_file.read()
    # print(type(data))   <type 'str'>

    #make a list of questions out of "data"
    bla = data.split("\n\n")
    #print(bla[2]) #prints out question number 3 with answers
    # print(type(bla))   <type 'list'>

    newList = []

    for questionanswers in bla:
        # creates list(array) of each question, by replacing new line character with a coma
        splitresults = questionanswers.split('\n')
        # print(splitresults) ['1....', 'a....', 'b...']
        #                     ['2....', 'a....', 'b...']
        newList.append(questionanswers[0] + ":" + splitresults[1][2:5]
                       + ","
                       + questionanswers[0] + ":" + splitresults[2][2:5]
                       + ","
                       + questionanswers[0] + ":" + splitresults[3][2:5]
                       )

    #remove all the spaces in the array list caused by hardcoded [2:5]
    result = [x.replace(' ', '') for x in newList]
    print(result)
    store = []
    #loop through the answers list in order to detect positions of "X" (detect also little "x", in case of blend of mistake and laziness))
    for answers in result:
        uppercase_answers = answers.upper()
        store.append(uppercase_answers.find('X'))

    #store is a list with positions of X expressed in int
    #print(store)
    return store


usersAnswers = parsePunchedCard(file_path_users_answers)
correctAnswers = parsePunchedCard(file_path_correct_answers)

print(usersAnswers)
print(correctAnswers)

resultsArray = []
for i, j in zip(usersAnswers, correctAnswers):
    if(i == j):
        resultsArray.append(1)
    else:
        resultsArray.append(0)

print(resultsArray)
totalcorrect = sum(resultsArray)
total = len(resultsArray)
percentage = 100*totalcorrect/total

if(percentage > 50):
    theverdict = "so you passed the test 🤩"
else:
    theverdict = "so unfortunately you failed 😵"

print("Your score is: " + str(totalcorrect)
      + "/" + str(total) + " (" + str(percentage) + "%), " + theverdict)

print("The questions that were answered incorrectly are:")
for i in range(len(resultsArray)):
    if(resultsArray[i] != 1):
        print(i + 1)
