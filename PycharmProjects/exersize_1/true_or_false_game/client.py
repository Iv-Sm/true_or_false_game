from true_or_false_game.game import Game
from true_or_false_game.question import QuestionGenerator

question_generator = QuestionGenerator()
question_generator.fill_in_list_of_questions()

game = Game(question_generator)

game.launch_game()
