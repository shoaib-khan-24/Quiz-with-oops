from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    new_question = Question(question["text"] , question["answer"])
    question_bank.append(new_question)

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_have_questions():
    quiz_brain.next_question()

print("***  You have completed the quiz  ***")
print(f"Your final score is {quiz_brain.score} out of {len(question_bank)}")

