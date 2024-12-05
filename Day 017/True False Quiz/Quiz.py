from Question import Question
from Util import clear_screen
from User import User


class Quiz:
    def __init__(self, questions: list[Question]):
        self.questions = questions
        self.current_player = User()
        self.results: list[dict] = []

    def add_question_result(self, question_id: int, is_correct: bool):
        self.results.append({"id": question_id, "correct": "✔" if is_correct else "X"})

    def get_results(self):
        print("-" * 60)
        print(f"Name: {self.current_player.username}")
        print(f"Score: {self.current_player.score} / {len(self.questions)}")
        for result in self.results:
            print(f"Question {result["id"]}: {result['correct']}")
        print("-" * 60)

    def ask_questions(self, question_number: int):
        while True:
            print(f"{self.questions[question_number].id} - {self.questions[question_number].text}.", end=" ")
            print("True or False? ")
            user_input = input().strip().lower()
            match user_input:
                case "true" | "1":
                    is_correct = self.questions[question_number].check_answer_is_correct(True)
                    self.current_player.score += 1 if is_correct else 0
                    self.add_question_result(self.questions[question_number].id, is_correct)
                    return
                case "false" | "0":
                    is_correct = self.questions[question_number].check_answer_is_correct(False)
                    self.current_player.score += 1 if is_correct else 0
                    self.add_question_result(self.questions[question_number].id, is_correct)
                    return
                case _:
                    print("Sorry, that's not a valid option. Try again.")
                    clear_screen()
