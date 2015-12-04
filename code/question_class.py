'''
Simple class for formatting the questions out in an easier to use manner
'''


class QuestionClass():
    def __init__(self, question):
        self.question = question

    def __str__(self):
        print self.question["question"]
        answers = self.question["answers"]
        for x in range(len(answers)):
            print answers[x]

    def print_answer_text(self):
        try:
            print self.question["correctAnswerText"]
        except:
            pass

    def check_answer(self, usersAnswer):
        if usersAnswer == self.question["correctAnswerIndex"]:
            return True
        else:
            return False
