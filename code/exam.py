'''
A class to handle everything to do with an exam, such as keeping track of results and statistics,
and adminstering the exam.  Includes a method that allows the exam class to be extended and
controlled from another class if required.


'''

from database_accessor import DatabaseAccessor

class Exam():
    question_database = None
    num_questions = None
    answer_list = list()    # To keep track of what the user answered to each question
    question_list = list()  # A list of all the questions to ask the user.
    current_question_index = 0

    def __init__(self, num_questions=50):
        # set up the exam, what databases to include, how many questions to ask.
        # then get those questions and add them to the question list.  Initialize
        # the answer list to false for every question.  Also check that the user's
        # number of questions is actually possible given the size of our databases
        self.question_database = DatabaseAccessor()
        self.num_questions = num_questions

        for i in range(self.num_questions):
            self.question_list.append(self.question_database.get_random_question())
            self.answer_list.append(None)

    def get_percent(self):
        return float(self.get_num_correct()) / float(self.num_questions) * 100

    def print_percent(self):
        print "Result: {0}%".format(int(self.get_percent()))

    def get_num_correct(self):
        total_correct = 0
        for x in self.answer_list:
            if x == True:
                total_correct += 1
        return total_correct

    def get_details(self):
        return self.answer_list

    def print_details(self):
        # prints the details of the exam
        for aindex in range(len(self.answer_list)):
            print "Question {0} Result: {1}".format(aindex,
                                                    "Correct" if self.answer_list[aindex] == True else "Incorrect")
        pass

    def administer_exam(self):
        # Administer the test to user, including input and output to the screen
        for qindex in range(len(self.question_list)):
            print "Question Number {0}".format(qindex + 1)
            print self.question_list[qindex]

            answer_index = None
            while 1:
                userInput = raw_input("Answer: ")
                try:
                    answer_index = int(userInput)
                    break
                except:
                    if userInput.lower() == 'exit':
                        print "Exiting Exam"
                        break
                    else:
                        print "That's not what an number looks like, try again"
            if answer_index is not None:
                if self.question_list[qindex].check_answer(answer_index - 1):
                    print "Correct!\n"
                    self.answer_list[qindex] = True
                else:
                    print "INCORRECT - Correct Answer is {0}\n".format(
                        self.question_list[qindex].get_correct_answer() + 1)
                    self.answer_list[qindex] = False
            else:
                break
        self.print_percent()
        # self.print_details()


if __name__ == '__main__':
    exam = Exam()
    exam.administer_exam()
