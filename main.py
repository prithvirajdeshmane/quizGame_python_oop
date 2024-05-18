from question_model import Question
from data2 import question_data
from quiz_brain import QuizBrain

question_bank = []

for entry in question_data:
    # new_question = Question(entry["text"], entry["answer"])
    new_question = Question(entry["question"], entry["correct_answer"])
    question_bank.append(new_question)

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print("You've completed the quiz!")
print(f"Your final score was {quiz_brain.score}/{quiz_brain.question_number}")
