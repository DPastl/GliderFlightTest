'''
A class that handles the getting a setting of questions in the databases.

Loads the databases and then automagically will provide questions as requested
'''
import json

from databases.db_test import db_test
from question_class import QuestionClass


class DatabaseAccessor():
    database_list = list()
    def __init__(self):
        # this isn't working correctly
        self.database_list.append(json.loads(db_test))

    def get_random_question(self):
        return QuestionClass(self.database_list[0])

    def get_random_question_from(self, database_name):
        pass

    def get_question(self, database_name, question_name):
        pass

    def add_question(self, database_name):
        pass


if __name__ == '__main__':
    database = DatabaseAccessor()
    print database.get_random_question()
