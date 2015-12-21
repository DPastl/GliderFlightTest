import Tkinter as Tk

import exam


class ExamGui():
    answer_index = 0

    def __init__(self, master):
        self._master = master
        self.display_startup()

    ######################## Window Creation #######################

    def display_startup(self):
        self.frame = Tk.Frame(self._master)
        self.frame.pack()

        self.label = Tk.Label(self.frame, text="Welcome to the Glider Exam Generator")
        self.label.pack()
        self.button = Tk.Button(
            self.frame, text="QUIT", fg="red", command=self.frame.quit
        )
        self.button.pack(side=Tk.RIGHT)
        self.button = Tk.Button(
            self.frame, text="Start Test", command=self.start_test
        )
        self.button.pack(side=Tk.LEFT)

    def create_test_frame(self):
        self.frame = Tk.Frame(self._master, width=500, height=300)
        self.frame.pack()
        question_text = self._exam.get_current_question_text()
        self.question_label = Tk.Label(self.frame, text=question_text[0])
        self.question_label.pack()
        self.radio_buttons = list()
        for answer_text in question_text[1:5]:
            self.radio_buttons.append(Tk.Radiobutton(
                self.frame, text=answer_text, variable=self.answer_index))

        for radio_button in self.radio_buttons:
            radio_button.pack()

        self.answer_button = Tk.Button(
            self.frame, text="Answer", command=self.answer_question
        )
        self.answer_button.pack(side=Tk.RIGHT)

    def create_results_frame(self):
        self.frame = Tk.Frame(self._master)
        self.frame.pack()

    ######################## Window Updating #######################

    def update_test_frame(self):
        question_text = self._exam.get_current_question_text()
        # self.question_label
        # for radio_button in self.radio_buttons:
        #     pass
        pass

    ######################## Events #######################

    def start_test(self):
        # Destroy the old frame and make a new one
        self.frame.destroy()

        self._exam = exam.Exam()  # Create a list of questions
        self._exam.next_question()
        self.create_test_frame()

    def answer_question(self):
        # Display to user if the test passed or failed
        # Display correct answer
        # Move to next question
        # Update the GUI
        pass


#######################################################

if __name__ == '__main__':
    root = Tk.Tk()

    app = ExamGui(root)

    root.mainloop()
    root.destroy()  # optional; see description below
