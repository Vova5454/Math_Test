import random


def generate_math_question(a: int, b: int) -> str:
    num1 = random.randint(a, b)
    num2 = random.randint(a, b)
    operator = '+-*/'[random.randint(0, 3)]
    return f'{num1} {operator} {num2}'

def check_answer(question, answer):
    try:
        return float(answer) == eval(question)
    except ValueError:
        return False
        
def math_quiz(num_of_questions):
    print('Добро пожаловать в математический тест!')
    correct_answers = 0
    for g in range(num_of_questions):
        question = generate_math_question(1, 20)
        answer = input(f'{question} = ')
        if check_answer(question, answer):
            correct_answers += 1
    print('Тест завершен.')
    print(f'Вы правильно решили {correct_answers} из {num_of_questions} вопросов.')
    if correct_answers >= num_of_questions * 0.8:
        print(f'Хорошо! Вы получаете оценку A.')
    elif correct_answers >= num_of_questions * 0.6:
        print(f'Хорошо! Вы получаете оценку B.')
    else:
        print(f'Хорошо! Вы получаете оценку C.')

math_quiz(15)