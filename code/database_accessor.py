'''
A class that handles the getting a setting of questions in the databases.

Loads the databases and then automagically will provide questions as requested
'''
import json
from random import randrange, choice

from question_class import QuestionClass

database_root_dir = 'databases'
database_file_enum = {
    'airlaw': 'db_airlaw.json',
    'flight_theory': 'db_flight_theory.json',
    'metrology': 'db_metrology.json',
    'navigation': 'db_navigation.json'
}

class DatabaseAccessor(object):
    database_list = {}
    allow_duplicates = False

    def __init__(self, database_to_use='all', allow_duplicates=False):
        self.allow_duplicates = allow_duplicates
        if database_to_use == 'all':
            for database_name, database_file_name in database_file_enum.iteritems():
                with open(database_root_dir + '/' + database_file_name, 'r') as f:
                    self.database_list[database_name] = json.load(f)
        else:
            if database_to_use not in database_file_enum.keys():
                raise Exception("Database name not in list!")
            else:
                with open(database_root_dir + '/' + database_file_enum[database_to_use], 'r') as f:
                    self.database_list[database_to_use] = json.load(f)

    def get_num_questions(self):
        num_questions = 0
        for x in self.database_list.keys():
            num_questions += len(self.database_list[x])
        return num_questions

    def get_random_question(self):
        # We need to add something that keeps track of which questions we've provided so we don't have duplicates.
        # or just not care that there might be duplicates
        random_database = choice(database_file_enum.keys())
        num_questions = len(self.database_list[random_database])
        rand_index = randrange(num_questions)
        return QuestionClass(self.database_list[random_database][rand_index])

    def get_random_question_from(self, database_name):
        if database_name not in database_file_enum.keys():
            raise Exception("Database name not in list!")
        num_questions = len(self.database_list[database_name])
        rand_index = randrange(num_questions)
        return QuestionClass(self.database_list[database_name][rand_index])

    def get_question(self, database_name, question_name):
        # Even more not sure how this will work
        pass

    def add_question(self, database_name):
        # Is there even a point to this?
        pass


if __name__ == '__main__':
    database = DatabaseAccessor()
    print database.get_num_questions()
    question = database.get_random_question()
    print question
    answer_index = None
    try:
        answer_index = int(raw_input("Answer: "))
    except:
        pass
    finally:
        if answer_index is not None:
            if question.check_answer(answer_index - 1):
                print "Correct!"
            else:
                print "INCORRECT"
