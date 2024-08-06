import html

class QuizBrain:
    score = 0
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0

    def next_question(self):
        self.curr_question =  self.question_list[self.question_number]
        self.question_number += 1

        q_text = html.unescape(self.curr_question.question)
        return f"Q.{self.question_number}: {q_text} (True/False)?"

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer):
        if user_answer.lower() == self.curr_question.answer.lower():
            self.score += 1
            return True
        return False