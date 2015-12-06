'''
Simple class for formatting the questions out in an easier to use manner.
'''


class QuestionClass(object):
    def __init__(self, question):
        self.question = question

    def __str__(self):
        out = self.question["question"].encode('utf-8')
        answers = self.question["answers"]
        for x,answer in enumerate(answers):
            num = "{}) ".format(x+1)
            out = out + "\n" + num + answer.encode('utf-8')
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
        return self.question["question"].encode('utf-8')

    def get_list_of_answers(self):
        answers [x.encode('utf-8') for x in self.question["answers"]]
        return answers
