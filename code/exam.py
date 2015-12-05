'''
A class to handle everything to do with an exam, such as keeping track of results and statistics,
and adminstering the exam.  Includes a method that allows the exam class to be extended and
controlled from another class if required.


'''

class Exam():
    answer_list = list()    # To keep track of what the user answered to each question
    question_list = list()  # A list of all the questions to ask the user.
    current_question_index = 0

    def __init__(self):
        # set up the exam, what databases to include, how many questions to ask.
        # then get those questions and add them to the question list.  Initialize
        # the answer list to false for every question.  Also check that the user's
        # number of questions is actually possible given the size of our databases
        pass

    def get_statistics(self):
        return sum(self.answer_list)/len(self.answer_list)

    def get_details(self):
        return self.answer_list

    def print_details(self):
        # prints the details of the exam
        for aindex in range(len(self.answer_list)):
            print "Question {0} Result: ".format(aindex, "Correct" if self.answer_list[aindex] else "Incorrect")
        pass

    def administerExam(self):
        # Administer the test to user, including input and output to the screen
        for qindex in range(len(self.question_list)):
            print self.question_list[qindex]
            try:
                answerIndex = int(raw_input("Answer: "))
            except:
                print "That's not what an number looks like"
            finally:
                if self.question_list[qindex].check_answer(answerIndex-1):
                    print "Correct!\n"
                    self.answer_list[qindex] = True
                else:
                    print "INCORRECT\n"
                    self.answer_list[qindex] = False
                pass
        print "Result: {0}%".format(self.get_statistics())
        self.print_details()
