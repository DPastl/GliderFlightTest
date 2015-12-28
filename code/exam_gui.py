import Tkinter as Tk

import exam

'''
A simple exam GUI.

Row and column sizes are set manually as there does not appear to be an option to
expand to fit the window in tkinter, thus for each question the button placement
would change without this.
'''

class ExamGui():


    def __init__(self, master):
        self._master = master
        self.display_startup()

    ######################## Window Creation #######################

    def display_startup(self):
        self._master.minsize(width=600, height=230)
        self._master.maxsize(width=600, height=400)

        self.frame = Tk.Frame(self._master)
        self.frame.grid(sticky=Tk.N + Tk.S + Tk.E + Tk.W)
        self.frame.grid_columnconfigure(0, minsize=300)
        self.frame.grid_columnconfigure(1, minsize=300)
        self.frame.grid_rowconfigure(0, minsize=200)
        self.frame.grid_rowconfigure(1, minsize=30)

        self.label = Tk.Label(self.frame, text="Welcome to the Glider Exam Generator")
        self.label.grid(row=0, columnspan=2, sticky=Tk.N + Tk.S + Tk.E + Tk.W)

        self.button = Tk.Button(
            self.frame, text="Start Test", command=self.start_test
        )
        self.button.grid(row=1, column=0, sticky=Tk.N + Tk.S + Tk.E + Tk.W)

        self.button = Tk.Button(
            self.frame, text="QUIT", fg="red", command=self.frame.quit
        )
        self.button.grid(row=1, column=1, sticky=Tk.N + Tk.S + Tk.E + Tk.W)


    def create_test_frame(self):
        self.frame.destroy()
        self.frame = Tk.Frame(self._master)
        self.frame.grid(sticky=Tk.N + Tk.S + Tk.E + Tk.W)

        self.frame.grid_columnconfigure(0, minsize=200)
        self.frame.grid_columnconfigure(1, minsize=200)
        self.frame.grid_columnconfigure(2, minsize=200)
        self.frame.grid_rowconfigure(0, minsize=80)
        self.frame.grid_rowconfigure(1, minsize=30)
        self.frame.grid_rowconfigure(2, minsize=30)
        self.frame.grid_rowconfigure(3, minsize=30)
        self.frame.grid_rowconfigure(4, minsize=30)
        self.frame.grid_rowconfigure(5, minsize=30)

        question_text = self._exam.get_current_question_text()
        self.question_label = Tk.Label(self.frame, text=question_text[0],
                                       justify=Tk.LEFT, anchor=Tk.W,
                                       wraplength=600)
        self.question_label.grid(row=0, columnspan=3, sticky=Tk.N + Tk.S + Tk.E + Tk.W)
        self.radio_buttons = list()
        self.answer_index = Tk.IntVar()

        # Determine how many answers there are for the current question
        self.num_answers = len(self._exam.question_list[self._exam.current_question_index].answers)

        for i in range(self.num_answers):
            self.radio_buttons.append(Tk.Radiobutton(
                self.frame, text=question_text[i + 1], variable=self.answer_index,
                justify=Tk.LEFT, value=i))

        for i in xrange(self.num_answers):
            self.radio_buttons[i].grid(row=i + 1, columnspan=3, sticky=Tk.N + Tk.S + Tk.E + Tk.W)

        self.radio_buttons[0].select()

        self.answer_button = Tk.Button(
            self.frame, text="Next", command=self.next_question
        )
        self.answer_button.grid(row=5, column=0, sticky=Tk.N + Tk.S + Tk.E + Tk.W)

        self.answer_button = Tk.Button(
            self.frame, text="Answer", command=self.answer_question
        )
        self.answer_button.grid(row=5, column=1, sticky=Tk.N + Tk.S + Tk.E + Tk.W)

        self.quit_button = Tk.Button(
            self.frame, text="QUIT", fg="red", command=self.frame.quit
        )
        self.quit_button.grid(row=5, column=2, sticky=Tk.N + Tk.S + Tk.E + Tk.W)

    def create_results_frame(self):
        self.frame.destroy()
        self.frame = Tk.Frame(self._master)
        self.frame.grid(sticky=Tk.N + Tk.S + Tk.E + Tk.W)

        self.frame.grid_columnconfigure(0, minsize=300)
        self.frame.grid_columnconfigure(1, minsize=300)
        self.frame.grid_rowconfigure(0, minsize=100)
        self.frame.grid_rowconfigure(1, minsize=100)
        self.frame.grid_rowconfigure(2, minsize=30)

        result_label = Tk.Label(self.frame, text="Test Results:")
        result_label.grid(row=0, column=0, columnspan=2)

        result_label = Tk.Label(self.frame, text="Score: {0}%".format(self._exam.get_percent()))
        result_label.grid(row=1, column=0, columnspan=2)

        quit_button = Tk.Button(
            self.frame, text="QUIT", fg="red", command=self.frame.quit
        )
        quit_button.grid(row=2, column=0, sticky=Tk.N + Tk.S + Tk.E + Tk.W)

        self.new_button = Tk.Button(
            self.frame, text="New Test", command=self.answer_question
        )
        self.new_button.grid(row=2, column=1, sticky=Tk.N + Tk.S + Tk.E + Tk.W)

    ######################## Window Updating #######################

    def update_test_frame(self):
        # Updates the already created list of radio buttons and question label
        question_text = self._exam.get_current_question_text()
        self.question_label.configure(text=question_text[0])
        default_bg = self._master.cget('bg')
        
        # Determine how many answers there are for the current question
        self.num_answers = len(self._exam.question_list[self._exam.current_question_index].answers)
        
        for i in range(self.num_answers):
            self.radio_buttons[i].configure(text=question_text[i + 1], bg=default_bg)

    ######################## Events #######################

    def start_test(self):
        # Destroy the old frame and make a new one
        self.frame.destroy()

        self._exam = exam.Exam()  # Create a list of questions
        self._exam.next_question()
        self.create_test_frame()

    def answer_question(self):
        print self.answer_index.get()
        if not self._exam.answer_current_question(self.answer_index.get() + 1):
            # Make incorrect answer turn red
            self.radio_buttons[self.answer_index.get()].configure(bg='red')
        # Display correct answer
        print self._exam.get_correct_answer() - 1
        self.radio_buttons[self._exam.get_correct_answer() - 1].configure(bg='green')

    def next_question(self):
        if self._exam.next_question():
            self.update_test_frame()
        else:
            self.create_results_frame()


#######################################################

if __name__ == '__main__':
    root = Tk.Tk()

    app = ExamGui(root)
    root.wm_title("Glider Exam Generator")
    root.mainloop()
    root.destroy()  # optional; see description below
