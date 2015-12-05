'''
Simple class for formatting the questions out in an easier to use manner
'''


class QuestionClass(object):
    def __init__(self, question):
        self.question = question

    def __str__(self):
        out = self.question["question"]
        answers = self.question["answers"]
        for x,answer in enumerate(answers):
            num = "{}) ".format(x+1)
            out = out + "\n" + num + answer
        return out

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

    def get_question_text(self):
        return self.question["question"]

    def get_list_of_answers(self):
        return self.question["answers"]
