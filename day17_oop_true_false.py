from day17_data import *
from day17_question_model import *
from day17_quiz_brain import *
class Question:
    def __init__(self,text,answer):
        self.text = text
        self.answer = answer

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")