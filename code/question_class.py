'''
Simple class that wraps the question and answer text. Also provides clean 
methods for obtaining the question and answer text. The str() of this class
returns a nicely formatted question and answer that can be printed.
'''


# Class to handle questions and answers.
class QuestionClass(object):
    def __init__(self, question, randomize=True):
        self.question_text = question["question"].encode('utf-8')
        self.answers = list()
        for ans in question["answers"]:
            self.answers.append(ans.encode('utf-8'))
        self.answerindex = question["correctAnswerIndex"]
        self.answertext = question["correctAnswerText"].encode('utf-8')
        self.used = False  # Indicates if the question was already chosen

        if randomize:
            from random import sample
            new_indicies = sample(range(len(self.answers)), len(self.answers))
            newanswers = [None for _ in range(len(self.answers))]
            for i in range(len(self.answers)):
                newanswers[new_indicies[i]] = self.answers[i]
            self.answerindex = new_indicies[self.answerindex]
            self.answers = newanswers

    def __str__(self):
        out = self.question_text
        for x, answer in enumerate(self.answers):
            num = "{}) ".format(x+1)
            out = out + "\n" + num + answer
        return out

    # A method that returns the correct answer text if it exists
    # for the question.
    def get_correct_answer_text(self):
        return self.answertext

    # A method that checks the user's answer against the right answer.
    def check_answer(self, usersAnswer):
        if (usersAnswer - 1) == self.answerindex:
            return True
        else:
            return False

    def get_correct_answer(self):
        return self.answerindex + 1

    # A method that returns the question text.
    def get_question_text(self):
        return self.question_text

    # A method that returns a list of answers.
    def get_list_of_answers(self):
        return self.answers

    # A method that declares if a question was used previously.
    def set_used(self):
        self.used = True

    # A method that clears the previously used flag.
    def clear_used(self):
        self.used = False

    # Returns the flag to indicate if the question was used or not
    def get_used(self):
        return self.used

