'''
A class that handles the getting a setting of questions in the databases.

Loads the databases and then automagically will provide questions as requested
'''
import json

from question_class import QuestionClass


class DatabaseAccessor():
    database_list = list()
    def __init__(self):
        with open('databases/db_test.json', 'r') as f:
            self.database_list.append(json.load(f))

    def get_random_question(self):
        print self.database_list[0][0]
        return QuestionClass(self.database_list[0][0])

    def get_random_question_from(self, database_name):
        pass

    def get_question(self, database_name, question_name):
        pass

    def add_question(self, database_name):
        pass


if __name__ == '__main__':
    database = DatabaseAccessor()
    print database.get_random_question()
