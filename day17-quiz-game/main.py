from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from random import shuffle


question_bank = []
for question in question_data:
    text = question['text']
    answer = question['correct_answer']
    question_object = Question(text, answer)
    question_bank.append(question_object)
shuffle(question_bank)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print('Você completou o desafio!')
print(f'Sua pontuaçao final foi {quiz.score}/{quiz.question_number} pontos.')
