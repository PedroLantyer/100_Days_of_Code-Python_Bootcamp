from Data import question_data
from Question import Question
from Quiz import Quiz
from Util import clear_screen
import random


def set_questions() -> list[Question] | None:
    """
    Create an Array containing all questions
    """
    try:
        question_arr: list[dict] = question_data
        randomized_questions: list[Question] = []
        random.shuffle(question_arr)
        for i in range(len(question_arr)):
            question_arr[i]["id"] = i+1

        for question in question_arr:
            question_obj = Question(question["id"], question["text"], question["answer"])
            randomized_questions.append(question_obj)
        random.shuffle(question_arr)

        return randomized_questions
    except Exception as error:
        print(error)
        return None


if __name__ == '__main__':
    question_bank: list[Question] = set_questions()
    if question_bank is None:
        print("Failed to get questions")
        exit(1)

    quiz = Quiz(question_bank)
    quiz.start_quiz()
    clear_screen()
    quiz.get_results()
    input("Press anything to exit the program...")
