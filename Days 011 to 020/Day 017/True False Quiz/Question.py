class Question:
    def __init__(self, question_id: int, question_text: str, question_answer: bool):
        self.id: int = question_id
        self.text: str = question_text
        self.answer: bool = question_answer

    def check_answer_is_correct(self, user_answer: True) -> bool:
        return self.answer == user_answer
