<<<<<<< HEAD
class QuizBrain:
    def __init__(self, qlist):
        self.question_number = 0
        self.question_list = qlist
        self.score = 0
        self.trys = 0

    def increment_score(self):
        self.score += 1

    def increment_trys(self):
        self.trys += 1

    def increment_question_number(self):
        self.question_number += 1

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        question = input(
            f'Q.{self.question_number + 1}: {self.question_list[self.question_number].question}. (True/False)')
        if question == self.question_list[self.question_number].answer:
            print('You got it right!')
            self.increment_score()
            self.increment_trys()
            print(f'The correct answer was: {self.question_list[self.question_number].answer}')
            print(f'Your current score is {self.score}/{self.trys}')
            self.increment_question_number()
        else:
            print('You got it wrong!')
            print(f'Your current score is {self.score}/{self.trys}')
=======
class QuizBrain:
    def __init__(self, qlist):
        self.question_number = 0
        self.question_list = qlist
        self.score = 0
        self.trys = 0

    def increment_score(self):
        self.score += 1

    def increment_trys(self):
        self.trys += 1

    def increment_question_number(self):
        self.question_number += 1

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        question = input(
            f'Q.{self.question_number + 1}: {self.question_list[self.question_number].question}. (True/False)')
        if question == self.question_list[self.question_number].answer:
            print('You got it right!')
            self.increment_score()
            self.increment_trys()
            print(f'The correct answer was: {self.question_list[self.question_number].answer}')
            print(f'Your current score is {self.score}/{self.trys}')
            self.increment_question_number()
        else:
            print('You got it wrong!')
            print(f'Your current score is {self.score}/{self.trys}')
>>>>>>> bc3c9ccd99c84d30a2ffd9018f001e80e152ed8c
            self.increment_trys()