class Answer:

    def __init__(self, answer: str):
        self.answer = answer

    def is_correct(self):
        if self.answer == 'Y' or 'N':
            return True
        else:
            return False

    @staticmethod
    def get_answer():
        answer = Answer(str(input('Enter your answer\n')))
        while not ((answer.answer == 'Y') or (answer.answer == 'N')):
            print("Incorrect answer: 'Y' or 'N' expected")
            answer = Answer(str(input('Enter your answer')))
        return answer
