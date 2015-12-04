'''
    A simple template for the database class that demonstrates how to generate a database file

    Naming convention:
    datebase filenames will have the form "db_<nameofdatabase>.py" so that
    the scripts can easily determine what is a database and what isn't.

    Each question should be formatted as a dictionary:

    question = {
        "questions": ["Question 1 text","Question 2 Text", ...],
        "answerIndex": <index in above array of the answer>,
        "answerText": "Text for the answer"
    }

    This is then saved in json format.  Possibly.  It might just be easier to have them all as dictionaries with a number
    as the question.
'''

sample_question = {
    "questions": ["What... is your name?", "What... is your quest?",
                  "What... is the air-speed velocity of an unladen swallow?"],
    "answerIndex": 2,
    "answerText": "What do you mean? An African or a European swallow?"
}
