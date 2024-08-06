from day_34_quiz.data import question_data
from day_34_quiz.ui import QuizInterface
from question_model import Question
from quiz_brain import QuizBrain

def create_questions(data):
    questions = []
    for question in data:
        question_text = question["question"]
        answer = question["correct_answer"]

        questions.append(Question(question=question_text, answer=answer))

    return questions

if __name__ == "__main__":
    questions = create_questions(question_data)

    quiz = QuizBrain(questions)

    window = QuizInterface(quiz)

