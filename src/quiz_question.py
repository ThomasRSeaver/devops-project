class quiz_question:
    def __init__(self, question_text, answer_text, wrong1, wrong2, wrong3):
        self.question_text = question_text
        self.answer_text = answer_text
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

    def get_options(self):
        return [self.answer_text, self.wrong1, self.wrong2, self.wrong3]