from day_34.data import question_data
from question_model import Question
from quiz_brain import QuizBrain

def create_questions(data):
    questions = []
    for question in data:
        question_text = question["text"]
        answer = question["answer"]

        questions.append(Question(question=question_text, answer=answer))

    return questions

if __name__ == "__main__":
    questions = create_questions(question_data)

    quiz = QuizBrain(questions)

    while quiz.still_has_questions():
        quiz.next_question()

