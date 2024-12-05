from Question import Question
from Util import clear_screen
from User import User


class Quiz:
    def __init__(self, questions: list[Question]):
        self.questions = questions
        self.current_player = User()
        self.results: list[dict] = []

    def start_quiz(self):
        for i in range(len(self.questions)):
            if self.ask_questions(i) == "QUIT":
                self.add_remaining_results()
                clear_screen()
                return
            clear_screen()

    def add_remaining_results(self):
        remaining = len(self.questions) - len(self.results)
        for i in range(remaining):
            question_id: int = len(self.results)+1
            self.results.append({"id": question_id, "correct": "X"})

    def add_question_result(self, question_id: int, is_correct: bool):
        self.results.append({"id": question_id, "correct": "✔" if is_correct else "X"})

    def get_results(self):
        print("-" * 60)
        print(f"Name: {self.current_player.username}")
        print(f"Score: {self.current_player.score} / {len(self.questions)}")
        for result in self.results:
            print(f"Question {result["id"]}: {result['correct']}")
        print("-" * 60)

    def ask_questions(self, question_number: int) -> None or str:
        """
        Asks each question

        Parameters:
            question_number (int): The question number

        Returns:
            - None if question is answered
            - "QUIT" if user quits
        """
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
                case "quit":
                    return "QUIT"
                case _:
                    clear_screen()
                    print("Sorry, that's not a valid option. Try again.", end="\n\n")

