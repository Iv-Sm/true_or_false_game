import random
from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class Question:
    text: str
    is_true: bool
    explanation: str


class QuestionGenerator:

    def __init__(self, path_file: str = r'data\Questions.csv'):

        self.__path_file = path_file
        self.list_of_questions: List[Question] = []

    def fill_in_list_of_questions(self) -> None:

        with open(self.__path_file, encoding='utf8') as file:
            for line in file:
                self.list_of_questions.append(self.parse_line(line))

    @staticmethod
    def parse_line(line) -> Question:

        parsing = line.split(';')
        text = parsing[0]
        is_true = parsing[1] == 'Yes'
        explanation = parsing[2]

        return Question(text, is_true, explanation)

    def generate_questions(self, number_of_questions: int = 6) -> List[Question]:

        if self.list_of_questions:
            if len(self.list_of_questions) < number_of_questions:
                raise ValueError("There are no such number of questions!")
            else:
                return random.sample(self.list_of_questions, number_of_questions)
        else:
            raise ValueError("List of questions is not defined")

