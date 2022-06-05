One my professors in the University published final test in txt file. Then he was forced to review each of the student's test manually (60 txt files).
In order to save his effort, I decided to write a script, that could automate reviewing process.

1) After downloading the repo, fill up multiple_choice_quiz_blank.txt. For each question, place "X" character between the curly brackets [] e.g.
2. Who won Johnny Depp and Amber Heard trial?
a.[] Johny
b.[] Amber
c.[X] Who cares
Remember that there's only one correct answer.
2) Open up multiple-choice-quiz-parser-resolver.py and change the directories of file_path_users_answers and file_path_correct_answers*
3) Launch the script
*Please note that some operating systems have open restrictions if it comes to processing local files via script. In Ubuntu, I had to place the files in home/usr directory
