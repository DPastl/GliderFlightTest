'''
A class that handles the getting and setting of questions in the databases.

Loads the databases and then automagically will provide questions as requested
'''
from question_class import QuestionClass

# The relative path to the root directory containing the .json
# question database files.
database_root_dir = 'databases'
# A dict() mapping the type of database to the appropriate .json
# database file. There are 8 sections of topics to study for. See
# the TC Study and Reference Guide.
database_file_enum = {
    'airlaw': 'db_airlaw.json',
    'navigation': 'db_navigation.json',
    'metrology': 'db_metrology.json',
    'flight_theory': 'db_flight_theory.json',
    'instruments': 'db_instruments.json',
    'flight_operations': 'db_flight_operations.json',
    'human_factors': 'db_human_factors.json',

}


# A class to handle parsing pulling questions from the database files.
class DatabaseAccessor(object):
    database_list = {}
    allow_duplicates = False

    def __init__(self, database_to_use='all', allow_duplicates=False):
        import json

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


    # This method randomly selects a question from a database.
    def get_random_question(self,db_name=None):
        # We need to add something that keeps track of which questions we've provided so we don't have duplicates.
        # or just not care that there might be duplicates
        # OR this can be handled by the Exam class.
        from random import choice

        # If database name is supplied, verify the name
        if db_name is not None:
            if db_name not in database_file_enum.keys():
                raise Exception("Database name not in list!")

        # If not specific database name is supplied, just grab
        # questions from a randomly chosen database.
        if db_name is None:
            db_name = choice(database_file_enum.keys())

        return QuestionClass(choice(self.database_list[db_name]))


if __name__ == '__main__':
    database = DatabaseAccessor()
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
