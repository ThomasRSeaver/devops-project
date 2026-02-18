# We need 3 things.
# 1. The question asked
# 2. Four potential answers
# 3. Which answer is correct

class quiz_question:
    def __init__(self, question_text, answer_text, wrong1, wrong2, wrong3):
        self.question_text = question_text
        self.answer_text = answer_text
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3