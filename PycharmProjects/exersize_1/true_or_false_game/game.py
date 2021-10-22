from true_or_false_game.Answer import Answer
from true_or_false_game.game_status import GameStatus
from true_or_false_game.question import QuestionGenerator


class Game:

    def __init__(self: str, questions_generator: QuestionGenerator, number_of_questions: int = 5):
        self.number_of_questions = number_of_questions
        self.number_of_correct_answers = 0
        self.number_of_mistakes = 0
        self.game_status = GameStatus.NOT_STARTED
        self.current_question = 0
        self.question_generator = questions_generator
        self.list_of_questions = questions_generator.generate_questions(number_of_questions)

    def launch_game(self):
        if self.game_status != GameStatus.IN_PROGRESS:
            self.start_game()
            self.finish_game()
        else:
            raise ValueError('Game is already started!')

    def start_game(self) -> None:
        self.game_status = GameStatus.IN_PROGRESS
        while self.game_status != GameStatus.FINISHED:
            self.game_round()

    def finish_game(self):
        self.show_results()
        self.reload_game()

    def game_round(self) -> None:
        if not self.list_of_questions:
            raise ValueError("List of questions is not defined")

        if self.game_status == GameStatus.IN_PROGRESS:
            self.show_question()
            answer = Answer.get_answer()
            self.check_answer(answer)
            self.switch_game_status()
        else:
            raise ValueError('Game is not in progress!')

    def correct_answer(self, answer: Answer) -> bool:
        return (answer.answer == "Y" and self.list_of_questions[self.current_question-1].is_true) or (
                answer.answer == "N" and not self.list_of_questions[self.current_question-1].is_true
        )

    def switch_game_status(self) -> None:
        if self.current_question == self.number_of_questions:
            self.game_status = GameStatus.FINISHED

    def show_question(self) -> None:
        print(self.list_of_questions[self.current_question].text)
        self.current_question += 1

    def check_answer(self, answer: Answer) -> None:
        if self.correct_answer(answer):
            print(f'Correct!\n{self.list_of_questions[self.current_question-1].explanation}')
            self.number_of_correct_answers += 1
        else:
            print(f'No!\n{self.list_of_questions[self.current_question-1].explanation}')
            self.number_of_mistakes += 1

    def show_results(self) -> None:
        print('You are finished!')
        print(f'Your score is {self.number_of_correct_answers / self.number_of_questions * 100}%')
        print(f"You answered {self.number_of_correct_answers} of {self.number_of_questions} questions correctly!")

    def reload_game(self) -> None:
        print('Would you like to reload the game with this question pack?')
        answer = Answer.get_answer()
        if answer.answer == "Y":
            new_game = Game(self.question_generator, self.number_of_questions)
            new_game.launch_game()
