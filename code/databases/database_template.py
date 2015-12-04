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

    This is then saved in json format as a list of dictionaries.  We don't care how they are ordered and we can search
    for them based on the answer or the question so that should work.

    Might consume too much memory if we're loading a large database into memory, since we load every question.

    Also need to make a simple writing function to add to databases
'''

sample_question = {
    "question": "These are questions?",
    "answers": ["What... is your name?", "What... is your quest?",
                  "What... is the air-speed velocity of an unladen swallow?"],
    "correctAnswerIndex": 2,
    "correctAnswerText": "What do you mean? An African or a European swallow?"
}

# becomes when put through the json.dumps formatter.
[
    {
        "correctAnswerText": "What do you mean? An African or a European swallow?",
        "question": "These are questions?",
        "correctAnswerIndex": 2,
        "answers": [
            "What... is your name?",
            "What... is your quest?",
            "What... is the air-speed velocity of an unladen swallow?"
        ]
    }
]
