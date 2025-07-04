from data import question_data
from question_model import Question
from quiz_brain_module import QuizBrain

question_bank = []
for i in range(0,len(question_data)):
    question_bank.append(Question(str(question_data[i]['text']),str(question_data[i]['answer'])))

quizbrain = QuizBrain(question_bank)

while quizbrain.still_has_questions():
    quizbrain.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quizbrain.score}/{quizbrain.trys}")