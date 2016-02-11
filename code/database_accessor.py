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
    'human_factors': 'db_human_factors.json'
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
                    db_contents = json.load(f)
                    valid = ValidateDatabase(db_contents)
                    if valid.valid:
                        self.database_list[database_name] = db_contents
                    else:
                        print database_name
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

    # This method randomly selects a question from a database.
    def get_random_question(self, db_name=None):
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


# This method validates the contents of a database file. Makes sure
# each required field is there and verifies the type of the contents
# of each field. This method is not part of the DatabaseAccessor 
# class.
class ValidateDatabase(object):
    def __init__(self, database):

        # Initialize variables needed to perform checks.
        self.num_answers = 4
        required_fields = {"question": self.validate_string,
                           "answers": self.validate_list_of_strings,
                           "correctAnswerIndex": self.validate_number_answers,
                           "questionSource": self.validate_string
                           }
        optional_fields = {"correctAnswerText": self.validate_string}

        # Check that all required fields are present
        self.missing_fields = list()
        self.invalid_field_contents = list()
        self.valid = False

        # First check for required fields and validate contents.
        for question in database:
            for key in required_fields.keys():
                if key not in question.keys():
                    self.missing_fields.append(key)
                else:
                    if not required_fields[key](question[key]):
                        self.invalid_field_contents.append(key)

            # Now check for optional fields and validate contents.
            for key in optional_fields.keys():
                if key in question.keys():
                    if not optional_fields[key](question[key]):
                        self.invalid_field_contents.append(key)

        if (len(self.missing_fields) == 0) and (len(self.invalid_field_contents) == 0):
            self.valid = True

    # Check whether input is a str or unicode
    def validate_string(self, s):
        return isinstance(s, (str, unicode))


        # Check whether input is a list of str or unicode

    def validate_list_of_strings(self, s):
        valid = False
        if isinstance(s, list):
            valid = True
            for x in s:
                if not isinstance(x, (str, unicode)):
                    valid = False
        return valid

    # Check if input is int and in [0,1,2,3].
    def validate_number_answers(self, num):
        valid = False
        if isinstance(num, int):
            if (num >= 0) and (num < self.num_answers):
                valid = True
        return valid



if __name__ == '__main__':
    database = DatabaseAccessor()
    print "Number of questions in database: {0}".format(database.get_num_questions())
    # question = database.get_random_question()
    # print question
    # answer_index = None
    # try:
    #     answer_index = int(raw_input("Answer: "))
    # except:
    #     pass
    # finally:
    #     if answer_index is not None:
    #         if question.check_answer(answer_index - 1):
    #             print "Correct!"
    #         else:
    #             print "INCORRECT"
