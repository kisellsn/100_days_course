class QuizBrain:
    score = 0
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0

    def next_question(self):
        curr_question =  self.question_list[self.question_number]
        self.question_number += 1

        user_answer = input(f"Q.{self.question_number}: {curr_question.question} (True/False)?: ")
        self.check_answer(user_answer, curr_question.answer)

        print(f"Your score is {self.score}/{self.question_number}\n")

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, real_answer):
        if user_answer.lower() == real_answer.lower():
            print("Correct!")
            self.score += 1
        else:
            print("Incorrect!")