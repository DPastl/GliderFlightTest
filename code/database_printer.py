"""
Utility to print out all the questions and answers into a
large pdf to allow easier reading over and verification
of the question database
"""

from pylatex import Document, Section, Enumerate
from pylatex.utils import bold
from database_accessor import DatabaseAccessor, database_file_enum

def fill_document_from_database(doc, database):
    """
    Adds questions and answers to the document
    :param doc: The pylatex document
    :param database: The database name to use to fill the document
    """
    db = DatabaseAccessor(database_to_use=[database])
    print database, db.get_num_questions()
    with doc.create(Enumerate()) as qenum:
        for question in db.question_list:
            qenum.add_item(question.get_question_text().decode('utf-8'))
            with doc.create(Enumerate()) as enum:
                alist = question.get_list_of_answers()
                for i in range(len(alist)):
                    if i == (question.get_correct_answer() -1):
                        enum.add_item(bold(alist[i].decode('utf-8')))
                    else:
                        enum.add_item(alist[i].decode('utf-8'))

if __name__ == '__main__':
    doc = Document('database_questions')
    for database in database_file_enum:
        with doc.create(Section(database, numbering=True)):
            fill_document_from_database(doc, database)
    doc.generate_tex()