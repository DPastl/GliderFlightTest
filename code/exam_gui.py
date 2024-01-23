'''
A simple multiple choice exam GUI in Tk to provide simple cross-platform support.
This GUI makes use of the exam class to manage the question/answer management and
simply creates the GUI and passes events to the exam class when required.

Requirements:
    * Tkinter

The GUI takes in a set of databases selected by the user and creates a randomized
test of 50 questions. The user can go back and forth within the list of questions
and answer them in any order they wish to. Once all questions have been answered
a score is computed and displayed to the user. Finally, the user can either quit
or do another test. Answered questions cannot be modified as the list of which
questions have been answered is updated each time the user answers and question.

The exam GUI is stateful and waits for events passed to it from the tkinter
window manager.

Row and column sizes are set manually as there does not appear to be an option to
expand to fit the window in tkinter, thus for each question the button placement
would change without this.
'''

import Tkinter as Tk
import exam
from database_accessor import database_file_enum

class ExamGui():
    ######################## Class Constants #######################

    exterior_window_width = 600
    interior_window_width = 570
    num_questions = 50

    ######################## Class Constructor #######################

    def __init__(self, window):
        """
        Initialize the exam GUI with the provided Tkinter window
        :param window: A Tk window object
        """
        self._window = window
        # Create a list to keep track of which databases are available and a lit to track
        # a list to track which databases were selected.
        self.database_file_names = database_file_enum.keys()
        self.checkbox_list = [Tk.IntVar() for _ in range(len(self.database_file_names))]
        for item in self.checkbox_list:
            item.set(True)

        self.display_startup()

    ######################## Window Creation #######################

    def display_startup(self):
        """
        Creates the initial frame of the application. This view will show the
        user the list of possible databases to be tested on and allow them to select
        which databases they want to use. Two buttons are provided to allow the user
        to indicate they wish to start the test or to quit the application. When the user
        chooses to start the test, the currently selected checkboxes for each database
        are verified and make into a list which is used to create the exam.
        """
        self._window.minsize(width=self.exterior_window_width, height=230)
        self._window.maxsize(width=self.exterior_window_width, height=400)

        self.frame = Tk.Frame(self._window)

        # Create the grid of rows and columns used to place visual elements on the frame
        self.frame.grid(sticky=Tk.N + Tk.S + Tk.E + Tk.W)
        self.frame.grid_columnconfigure(0, minsize=300)
        self.frame.grid_columnconfigure(1, minsize=300)
        self.frame.grid_rowconfigure(0, minsize=80)
        self.frame.grid_rowconfigure(1, minsize=60)
        self.frame.grid_rowconfigure(2, minsize=30)
        self.frame.grid_rowconfigure(3, minsize=30)
        self.frame.grid_rowconfigure(4, minsize=30)
        self.frame.grid_rowconfigure(5, minsize=30)
        self.frame.grid_rowconfigure(6, minsize=30)

        # Create the text shown to the user on boot

        self.label = Tk.Label(self.frame, text="Welcome to the Glider Exam Generator")
        self.label.grid(row=0, columnspan=2, sticky=Tk.N + Tk.S + Tk.E + Tk.W)

        self.label = Tk.Label(self.frame, text="Select the databases to use:")
        self.label.grid(row=1, columnspan=2, sticky=Tk.N + Tk.S + Tk.E + Tk.W)

        # Add checkboxes for each database

        for index in range(len(self.database_file_names)):
            checkbutton = Tk.Checkbutton(self.frame, text=self.database_file_names[index],
                                         variable=self.checkbox_list[index])
            checkbutton.grid(row=int(index / 2) + 2, column=index % 2, sticky=Tk.N + Tk.S + Tk.E + Tk.W)

        # Create buttons

        self.button = Tk.Button(
            self.frame, text="Start Test", command=self.start_test
        )
        self.button.grid(row=6, column=0, sticky=Tk.N + Tk.S + Tk.E + Tk.W)

        self.button = Tk.Button(
            self.frame, text="QUIT", fg="red", command=self.frame.quit
        )
        self.button.grid(row=6, column=1, sticky=Tk.N + Tk.S + Tk.E + Tk.W)


    def create_test_frame(self):
        """
        Creates the frame displaying a question and the potential answers. The question
        is pulled from the exam object associated with this class. The user may choose
        to advance to the next question, view the previous question, answer the question
        using the currently selected radio button, or to quit the exam.
        """
        # Determine how many answers there are for the current question
        self.num_answers = len(self._exam.question_list[self._exam.current_question_index].answers)

        self.frame.destroy()
        self.frame = Tk.Frame(self._window)

        # Create the grid of rows and columns used to place visual elements on the frame
        self.frame.grid(sticky=Tk.N + Tk.S + Tk.E + Tk.W)
        self.frame.grid_columnconfigure(0, minsize=150)
        self.frame.grid_columnconfigure(1, minsize=150)
        self.frame.grid_columnconfigure(2, minsize=150)
        self.frame.grid_columnconfigure(3, minsize=150)

        self.frame.grid_rowconfigure(0, minsize=80)
        for i in range(self.num_answers):
            self.frame.grid_rowconfigure(1 + i, minsize=45)
        self.frame.grid_rowconfigure(5, minsize=30)

        # Displays the question index number and the question itself
        question_num = "Question {0}:\n".format(self._exam.current_question_index + 1)
        question_text = self._exam.get_current_question_text()
        self.question_label = Tk.Label(self.frame, text=(question_num + question_text[0]),
                                       justify=Tk.LEFT, anchor=Tk.W,
                                       wraplength=self.interior_window_width)
        self.question_label.grid(row=0, column=0, columnspan=4, sticky=Tk.N + Tk.S + Tk.E + Tk.W)
        self.radio_buttons = list()
        self.answer_index = Tk.IntVar()

        # Determine how many answers there are for the current question
        self.num_answers = len(self._exam.question_list[self._exam.current_question_index].answers)

        # Create the radio buttons
        for i in range(self.num_answers):
            self.radio_buttons.append(Tk.Radiobutton(
                self.frame, text=question_text[i + 1], variable=self.answer_index,
                justify=Tk.LEFT, value=i, wraplength=self.interior_window_width))

        # Apply them to the grid to display them to user
        for i in range(self.num_answers):
            self.radio_buttons[i].grid(row=i + 1, column=0, columnspan=4, sticky=Tk.N + Tk.S + Tk.E + Tk.W)

        self.radio_buttons[0].select()  # Select the first radio button as the currently selected answer

        # Draw the buttons

        self.prev_button = Tk.Button(
            self.frame, text="Prev", command=self.prev_question)
        self.prev_button.grid(row=5, column=0, sticky=Tk.N + Tk.S + Tk.E + Tk.W)
        self.prev_button.config(width=15)

        self.answer_button = Tk.Button(
            self.frame, text="Next", command=self.next_question)        
        self.answer_button.grid(row=5, column=1, sticky=Tk.N + Tk.S + Tk.E + Tk.W)
        self.answer_button.config(width=15)

        self.answer_button = Tk.Button(
            self.frame, text="Answer", command=self.answer_question)
        self.answer_button.grid(row=5, column=2, sticky=Tk.N + Tk.S + Tk.E + Tk.W)
        self.answer_button.config(width=15)

        self.quit_button = Tk.Button(
            self.frame, text="QUIT", fg="red", command=self.frame.quit)
        self.quit_button.grid(row=5, column=3, sticky=Tk.N + Tk.S + Tk.E + Tk.W)
        self.quit_button.config(width=15)

    def create_results_frame(self):
        """
        Creates the final results frame for the user, showing the users score
        and allow the user to select between starting a new test and exiting the
        application.
        """
        self.frame.destroy()
        self.frame = Tk.Frame(self._window) # Create a new blank frame after destroying the current one

        # Create the grid of rows and columns used to place visual elements on the frame
        self.frame.grid(sticky=Tk.N + Tk.S + Tk.E + Tk.W)
        self.frame.grid_columnconfigure(0, minsize=300)
        self.frame.grid_columnconfigure(1, minsize=300)
        self.frame.grid_rowconfigure(0, minsize=130)
        self.frame.grid_rowconfigure(1, minsize=130)
        self.frame.grid_rowconfigure(2, minsize=30)

        # Fill in the text to display to the user
        result_label = Tk.Label(self.frame, text="Test Results:")
        result_label.grid(row=0, column=0, columnspan=2)

        result_label = Tk.Label(self.frame, text="Score: {0}%".format(self._exam.get_percent()))
        result_label.grid(row=1, column=0, columnspan=2)

        # Create the buttons

        quit_button = Tk.Button(
            self.frame, text="QUIT", fg="red", command=self.frame.quit
        )
        quit_button.grid(row=2, column=0, sticky=Tk.N + Tk.S + Tk.E + Tk.W)

        self.new_button = Tk.Button(
            self.frame, text="New Test", command=self.start_test
        )
        self.new_button.grid(row=2, column=1, sticky=Tk.N + Tk.S + Tk.E + Tk.W)

    ######################## Window Updating #######################

    def update_test_frame(self):
        """
        Updates the already created list of radio buttons and the question label
        to show the user the currently selected question, rather than destroying
        the frame and redrawing it.
        """
        question_num = "Question {0}:\n".format(self._exam.current_question_index + 1)
        question_text = self._exam.get_current_question_text()
        self.question_label.configure(text=(question_num + question_text[0]))
        default_bg = self._window.cget('bg')
        
        # Determine how many answers there are for the current question
        self.num_answers = len(self._exam.question_list[self._exam.current_question_index].answers)

        # Update the radio button text with the new possible answers to the question
        for i in range(self.num_answers):
            self.radio_buttons[i].configure(text=question_text[i + 1], bg=default_bg)

        # Check if the user has answered this question
        if self._exam.answer_list[self._exam.current_question_index] is not None:
            if self.user_answers[self._exam.current_question_index] is not None:
                self.radio_buttons[self.user_answers[self._exam.current_question_index]].configure(bg='red')
            self.radio_buttons[self._exam.get_correct_answer() - 1].configure(bg='green')

    ######################## Events #######################

    def start_test(self):
        # Destroy the old frame and make a new one
        self.frame.destroy()

        # Select the databases to use based on the user's selection
        database_list = list()
        for index in range(len(self.checkbox_list)):
            if self.checkbox_list[index].get():
                database_list.append(self.database_file_names[index])

        # Create the exam test object and have it generate the list of questions the draw the test frame
        self._exam = exam.Exam(self.num_questions, database_list)
        self._exam.next_question()  # Advances to the first question
        self.create_test_frame()  # Draws the frame for the first question
        # Creates a local list of answered used to populate the answer when the user
        # selects a previous question
        self.user_answers = [None for _ in range(self.num_questions)]

    def answer_question(self):
        """
        Inspects the currently selected radio button and then updates the list of
        answers and the exam test object
        """
        # Check if question was already answered.
        if self._exam.answer_list[self._exam.current_question_index] is not None:
            pass
        else:
            self.user_answers[self._exam.current_question_index] = self.answer_index.get()
            # If it wasn't, then check the inputted answer.
            if not self._exam.answer_current_question(self.answer_index.get() + 1):
                # Make incorrect answer turn red
                self.radio_buttons[self.answer_index.get()].configure(bg='red')
            # Display correct answer
            self.radio_buttons[self._exam.get_correct_answer() - 1].configure(bg='green')

    def next_question(self):
        """
        Advances to the next question if one is still available and then redraws the frmae.
        If all the questions have been answered the results frame is drawn instead.
        :return:
        """
        if self._exam.next_question():
            self.update_test_frame()
        else:
            self.create_results_frame()

    def prev_question(self):
        """
        Returns to a previously viewed question and redraws the frame.
        """
        if self._exam.prev_question():
            self.update_test_frame()


#######################################################

if __name__ == '__main__':
    """
    Create the Tkinter window, then start the exam gui
    """
    root = Tk.Tk()

    app = ExamGui(root)
    root.wm_title("Glider Exam Generator")
    root.mainloop()
