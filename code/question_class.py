'''
Simple class that wraps the question and answer text. Also provides clean 
methods for obtaining the question and answer text. The str() of this class
returns a nicely formatted question and answer that can be printed.
'''


# Class to handle questions and answers.
class QuestionClass(object):
    def __init__(self, question):
        self.question = question
        self.answers = question["answers"]

    def __str__(self):
        out = self.question["question"].encode('utf-8')
        answers = self.question["answers"]
        for x,answer in enumerate(answers):
            num = "{}) ".format(x+1)
            out = out + "\n" + num + answer.encode('utf-8')
        return out

    # A method that returns the correct answer text if it exists
    # for the question.
    def get_correct_answer_text(self):
        if "correctAnswerText" in self.question.keys():
            return self.question["correctAnswerText"].encode('utf-8')
        else:
            return str()

    # A method that checks the user's answer against the right answer.
    def check_answer(self, usersAnswer):
        if (usersAnswer - 1) == self.question["correctAnswerIndex"]:
            return True
        else:
            return False

    def get_correct_answer(self):
        return self.question["correctAnswerIndex"] + 1

    # A method that returns the question text.
    def get_question_text(self):
        return self.question["question"].encode('utf-8')

    # A method that returns a list of answers.
    def get_list_of_answers(self):
        answers = [x.encode('utf-8') for x in self.question["answers"]]
        return answers
