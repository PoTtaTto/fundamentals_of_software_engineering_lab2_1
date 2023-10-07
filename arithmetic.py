def solve_math_problem():
    print('Task: 4 * 100 - 54')
    user_answer = int(input('Enter your answer: '))
    right_answer = 4 * 100 - 54
    print(f'You\'re answer: {user_answer}\nRight answer: {right_answer}')
    if user_answer == right_answer:
        print('You\'re right!')
    else:
        print('You\'re answer is wrong!')