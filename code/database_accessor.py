'''
A class that handles the getting a setting of questions in the databases.

Loads the databases and then automagically will provide questions as requested
'''
import json

from question_class import QuestionClass
from random import randrange

class DatabaseAccessor(object):
    database_list = list()
    def __init__(self):
        with open('databases/db_airlaw.json', 'r') as f:
            self.database_list.append(json.load(f))

    def get_random_question(self):
        # We need to add something that keeps track of which questions we've provided so we don't have duplicates.
        num_questions = len(self.database_list[0])
        rand_index = randrange(num_questions)
        return QuestionClass(self.database_list[0][rand_index])

    def get_random_question_from(self, database_name):
        # Not sure how this will actually work in the end
        pass

    def get_question(self, database_name, question_name):
        # Even more not sure how this will work
        pass

    def add_question(self, database_name):
        # Is there even a point to this?
        pass


if __name__ == '__main__':
    database = DatabaseAccessor()
    question = database.get_random_question()
    print question
    try:
        answerIndex = int(raw_input("Answer: "))
    except:
        pass
    finally:
        if question.check_answer(answerIndex-1):
            print "Correct!"
        else:
            print "INCORRECT"

