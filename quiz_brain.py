class QuizBrain:
    def __init__(self, question_bank):
        self.question_list = question_bank
        self.question_number = 0
        self.score = 0

    def next_question(self):
        next_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q{self.question_number}: {next_question.text}. (True/False): ").lower().capitalize()
        self.check_answer(user_answer, next_question.answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
        # return self.question_number < 3

    def check_answer(self, guess, answer):
        if guess == answer:
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")

        print(f"The correct answer was: {answer}")
        print(f"Score: {self.score}/{self.question_number}\n")
