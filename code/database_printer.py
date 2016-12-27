"""
Utility to print out all the questions and answers into a
large pdf to allow easier reading over and verification
of the question database
"""

from pylatex import Document, Section, Subsection, Enumerate
from pylatex.utils import italic, NoEscape
from database_accessor import DatabaseAccessor

def fill_document_from_database(doc, database):
    """
    Adds questions and answers to the document
    :param doc: The pylatex document
    :param database: The database name to use to fill the document
    """
    db = DatabaseAccessor(database_to_use=[database])
    for question in db.question_list:
        with doc.create(Subsection(question.get_question_text().decode('utf-8'), numbering=True)):
            with doc.create(Enumerate()) as enum:
                for answer in question.get_list_of_answers():
                    enum.add_item(answer.decode('utf-8'))



if __name__ == '__main__':
    doc = Document('database_questions')
    with doc.create(Section('Airlaw', numbering=True)):
        fill_document_from_database(doc, 'airlaw')

    with doc.create(Section('Navigation', numbering=True)):
        fill_document_from_database(doc, 'navigation')

    with doc.create(Section('Metrology', numbering=True)):
        fill_document_from_database(doc, 'metrology')

    with doc.create(Section('Flight Theory', numbering=True)):
        fill_document_from_database(doc, 'flight_theory')

    with doc.create(Section('Instruments', numbering=True)):
        fill_document_from_database(doc, 'instruments')

    with doc.create(Section('Flight Operations', numbering=True)):
        fill_document_from_database(doc, 'flight_operations')

    with doc.create(Section('Human Factors', numbering=True)):
        fill_document_from_database(doc, 'human_factors')

    with doc.create(Section('Radio', numbering=True)):
        fill_document_from_database(doc, 'radio')


    doc.generate_tex()