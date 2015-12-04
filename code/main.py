'''
Main console application.  Handles user input and such but not the generation or getting of questions
'''
from database_accessor import DatabaseAccessor

# create the question handler then just loop until user wants to exit or the exam is done

print "Welcome to the Glider Flight Test Exam Generator"
for _ in range(3):
    try:
        num_questions = int(raw_input("Please enter the number of questions you'd like (1-100):"))
        break
    except:
        print "Sorry, that number was invalid, try again"

database = DatabaseAccessor()

for i in range(num_questions):
    print "Question #{}:".format(i+1)

    # get question1
    question = database.get_random_question()
    # display question
    print question

    # wait for user input
    user_answer = int(raw_input("Selection: ")) - 1

    # check user input and print a response
    if question.check_answer(user_answer):
        question.print_answer_text()
    else:
        print "Incorrect."

    #Print a space to separate questions.
    print ""


    pass
